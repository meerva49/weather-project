# Weather Analytics Platform

## Project Overview

This project builds a weather analytics platform using historical weather data from the Open-Meteo API. The system extracts weather data for multiple cities, performs data profiling and cleaning using pandas, loads the cleaned data into PostgreSQL, and answers business questions through SQL analysis.

## Cities Analyzed

- New York
- Phoenix
- Seattle

## Date Range

January 1, 2024 - December 31, 2024

## Data Source

Historical weather data was collected from the Open-Meteo Archive API.

API Endpoint:
https://archive-api.open-meteo.com/v1/archive

## ETL Process

### Extract

- Retrieved historical weather data from the Open-Meteo API
- Collected daily weather records for three cities
- Saved raw API responses as JSON files

### Profile and Clean

Data quality checks included:

- Missing value detection
- Duplicate record detection
- Data type validation
- Range inspection of weather metrics

The nested JSON responses from the Open-Meteo API were transformed into a tabular format using pandas. Weather measurements were extracted from the API response structure and organized into rows and columns for analysis and database loading.

### Load

- Created a normalized PostgreSQL schema
- Loaded cleaned weather data into PostgreSQL using Python and psycopg
- Established relationships using primary and foreign keys

## Database Schema

### cities

Stores city information.

| Column    | Description |
|-----------|-------------|
| city_id   | Primary Key |
| city_name | City Name   |

### weather_records

Stores daily weather measurements.

| Column | Description |
|----------|-------------|
| record_id | Primary Key |
| city_id | Foreign Key |
| weather_date | Date of observation |
| max_temp | Maximum daily temperature |
| precipitation | Daily precipitation |
| wind_speed | Maximum daily wind speed |

## SQL Business Questions

1. What was the highest recorded temperature in each city?
2. What was the total precipitation for each month?
3. Which week was the windiest week of the year?
4. What was the average rainfall for each city?
5. How many extreme temperature days occurred in each city?
6. Which month was the hottest month of the year?

## Key Findings

- Phoenix recorded the highest temperature at 46.8 degrees Celsius.
- July was the hottest month with an average temperature of 33.87 degrees Celsius.
- Week 2 was the windiest week of the year.
- New York had the highest average precipitation.
- Phoenix experienced 156 extreme temperature days.
- Seattle experienced no days with temperatures above 35 degrees Celsius.

## Technologies Used

- Python - Used to build ETL pipeline and automate data processing tasks.
- pandas - Used for data profiling, cleaning, transformation, and CSV generation.
- requests - Used to retrieve historical weather data from the Open-Meteo API.
- psycopg - Used to connect Python to PostgreSQL and laod cleaned weather data into the database.
- PostgreSQL - Used to store weather data in a normalized relational database.
- pgAdmin - Used to manage the PostgreSQL database and execute SQL queries.
- Git - Used for version control and tracking project changes.
- GitHub - Used to store the project repository and maintain commit history.