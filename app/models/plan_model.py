from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column , relationship
from typing import Union
from app.app import db
from datetime import datetime


class PlanModel(db.Model):
    __tablename__ =  'Plan'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    value: Mapped[float] = mapped_column(Float)
    created_at: Mapped[Union[DateTime, None]] = mapped_column(DateTime, default=datetime.now())

    students = relationship("StudentModel", back_populates="plan")

    def __init__(self, name:str, value:float, created_at:Union[DateTime, None] = None):
        self.name = name
        self.value = value

        if created_at:
            self.created_at = created_at

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "value": self.value
        }
    
    def get_all_plan():

        plans = db.session.query(PlanModel).all()

        return [plan.to_dict() for plan in plans]
    
    def get_plan_by_id(id:int):

        plan = db.session.get(PlanModel, id)

        return plan.to_dict() if plan else None

    



        


