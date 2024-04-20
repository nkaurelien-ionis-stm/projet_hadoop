import pandas as pd

from databases.models.weatherdata import WeatherData
from databases.models.customer_feedback import CustomerFeedback
from database import session

def load_customer_feedback_to_db(filepath, session):
    data = pd.read_csv(filepath)

    data = data.where(pd.notnull(data), None)

    for index, row in data.iterrows():
        model = CustomerFeedback(
            feedback_id=row['feedback_id'],
            order_id=row['order_id'],
            comment=row['comment'] or None,
            satisfaction_rating=row['satisfaction_rating'] or 0,
        )
        session.add(model)
    session.commit()


# Path to the CSV file
filepath = 'resources/data/fake_customer_feedback.csv'

# Function call to load the data
load_customer_feedback_to_db(filepath, session)
