from data_api import return_weather_data
from direct_api import get_suggestion
from pprint import pprint

pprint(get_suggestion("london"))

#print(return_weather_data(24, 54)["print_weather_data"])