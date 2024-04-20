from sqlalchemy import  Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base


# Define the base class
Base = declarative_base()

# Define the ORM class for the 'weather_data' table
class WeatherData(Base):
    __tablename__ = 'weather_data'
    data_id = Column(Integer, primary_key=True)
    date = Column(Date)
    weather_condition = Column(String(50))
    traffic_intensity = Column(String(50))
    MinTemp = Column(Float)
    MaxTemp = Column(Float)
    Rainfall = Column(Float)
    Evaporation = Column(Float)
    Sunshine = Column(Float)
    WindGustDir = Column(String(10))
    WindGustSpeed = Column(Float)
    WindDir9am = Column(String(10))
    WindDir3pm = Column(String(10))
    WindSpeed9am = Column(Float)
    WindSpeed3pm = Column(Float)
    Humidity9am = Column(Float)
    Humidity3pm = Column(Float)
    Pressure9am = Column(Float)
    Pressure3pm = Column(Float)
    Cloud9am = Column(Float)
    Cloud3pm = Column(Float)
    Temp9am = Column(Float)
    Temp3pm = Column(Float)
    RainToday = Column(String(5))
    RISK_MM = Column(Float)
    RainTomorrow = Column(String(5))