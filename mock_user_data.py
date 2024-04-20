
import pandas as pd
from faker import Faker
import random
import os


def user_data():
    # Initialize Faker
    fake = Faker()

    # Set the number of entries
    num_entries = 100

    # Create lists to store the generated data
    names = []
    addresses = []
    emails = []

    # Generate fake data
    for _ in range(num_entries):
        names.append(fake.name())
        addresses.append(fake.address())
        emails.append(fake.email())

    # Create a DataFrame
    data = {
        'Name': names,
        'Address': addresses,
        'Email': emails
    }
    df = pd.DataFrame(data)

    # Display the first few rows of the DataFrame
    print(df.head())



    # Save the DataFrame to a CSV file
    df.to_csv('fake_user_data.csv', index=False)

    # Optionally, print a confirmation or information
    print("The DataFrame has been saved to a CSV file named 'fake_data.csv'.")

if __name__ == "__main__":
    user_data()