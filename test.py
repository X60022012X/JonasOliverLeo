from direct_api import get_suggestion
import pycountry
import requests

x = get_suggestion("London")

print(x)

coords = (x["London, England, GB"][0], x["London, England, GB"][1])
place = "London, England, GB"

def get_state_code(state_name, country_code):
    subdivisions = pycountry.subdivisions.get(country_code=country_code)
    for sub in subdivisions:
        if sub.name.lower() == state_name.lower():
            return sub.code.split('-')[1]
        
splited = place.split(", ")

state_code = get_state_code(splited[1], splited[2])

api_key = "ba9b0f3ce4e121bee6ffb531794ec625"
units = "metric"
language = "en"

if not state_code:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={splited[0]},{splited[2]}&appid={api_key}&lang={language}&units={units}"
else:
    try:
      url = f"https://api.openweathermap.org/data/2.5/forecast?q={splited[0]},{state_code},{splited[2]}&appid={api_key}&lang={language}&units={units}"
    except:
      url = f"https://api.openweathermap.org/data/2.5/forecast?q={splited[0]},{splited[2]}&appid={api_key}&lang={language}&units={units}"
      

response_forkast = requests.get(url)
data_forkast = response_forkast.json()

print(data_forkast)

