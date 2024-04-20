
DOCUMENTATION="""
To expand the existing weather.csv file by generating more rows and adding the additional columns (data_id, date, weather_condition, and traffic_intensity) according to your database schema, we'll first generate synthetic data for these new fields using Python, specifically using the Faker library for realistic date values and random choices for weather_condition and traffic_intensity.

Here's a step-by-step process:

1- Read the existing CSV file into a pandas DataFrame.
2- Generate new data for the additional columns.
3- Concatenate the new data with the existing DataFrame.
4- Save the expanded DataFrame back to the CSV file.
"""

import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()


# Load the existing data
df = pd.read_csv('resources/kaggle_weather.csv')

# Generate additional data
num_entries = len(df)  # matching the number of new rows to the existing ones

data_id = range(1, num_entries + 1)  # simple sequential IDs starting from 1
dates = [fake.date_between(start_date='-30y', end_date='today') for _ in range(num_entries)]
weather_conditions = [random.choice(['Sunny', 'Cloudy', 'Rainy', 'Stormy', 'Foggy']) for _ in range(num_entries)]
traffic_intensities = [random.choice(['Low', 'Moderate', 'High', 'Very High']) for _ in range(num_entries)]

# Create a new DataFrame with the additional columns
additional_data = pd.DataFrame({
    'data_id': data_id,
    'date': dates,
    'weather_condition': weather_conditions,
    'traffic_intensity': traffic_intensities
})

# Concatenate the new columns with the existing DataFrame
expanded_df = pd.concat([additional_data, df], axis=1)

# Save the expanded DataFrame to a new CSV file
expanded_df.to_csv('external_weather_data.csv', index=False)

print(expanded_df.head())

print("Expanded data has been saved to 'expanded_weather.csv'.")
