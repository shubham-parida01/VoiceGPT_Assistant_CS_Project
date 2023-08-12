from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

def get_current_temperature(place:str):
    a = place.upper()
    config_dict = get_default_config()
    config_dict['language'] = 'en'

    owm = OWM('b370eb042aeff27bf40b61f859919490', config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(a)
    weather = observation.weather
    temperature = weather.temperature('celsius')

    return temperature['temp']


