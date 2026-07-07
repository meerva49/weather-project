import requests
import json

# dictionary having city names and coordinates
cities = {
    "new_york": (40.7128, -74.0060),
    "phoenix": (33.4484, -112.0740),
    "seattle": (47.6062, -122.3321)
}

# open-meteo historical weather API endpoint
url = "https://archive-api.open-meteo.com/v1/archive"

# loop through each city
for city, (lat, lon) in cities.items():

    # parameters for API request
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31",

        # daily weather metrics
        "daily": (
            "temperature_2m_max,"
            "precipitation_sum,"
            "wind_speed_10m_max"
        )
    }

    # send GET request
    response = requests.get(url, params=params)

    print(f"{city} Status Code:", response.status_code)

    # convert JSON response into python dictionary
    data = response.json()

    # create file path
    file_path = f"data/{city}.json"

    # save JSON response
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"{city}.json saved successfully.")

print("\nAll city weather data has been downloaded.")