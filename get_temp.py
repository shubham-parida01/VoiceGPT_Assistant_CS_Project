from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import geocoder


def get_user_city():
        g = geocoder.ip('me')
        if g.ok:
                city = g.city
                return city
        else:
                return None

def get_current_temperature():
        city = get_user_city()
        a = city.upper()
        config_dict = get_default_config()
        config_dict['language'] = 'en'
        owm = OWM('b370eb042aeff27bf40b61f859919490', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(a)
        weather = observation.weather
        weather_description = weather.detailed_status
        temperature = weather.temperature('celsius')
        return [weather_description,temperature['temp'],a]

def get_current_temperature_place(s):
        config_dict = get_default_config()
        config_dict['language'] = 'en'
        owm = OWM('b370eb042aeff27bf40b61f859919490', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(s)
        weather = observation.weather
        weather_description = weather.status
        temperature = weather.temperature('celsius')
        return [weather_description,temperature['temp']]