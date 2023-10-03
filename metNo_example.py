import requests
import xml.etree.ElementTree as ET
import dotenv
import os
from rich import pretty
from VÄSTERÅS import LAT,LON

# url = f'https://api.met.no/weatherapi/locationforecast/2.0/classic?lat={LAT}&lon={LON}&altitude=90'
url = "https://api.met.no/weatherapi/locationforecast/2.0/classic?lat=59.93&lon=10.72&altitude=90"
weather_data = requests.get(url)

print(weather_data.status_code)
print(weather_data.text)