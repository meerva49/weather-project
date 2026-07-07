-- create table to store city information
CREATE TABLE cities (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(50) NOT NULL UNIQUE
);

-- create table to store daily weather records
CREATE TABLE weather_records (
    record_id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    weather_date DATE NOT NULL,
    max_temp DECIMAL(5,2),
    precipitation DECIMAL(6,2),
    wind_speed DECIMAL(5,2),

    FOREIGN KEY (city_id)
        REFERENCES cities(city_id)
);