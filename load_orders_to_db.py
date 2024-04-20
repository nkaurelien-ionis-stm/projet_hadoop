import pandas as pd

from databases.models.order import Order
from database import session

def load_orders_to_db(filepath, session):
    data = pd.read_csv(filepath)

    data = data.where(pd.notnull(data), None)
    
    for index, row in data.iterrows():
        # print(index, row)
        existing_order = session.query(Order).filter_by(order_id=row['order_id']).first()
        if existing_order:
            for key, value in row.items():
                setattr(existing_order, key, value)
        else:
            # Create a new order object and add it to the session
            new_order = Order(**row)
            session.add(new_order)
        session.commit()


# Path to the CSV file
filepath = 'resources/data/orders.csv'

# Function call to load the data
load_orders_to_db(filepath, session)
