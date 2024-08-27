API_URL = "https://api.open-meteo.com/v1/forecast"

LATITUDE = -23.55

LONGITUDE = -46.63

PARAMS = {
    'latitude': LATITUDE,
    'longitude': LONGITUDE,
    'hourly': 'temperature_2m',
    'current_weather': True
}

DB_PATH = "data/weather.db"
CSV_PATH = "data/weather_data.csv"