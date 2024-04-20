
DOCUMENTATION="""
To generate a synthetic dataset for the customer_feedback table, which references the erp_orders table via the order_id foreign key, you'll need to generate values that are consistent with those in the erp_orders dataset. The main fields to generate are:

feedback_id: A unique identifier for each feedback entry.
order_id: This will be a reference to the order_id from the erp_orders dataset, implying that you will need to ensure consistency between the two datasets.
satisfaction_rating: A numerical rating, which could range from 1 to 5.
comment: Free-form text feedback which could be either populated or empty.
"""

import pandas as pd
from faker import Faker
import random
import numpy as np

# Initialize Faker
fake = Faker()

# Load the existing orders to get valid order_ids (assuming 'erp_orders.csv' is in the current directory)
orders_df = pd.read_csv('erp_orders.csv')
order_ids = orders_df['order_id'].tolist()

# Define the number of feedback entries
num_entries = 100  # You can adjust this to generate more or fewer entries

# Generate data for each column
feedback_ids = range(1, num_entries + 1)
selected_order_ids = random.choices(order_ids, k=num_entries)  # Randomly select order IDs with replacement
satisfaction_ratings = [random.randint(1, 5) for _ in range(num_entries)]  # Ratings from 1 to 5
comments = [fake.sentence(nb_words=10) if random.random() > 0.2 else None for _ in range(num_entries)]  # 20% chance of no comment

# Create a DataFrame
customer_feedback_df = pd.DataFrame({
    'feedback_id': feedback_ids,
    'order_id': selected_order_ids,
    'satisfaction_rating': satisfaction_ratings,
    'comment': comments
})

# Save the DataFrame to a CSV file
customer_feedback_df.to_csv('customer_feedback.csv', index=False)

print("Customer feedback data has been saved to 'customer_feedback.csv'.")
