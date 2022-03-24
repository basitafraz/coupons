from xmlrpc.client import DateTime
from .database import Base 
from sqlalchemy import Column, Integer, String, DateTime,Boolean


class Coupon(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key = True, nullable = False)
    name= Column(String, nullable= False)
    code = Column(String, nullable=True, unique= True)
    discount = Column(Integer, nullable = False)
    expiry_date = Column(DateTime,nullable= False)
    status= Column(Boolean, default = False,nullable= False)   
  