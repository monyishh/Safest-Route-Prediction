from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from osrm import get_routes
from clustering import detect_hotspots
from safety_score import route_safety_score

app = FastAPI(title="Safest Route Prediction API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load crime hotspots once at startup
hotspots, _ = detect_hotspots("../data/crimes.csv")


@app.get("/")
def root():
    return {"status": "Safest Route API is running"}


@app.post("/predict-safe-route")
def predict_safe_route(payload: dict):
    source = payload["source"]
    destination = payload["destination"]
    hour = payload["hour"]

    # Get REAL routes from OSRM
    routes = get_routes(source, destination)

    scores = {}
    for i, route in enumerate(routes):
        scores[f"route_{i+1}"] = route_safety_score(
            route, hotspots, hour
        )

    safest_route = min(scores, key=scores.get)

    return {
        "scores": scores,
        "safest_route": safest_route,
        "routes": {
            f"route_{i+1}": routes[i]
            for i in range(len(routes))
        }
    }
