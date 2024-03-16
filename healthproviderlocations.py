import requests

def get_health_providers_nearby(latitude, longitude):
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=hospital&key={api_key}"
    response = requests.get(url)
    results = response.json()
    health_providers = [(result["name"], result["geometry"]["location"]) for result in results["results"]]
    return health_providers