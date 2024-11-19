import requests
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime



def get_data(lat, lon):
    api_key = "ba9b0f3ce4e121bee6ffb531794ec625"
    units = "metric"
    language = "en"

    url_forkast = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&lang={language}&units={units}"
   
    response_forkast = requests.get(url_forkast)
    data_forkast = response_forkast.json()
  
    return data_forkast



def render_info(data_forkast):
    weather_info = {}
    
    for x, y in data_forkast.get("city", {}).items():
        weather_info[x] = y

    weather_info["entries"] = data_forkast.get("cnt", None)
    weather_info["code"] = data_forkast.get("cod", None)
    sunrise_unix = weather_info.get("sunrise", None)
    sunset_unix = weather_info.get("sunset", None)
    
    if sunrise_unix is not None:
        weather_info["sunrise"] = {
            "Unix": sunrise_unix,
            "UTC": datetime.utcfromtimestamp(sunrise_unix).strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        weather_info["sunrise"] = {"Unix": None, "UTC": None}

    if sunset_unix is not None:
        weather_info["sunset"] = {
            "Unix": sunset_unix,
            "UTC": datetime.utcfromtimestamp(sunset_unix).strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        weather_info["sunset"] = {"Unix": None, "UTC": None}

  
    timezone_sec = weather_info.get("timezone", None)
    if timezone_sec is not None:
      z = "" 
      if timezone_sec > 0:
        z = "+"
        weather_info["timezone"] = {
            "sec": timezone_sec,
            "UTC": f"UTC{z}{int(timezone_sec) / 3600:.0f}"
        }
    else:
        weather_info["timezone"] = {"sec": None, "UTC": None}

    return weather_info


def render_data(data_forkast):
    weather_data = {
      "clouds": [],
      "time": [],
      "atmospheric_pressure_at_ground_level": [],
      "atmospheric_pressure_at_sea_level": [],
      "sea_level_pressure": [],
      "humidity": [],
      "temperature": [],
      "min_temperature": [],
      "max_temperature": [],
      "feels_like": [],
      "probability_of_precipitation": [],
      "visibility": [],
      "wind_gust_speed": [],
      "wind_speed": [],
      "wind_direction": []
    }

    for i in data_forkast["list"]:
        weather_data["clouds"].append(i.get("clouds", {}).get("all", None))
        weather_data["time"].append(i.get("dt_txt", None))
        weather_data["atmospheric_pressure_at_ground_level"].append(i.get("main", {}).get("grnd_level", None))
        weather_data["atmospheric_pressure_at_sea_level"].append(i.get("main", {}).get("pressure", None))
        weather_data["sea_level_pressure"].append(i.get("main", {}).get("sea_level", None))
        weather_data["humidity"].append(i.get("main", {}).get("humidity", None))
        weather_data["temperature"].append(i.get("main", {}).get("temp", None))
        weather_data["min_temperature"].append(i.get("main", {}).get("temp_min", None))
        weather_data["max_temperature"].append(i.get("main", {}).get("temp_max", None))
        weather_data["feels_like"].append(i.get("main", {}).get("feels_like", None))
        weather_data["probability_of_precipitation"].append(i.get("pop", None))
        weather_data["visibility"].append(i.get("visibility", None))
        weather_data["wind_gust_speed"].append(i.get("wind", {}).get("gust", None))
        weather_data["wind_speed"].append(i.get("wind", {}).get("speed", None))
        weather_data["wind_direction"].append(i.get("wind", {}).get("deg", None))

    return weather_data



def print_weather_info(weather_info):
    result = "\n\n" + "-" * 35 + "\n"
    
    for key, value in weather_info.items():
        if isinstance(value, dict):
            result += f"{key}:\n"
            for sub_key, sub_value in value.items():
                result += f"  | {sub_key:5}:  {sub_value}\n"
        else:
            result += f"{key:10}:  {value}\n"
        
        result += "-" * 35 + "\n"
    
    result += "\n\n"
    return result



def print_weather_data(weather_data):
    result = "\n\n" + "-" * 120 + "\n"
    for key, value in weather_data.items():
        result += f"\n{key}:   {value}\n\n"
        result += "-" * 120 + "\n"
    result += "\n"
    return result

   
   
def return_weather_data(lat, lon):
    data_forkast = get_data(lat, lon)
    
    data_dict = {}

    data_dict["weather_info"] = render_info(data_forkast)
    data_dict["weather_data"] = render_data(data_forkast)
    data_dict["print_weather_info"] = print_weather_info(data_dict["weather_info"])
    data_dict["print_weather_data"] = print_weather_data(data_dict["weather_data"])

    return data_dict
