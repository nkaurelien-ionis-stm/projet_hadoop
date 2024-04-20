import pandas as pd

from databases.models.weatherdata import WeatherData
from databases.models.customer_feedback import ErpOrder
from database import session

def load_weather_data_to_db(filepath, session):
    data = pd.read_csv(filepath)
    for index, row in data.iterrows():
        weather = WeatherData(
            data_id=row['data_id'],
            date=row['date'],
            weather_condition=row['weather_condition'],
            traffic_intensity=row['traffic_intensity'],
            # MinTemp=row['MinTemp'],
            # MaxTemp=row['MaxTemp'],
            # Rainfall=row['Rainfall'],
            # Evaporation=row['Evaporation'],
            # Sunshine=row['Sunshine'],
            # WindGustDir=row['WindGustDir'],
            # WindGustSpeed=row['WindGustSpeed'],
            # WindDir9am=row['WindDir9am'],
            # WindDir3pm=row['WindDir3pm'],
            # WindSpeed9am=row['WindSpeed9am'],
            # WindSpeed3pm=row['WindSpeed3pm'],
            # Humidity9am=row['Humidity9am'],
            # Humidity3pm=row['Humidity3pm'],
            # Pressure9am=row['Pressure9am'],
            # Pressure3pm=row['Pressure3pm'],
            # Cloud9am=row['Cloud9am'],
            # Cloud3pm=row['Cloud3pm'],
            # Temp9am=row['Temp9am'],
            # Temp3pm=row['Temp3pm'],
            # RainToday=row['RainToday'],
            # RISK_MM=row['RISK_MM'],
            # RainTomorrow=row['RainTomorrow']
        )
        session.add(weather)
    session.commit()

# Path to the CSV file
filepath = 'resources/data/fake_weather_data.csv'

# Function call to load the data
load_weather_data_to_db(filepath, session)
