import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--key', required=True)
args = parser.parse_args()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = args.key

weather_params = {
    "lat": 37.687923, 
    "lon": -122.470207,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())