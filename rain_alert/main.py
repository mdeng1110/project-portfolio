import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "28d1a43cd11b6c764d9474bf21e644f3"

weather_params = {
    "lat": 37.687923, 
    "lon": -122.470207,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())