from sqlalchemy import  Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base


# Define the base class
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'CUSTOMERS'
    
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(255), nullable=False)
    gender = Column(String(50))
    age = Column(Integer)
    home_address = Column(String(255))
    zip_code = Column(String(20))
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))

    # def __repr__(self):
    #     return f"<Customer(customer_id={self.customer_id}, customer_name='{self.customer_name}', gender='{self.gender}', age={self.age}, address='{self.home_address}', zip='{self.zip_code}', city='{self.city}', state='{self.state}', country='{self.country}')>"
