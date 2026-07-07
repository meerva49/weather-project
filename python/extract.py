import requests
import json

# open meteo historical weather API endpoint
url = "https://archive-api.open-meteo.com/v1/archive"

# parameters for API request
params = {
    # nyc coordinates
    "latitude": 40.7128,
    "longitude": -74.0060,
    # data range for weather data
    "start_date": "2024-01-01",
    "end_date": "2024-01-31",
    # daily weather metrics to retreive
    "daily": "temperature_2m_max,precipitation_sum,wind_speed_10m_max"
}

# send GET request to API
response = requests.get(url, params=params)

# print HTTP status code
# 200 means request was successful
print("Status Code:", response.status_code)

# convert json response to Python dictionary
data = response.json()

# display top level keys by API
#print(data.keys())

# convert json response into a python dictionary 
with open("data/new_york_weather.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file saved successfully.")