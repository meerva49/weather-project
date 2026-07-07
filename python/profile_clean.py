import json
import pandas as pd

# weather json files
files = [
    "data/new_york.json",
    "data/phoenix.json",
    "data/seattle.json"
]

all_data = []

# load each json file
for file in files:

    with open(file, "r") as f:
        data = json.load(f)

    city_name = file.split("/")[-1].replace(".json", "")

    daily = data["daily"]

    # create dataframe from json
    df = pd.DataFrame({
        "date": daily["time"],
        "max_temp": daily["temperature_2m_max"],
        "precipitation": daily["precipitation_sum"],
        "wind_speed": daily["wind_speed_10m_max"]
    })

    df["city"] = city_name

    all_data.append(df)

# combine all cities into one dataframe
weather_df = pd.concat(all_data, ignore_index=True)

print("\nFIRST 5 ROWS")
print(weather_df.head())

print("\nDATA TYPES")
print(weather_df.dtypes)

print("\nMISSING VALUES")
print(weather_df.isnull().sum())

print("\nDUPLICATES")
print(weather_df.duplicated().sum())

print("\nSUMMARY STATISTICS")
print(weather_df.describe())

# convert date column to datetime format
weather_df["date"] = pd.to_datetime(weather_df["date"])

# sort data by city and date
weather_df = weather_df.sort_values(
    by=["city", "date"]
)

# reset index after sorting
weather_df = weather_df.reset_index(drop=True)

# save cleaned dataset
weather_df.to_csv(
    "data/cleaned_weather_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")
