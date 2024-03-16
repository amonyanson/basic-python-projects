from geopy.geocoders import Nominatim

def get_location_by_address(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)

def get_location_name_by_coordinates(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse([latitude, longitude])
    return location.address