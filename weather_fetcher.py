import requests
import pandas as pd


class WeatherFetcher:
    '''
    Weather Fetcher fetch the data from the base-url
    '''

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, latitude, longitude, start_date, end_date):
        self.latitude = latitude
        self.longitude = longitude
        self.start_date = start_date
        self.end_date = end_date

    def fetch(self):
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "daily": "temperature_2m_max,temperature_2m_min,"
                     "temperature_2m_mean,"
                     "wind_speed_10m_max,wind_speed_10m_min,"
                     "wind_speed_10m_mean",
            "timezone": "auto"
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()["daily"]
        df = pd.DataFrame(data)
        df["time"] = pd.to_datetime(df["time"])

        return df
