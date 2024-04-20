import pandas as pd

from databases.models.weatherdata import WeatherData
from databases.models.customer import Customer
from core.database import session

def load_customers_to_db(filepath, session):
    data = pd.read_csv(filepath)

    data = data.where(pd.notnull(data), None)

    
    for index, row in data.iterrows():
        # print(index, row)
        existing_order = session.query(Customer).filter_by(customer_id=row['customer_id']).first()
        if existing_order:
            for key, value in row.items():
                setattr(existing_order, key, value)
        else:
            # Create a new order object and add it to the session
            new_order = Customer(**row)
            session.add(new_order)
        session.commit()



# Path to the CSV file
filepath = 'resources/data/customers.csv'

# Function call to load the data
load_customers_to_db(filepath, session)
