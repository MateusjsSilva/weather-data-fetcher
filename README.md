# Weather Data Fetcher

Weather Data Fetcher is a Python-based project designed to consume weather data from the Open-Meteo API. The project fetches hourly temperature data for a specified location, processes it, and stores the results in both a CSV file and a SQLite database. The project is modularized and includes error handling, caching, and retry logic for robust API interaction.

## Features

- Fetches weather data using the [Open-Meteo API](https://open-meteo.com/).
- Caches API responses to reduce redundant requests.
- Retries API requests on failure with a configurable backoff strategy.
- Saves weather data to a SQLite database.
- Exports weather data to a CSV file.

## Project Structure

```plaintext
weather-py/
|
└── src   
    ├── config.py             # API configurations and constants
    ├── database.py           # Functions for database interactions
    ├── weather.py            # Main script to fetch and process weather data
    ├── utils.py              # Utility functions and error handling
    ├── requirements.txt      # Project dependencies
    ├── .gitignore            # Git ignore file
    └── data/
        ├── weather_data.csv  # CSV file where weather data is stored
        └── weather.db        # SQLite database where weather data is stored
```

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/MateusjsSilva/weather-data-fetcher.git
    cd weather-data-fetcher/src
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
API Configuration: The API endpoint, location coordinates, and other settings are stored in config.py. Adjust these values according to your needs.

## Usage
Run the weather data fetcher:
```bash
python weather.py
```
Output:
- The weather data will be printed to the console.
- Data will be saved in data/weather_data.csv.
- Data will be stored in the SQLite database at data/weather.db.

## Error Handling
The script includes basic error handling to manage exceptions that might occur during API requests or while saving data. Errors are logged to the console for debugging purposes.

## Contribution

Feel free to open issues or submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.