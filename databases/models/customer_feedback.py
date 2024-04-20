from sqlalchemy import  Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base


# Define the base class
Base = declarative_base()

# Define the ORM class for the 'weather_data' table
class CustomerFeedback(Base):
    __tablename__ = 'customer_feedback'
    feedback_id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    satisfaction_rating = Column(Integer)
    comment = Column(String(500))