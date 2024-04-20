
DOCUMENTATION="""
To generate a synthetic dataset that matches the SQL schema you provided for erp_orders, we'll need to create the following columns:

order_id: Sequential IDs starting from 1.
order_date: Random dates, likely within a reasonable range.
expected_delivery_date: Dates that are later than order_date.
actual_delivery_date: Dates that are close to expected_delivery_date, with some being None to simulate undelivered orders.
delivery_status: Various statuses such as "Delivered", "Pending", "Cancelled".
delivery_cost: Random decimal values representing the cost.
"""

import pandas as pd
from faker import Faker
import random
import numpy as np

# Initialize Faker
fake = Faker()

# Define the number of entries
num_entries = 100  # Adjust as needed

# Generate data for each column
order_ids = range(1, num_entries + 1)
order_dates = [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_entries)]
expected_delivery_dates = [fake.date_between(start_date=order_date, end_date='+30d') for order_date in order_dates]
actual_delivery_dates = [fake.date_between(start_date=order_date, end_date=expected_date) if random.random() > 0.1 else None for order_date, expected_date in zip(order_dates, expected_delivery_dates)]
delivery_statuses = [random.choice(['Delivered', 'Pending', 'Cancelled', 'In Transit']) for _ in range(num_entries)]
delivery_costs = [round(random.uniform(5.00, 100.00), 2) for _ in range(num_entries)]

# Handle None for actual_delivery_date with np.nan for proper handling in pandas
actual_delivery_dates = [date if date is not None else pd.NaT for date in actual_delivery_dates]

# Create a DataFrame
erp_orders_df = pd.DataFrame({
    'order_id': order_ids,
    'order_date': order_dates,
    'expected_delivery_date': expected_delivery_dates,
    'actual_delivery_date': actual_delivery_dates,
    'delivery_status': delivery_statuses,
    'delivery_cost': delivery_costs
})

# Save the DataFrame to a CSV file
erp_orders_df.to_csv('resources/data/fake_erp_orders.csv', index=False)

print(erp_orders_df.head())

print("ERP orders data has been saved to 'resources/data/fake_erp_orders.csv'.")
