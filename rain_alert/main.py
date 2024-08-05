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
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")