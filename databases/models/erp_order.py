from sqlalchemy import  Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base


# Define the base class
Base = declarative_base()

# Define the ORM class for the 'weather_data' table
class ErpOrder(Base):
    __tablename__ = 'erp_orders'
    order_id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    expected_delivery_date = Column(Date, nullable=False)
    actual_delivery_date = Column(Date)
    delivery_status = Column(String(50))
    delivery_cost = Column(Float)

    # def __repr__(self):
    #     return f"<ErpOrder(order_id={self.order_id}, order_date={self.order_date}, expected_delivery={self.expected_delivery_date}, actual_delivery={self.actual_delivery_date}, status={self.delivery_status}, cost={self.delivery_cost})>"
