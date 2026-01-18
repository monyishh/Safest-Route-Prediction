import requests

def get_routes(source, destination):
    #makes the message format to ask for routes
    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{source['lng']},{source['lat']};"
        f"{destination['lng']},{destination['lat']}"
        f"?alternatives=true&geometries=geojson"
    )

    response = requests.get(url) # sends the request to the OSRM server
    data = response.json() # parses the JSON response

    routes = [] #list to store the routes

    # Extract each route's coordinates
    for route in data["routes"]:
        coords = [
            (lat, lng)
            for lng, lat in route["geometry"]["coordinates"]
        ]
        routes.append(coords)

    return routes
