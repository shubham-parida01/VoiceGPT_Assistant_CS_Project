from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
b = input("Enter place:")
a = b.upper()
config_dict = get_default_config()
config_dict['language'] = 'en'

owm = OWM('b370eb042aeff27bf40b61f859919490', config_dict)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(a)
weather = observation.weather
temperature = weather.temperature('celsius')

print(f"The current temperature is {temperature['temp']} degree celsius.")
