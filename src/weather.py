import pandas as pd
import openmeteo_requests

from config import API_URL, PARAMS, CSV_PATH
from utils import setup_session, save_to_csv
from database import create_table, insert_weather_data

def get_weather():
    try:
        # Setup the session with cache and retries
        session = setup_session()
        openmeteo = openmeteo_requests.Client(session=session)

        # Fetch weather data
        responses = openmeteo.weather_api(API_URL, params=PARAMS)

        # Process first location. You can extend to handle multiple locations.
        response = responses[0]

        # Extract hourly data
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ),
            "temperature_2m": hourly_temperature_2m
        }

        # Create DataFrame
        hourly_dataframe = pd.DataFrame(data=hourly_data)

        # Save data to CSV
        save_to_csv(hourly_dataframe, CSV_PATH)

        # Save data to SQLite database
        create_table()
        insert_weather_data(hourly_dataframe)

        print("Data saved successfully!")
        print(hourly_dataframe)

    except Exception as e:
        print(f"Error retrieving weather data: {e}")

if __name__ == "__main__":
    get_weather()