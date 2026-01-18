from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def route_safety_score(route_points, hotspots, hour):
    crime_near_route = 0

    for _, crime in hotspots.iterrows():
        for point in route_points:
            if distance((crime.lat, crime.lng), point) < 0.001:
                crime_near_route += 1
                break

    night_factor = 1.5 if hour >= 20 or hour <= 5 else 1.0

    score = crime_near_route * night_factor
    return score
