from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BaseCoupon(BaseModel):

    name: str
    code : int
    discount : int
    expiry_date : datetime
    status: Optional[bool] = False    

class Update_Coupon(BaseCoupon):
  pass 

class Create_Coupon(BaseCoupon):
  pass

