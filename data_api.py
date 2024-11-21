import requests
import pycountry
from datetime import datetime


def get_data(city):
    city_list = city.split(", ")
    state_name = city_list[1]
    country_code = city_list[2]

    subdivisions = pycountry.subdivisions.get(country_code=country_code)
    for sub in subdivisions:
        if sub.name.lower() == state_name.lower():
            state_code = sub.code.split('-')[1]

    api_key = "ba9b0f3ce4e121bee6ffb531794ec625"
    units = "metric"
    language = "en"


    if not state_code:
        url_forkast = f"https://api.openweathermap.org/data/2.5/forecast?q={city_list[0]},{city_list[1]}&appid={api_key}&lang={language}&units={units}"
    else:
        try:
            url_forkast = f"https://api.openweathermap.org/data/2.5/forecast?q={city_list[0]},{state_code},{city_list[2]}&appid={api_key}&lang={language}&units={units}"
        except:
            url_forkast = f"https://api.openweathermap.org/data/2.5/forecast?q={city_list[0]},{city_list[1]}&appid={api_key}&lang={language}&units={units}"
   
    response_forkast = requests.get(url_forkast)
    data_forkast = response_forkast.json()

    return data_forkast





def return_city_info(city):
    forkast_data = get_data(city)
    weather_info = forkast_data.get("city", {}).copy()


    weather_info["entries"] = forkast_data.get("cnt")
    weather_info["code"] = forkast_data.get("cod")


    def format_unix_time(unix_time):
        if unix_time is not None:
            return {"Unix": unix_time, "ISO_8601": datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')}
        else:
            return {"Unix": None, "ISO_8601": None}
    
    weather_info["sunrise"] = format_unix_time(weather_info.get("sunrise"))
    weather_info["sunset"] = format_unix_time(weather_info.get("sunset"))
  

    timezone_sec = weather_info.get("timezone")
    if timezone_sec is not None:
        weather_info["timezone"] = {
            "offset_sec": timezone_sec,
            "UTC": f"UTC{'+' if timezone_sec > 0 else ''}{timezone_sec / 3600:.0f}"
        }
    else:
        weather_info["timezone"] = {"offset_sec": None, "UTC": None}


    return weather_info





def return_city_weather_data(city):
    forkast_data = get_data(city)

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

    for i in forkast_data["list"]:
        weather_data["clouds"].append(i.get("clouds", {}).get("all"))
        weather_data["time"].append(i.get("dt_txt"))
        weather_data["atmospheric_pressure_at_ground_level"].append(i.get("main", {}).get("grnd_level"))
        weather_data["atmospheric_pressure_at_sea_level"].append(i.get("main", {}).get("pressure"))
        weather_data["sea_level_pressure"].append(i.get("main", {}).get("sea_level",))
        weather_data["humidity"].append(i.get("main", {}).get("humidity"))
        weather_data["temperature"].append(i.get("main", {}).get("temp"))
        weather_data["min_temperature"].append(i.get("main", {}).get("temp_min"))
        weather_data["max_temperature"].append(i.get("main", {}).get("temp_max"))
        weather_data["feels_like"].append(i.get("main", {}).get("feels_like"))
        weather_data["probability_of_precipitation"].append(i.get("pop"))
        weather_data["visibility"].append(i.get("visibility"))
        weather_data["wind_gust_speed"].append(i.get("wind", {}).get("gust"))
        weather_data["wind_speed"].append(i.get("wind", {}).get("speed"))
        weather_data["wind_direction"].append(i.get("wind", {}).get("deg"))

    return weather_data





def return_weather_info_string(city):
    weather_info = return_city_info(city)

    string =  "\n" + "* CITY INFO *" + "\n" + "-" * 35 + "\n"
    for key, value in weather_info.items():
        if isinstance(value, dict):
            string += f"{key}:\n"
            for sub_key, sub_value in value.items():
                string += f"  - {sub_key:11}:  {sub_value}\n"
        else:
            string += f"{key:10}:  {value}\n"   
        string += "-" * 35 + "\n"
    
    return string





def return_weather_data_string(city):
    weather_data = return_city_weather_data(city)

    string = "\n" + "* WEATHER DATA *" + "\n" + "-" * 120 + "\n"
    for key, value in weather_data.items():
        string += f"\n{key}:   {value}\n"
        string += "\n" + "-" * 120 + "\n"

    return string