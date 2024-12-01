from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column , relationship
from typing import Union
from app.app import db
from datetime import datetime

class PaymentModel(db.Model):
    __tablename__ = 'Payment'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    method: Mapped[str] = mapped_column(String, unique=True)
    discount: Mapped[float] = mapped_column(Float)
    created_at:  Mapped[Union[DateTime, None]] = mapped_column(DateTime, default=datetime.now())

    students = relationship("StudentModel", back_populates="payment")

    def __init__(self, method:str, discount:float, created_at:Union[DateTime, None] = None):
        self.method = method
        self.discount =  discount

        if created_at:
            self.created_at = created_at

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.method,
            "discount": self.discount
        }

    def get_all_payment():

        payments = db.session.query(PaymentModel).all()
    
        return [payment.to_dict() for payment in payments]

    def get_payment_by_id(id:int):

        payment = db.session.get(PaymentModel, id)

        return payment.to_dict() if payment else None
