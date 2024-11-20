import requests
from pprint import pprint

def get_suggestion(city):
    api_key = "ba9b0f3ce4e121bee6ffb531794ec625"
    limit = "10"
    url_direct = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={api_key}"

    response_direct = requests.get(url_direct)
    data_direct = response_direct.json()

    suggestions = []
    for i in data_direct:
        temp_dict = {}

        if i.get("state"):
            temp_dict["place"] = f"{i['name']}, {i['state']}, {i['country']}"
        else:
            temp_dict["place"] = f"{i['name']}, {i['country']}"

        temp_dict["coordinates"] = [i['lat'], i['lon']]
        
        suggestions.append(temp_dict)

    # Print all collected suggestions
    pprint(suggestions)

    # Optionally, print the raw response data
    pprint(data_direct)

get_suggestion("Oslo")