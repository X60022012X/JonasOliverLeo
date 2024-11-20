import requests

def get_suggestion(city):
    api_key = "ba9b0f3ce4e121bee6ffb531794ec625"
    limit = "10"
    url_direct = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}"

    response_direct = requests.get(url_direct)
    data_direct = response_direct.json()

    suggestions = {}

    for location in data_direct:

        place = f"{location['name']}, {location.get('state', '')}, {location['country']}".replace(", ,", ",")
        coords = [location['lat'], location['lon']]
        
        if place not in suggestions:
            suggestions[place] = coords

    return suggestions