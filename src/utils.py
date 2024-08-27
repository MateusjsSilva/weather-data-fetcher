import os
import pandas as pd
import requests_cache

from retry_requests import retry

def setup_session():
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    return retry_session

def save_to_csv(dataframe, csv_path):
    try:
        directory = os.path.dirname(csv_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        dataframe.to_csv(csv_path, mode='a', header=not pd.io.common.os.path.exists(csv_path), index=False)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")