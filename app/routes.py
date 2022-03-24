
from .import schema, models
from sqlalchemy.orm import Session
from fastapi import   HTTPException, status, Depends, APIRouter
from .database import  get_db

router = APIRouter(
    prefix= "/coupon", tags= ["COUPONS"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_coupon(coupon:schema.Create_Coupon, db: Session = Depends(get_db)):
    #cursor.execute(''' INSERT INTO "coupons"(name, code, discount, max_discount) VALUES(%s,%s,%s,%s)  RETURNING *''',
    #(new_coupon.name, new_coupon.code, new_coupon.discount, new_coupon.max_discount))
    #newcoupon = cursor.fetchone()
    #conn.commit()
    
    if schema.Create_Coupon.discount > 250:
        return {"Max discount allowed is 250"}
    new_coupon = models.Coupon(**coupon.dict())
    db.add(new_coupon)
    db.commit() 
    db.refresh(new_coupon)  
    return {"new_coupon": new_coupon} 

@router.delete('/{id}')
def delete_coupon(id: int, db: Session = Depends(get_db)):
    #cursor.execute('''DELETE FROM "coupons" WHERE id = %s RETURNING *''', (str(id))) 
    #deleted_coupon = cursor.fetchone
    #conn.commit()
    deleted_coupon = db.query(models.Coupon).filter(models.Coupon.id == id)

    if deleted_coupon== None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail= "Not found")
    deleted_coupon.delete(synchronize_session=False)
    db.commit()
    return{'message':'post deleted'} 


@router.put('/{id}')
def update_coupon(id: int, updated_coupon: schema.Update_Coupon,db: Session = Depends(get_db)):
   #cursor.execute(''' UPDATE "coupons" SET name=%s, code=%s, discount=%s, max_discount=%s WHERE id=%s  RETURNING *''',
   #(new_coupon.name, new_coupon.code, new_coupon.discount, new_coupon.max_discount, str(id))) 
   #coupon = cursor.fetchone()
   #conn.commit()
   coupon_query = db.query(models.Coupon).filter(models.Coupon.id == id)
   new_coupon = coupon_query.first()

   if new_coupon == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Not found")
   coupon_query.update(updated_coupon.dict(), synchronize_session= False)
   db.commit()
   return{'Data':coupon_query.first()}  