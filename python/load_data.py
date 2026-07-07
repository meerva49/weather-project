import pandas as pd
import psycopg

# read cleaned CSV
weather_df = pd.read_csv("data/cleaned_weather_data.csv")

# connect to postgreSQL using psycopg
conn = psycopg.connect(
    dbname="weather_project",
    user="postgres",
    password="PinkUnicorn1%",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# dictionary to match city names with city_id
city_ids = {
    "new_york": 1,
    "phoenix": 2,
    "seattle": 3
}

# insert each weather record
for _, row in weather_df.iterrows():

    cur.execute(
        """
        INSERT INTO weather_records
        (city_id, weather_date, max_temp, precipitation, wind_speed)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            city_ids[row["city"]],
            row["date"],
            row["max_temp"],
            row["precipitation"],
            row["wind_speed"]
        )
    )

# save changes
conn.commit()

# close connection
cur.close()
conn.close()

print("Weather data loaded successfully.")