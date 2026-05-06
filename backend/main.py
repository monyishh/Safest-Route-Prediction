from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .osrm import get_routes
from .clustering import detect_hotspots
from .safety_score import route_safety_score

app = FastAPI(title="Safest Route Prediction API")

# Enable CORS for frontend if accessing the API from a different origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

# Load crime hotspots once at startup
data_file = Path(__file__).resolve().parent.parent / "data" / "crimes.csv"
hotspots, _ = detect_hotspots(str(data_file))


@app.get("/")
def root():
    return FileResponse(frontend_dir / "index.html")


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


# Vercel expects the app to be exported as 'app'
# This is required for Vercel Python runtime
