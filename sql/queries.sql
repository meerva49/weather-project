-- query 1: highest recorded temperature per city
-- find max temp recorded in each city 
-- and then rank cities from hottest to coolest

SELECT
    c.city_name,
    MAX(w.max_temp) AS highest_temperature
FROM weather_records w
JOIN cities c
ON w.city_id = c.city_id
GROUP BY c.city_name
ORDER BY highest_temperature DESC;

-- query 2: total monthly precipitation
-- calculate total rainfall across all cities for each month of year 
-- EXTRACT(MONTH) pulls month number (1-12) from weather_data col

SELECT
    EXTRACT(MONTH FROM weather_date) AS month,
    SUM(precipitation) AS total_precipitation
FROM weather_records
GROUP BY month
ORDER BY month;

-- query 3: windiest week of the year
-- see which week had highest avg wind speed across all weather records
-- wind speed across all weatehr records
-- LIMIT 1 returns only windiest week 

SELECT
    EXTRACT(WEEK FROM weather_date) AS week,
    AVG(wind_speed) AS average_wind_speed
FROM weather_records
GROUP BY week
ORDER BY average_wind_speed DESC
LIMIT 1;

-- query 4: average rainfall by city
-- calculate avg daily precipitation for each city and rank from wettest to driest
-- ROUND (...,2) limits result to 2 decimal places for readability

SELECT
    c.city_name,
    ROUND(AVG(w.precipitation), 2) AS average_precipitation
FROM weather_records w
JOIN cities c
ON w.city_id = c.city_id
GROUP BY c.city_name
ORDER BY average_precipitation DESC;

-- query 5: frequency of extreme temperature days (35 degrees celsius or higher)
-- count how manu days each city experiences temps of 35 deg C or higher
-- helps identify locations w/ frequent extreme heat events

SELECT
    c.city_name,
    COUNT(*) AS extreme_temperature_days
FROM weather_records w
JOIN cities c
ON w.city_id = c.city_id
WHERE w.max_temp >= 35
GROUP BY c.city_name
ORDER BY extreme_temperature_days DESC;

-- query 6: hottest month of the year
-- calculate avg max temp for each month and identify hottest month
-- LIMIT 2 returns only hottest month

SELECT
    c.city_name,
    ROUND(AVG(w.max_temp), 2) AS average_temperature
FROM weather_records w
JOIN cities c
ON w.city_id = c.city_id
GROUP BY c.city_name
ORDER BY average_temperature DESC;