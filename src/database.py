import sqlite3
import pandas as pd

from config import DB_PATH

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Drop the table if it already exists
    cursor.execute('DROP TABLE IF EXISTS WeatherData')

    # Create the table with the correct structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WeatherData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            temperature_2m REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_weather_data(dataframe):
    conn = sqlite3.connect(DB_PATH)
    dataframe.to_sql('WeatherData', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

def fetch_all_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql('SELECT * FROM WeatherData', conn)
    conn.close()
    return df