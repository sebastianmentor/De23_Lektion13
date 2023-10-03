import requests
import dotenv
import os
from rich import print_json
from VÄSTERÅS import LAT,LON

# https://openweathermap.org/api/one-call-3

dotenv.load_dotenv('.env')

OPENWEATHERMAP_APIKEY = os.getenv("OPENWEATHERMAP_APIKEY")
url = f'https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&appid={OPENWEATHERMAP_APIKEY}&exclude=current,minutely,daily&lang=sv&units=metric'
weather_data = requests.get(url)

print_json(data=weather_data.json())