from sqlalchemy import  Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base


# Define the base class
Base = declarative_base()

# Define the ORM class for the 'weather_data' table

class Order(Base):
    __tablename__ = 'ORDERS'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    payment = Column(Float, nullable=False)
    order_date = Column(Date, nullable=False)
    delivery_date = Column(Date, nullable=False)

    # def __repr__(self):
    #     return f"<Order(order_id={self.order_id}, customer_id={self.customer_id}, payment={self.payment}, order_date={self.order_date}, delivery_date={self.delivery_date})>"