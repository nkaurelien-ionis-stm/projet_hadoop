import pandas as pd

from databases.models.erp_order import ErpOrder
from database import session

def load_erp_orders_to_db(filepath, session):
    data = pd.read_csv(filepath)

    data = data.where(pd.notnull(data), None)
    
    for index, row in data.iterrows():
        # print(index, row)
        existing_order = session.query(ErpOrder).filter_by(order_id=row['order_id']).first()
        if existing_order:
            for key, value in row.items():
                setattr(existing_order, key, value)
        else:
            # Create a new order object and add it to the session
            new_order = ErpOrder(**row)
            session.add(new_order)
        session.commit()


# Path to the CSV file
filepath = 'resources/data/fake_erp_orders.csv'

# Function call to load the data
load_erp_orders_to_db(filepath, session)
