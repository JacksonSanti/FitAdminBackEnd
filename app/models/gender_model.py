from sqlalchemy import Integer, String, DateTime, Float, text
from sqlalchemy.orm import Mapped, mapped_column , relationship
from typing import Union
from app.app import db
from datetime import datetime

class GenderModel(db.Model):
    __tablename__ = 'Gender'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[Union[DateTime, None]] = mapped_column(DateTime, default=datetime.now())

    students = relationship("StudentModel", back_populates="gender")

    def __init__(self, name: str, created_at: Union[DateTime, None] = None):
        self.name = name
        if created_at:
            self.created_at = created_at

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name
        }
    
    def get_all_gender():

        genders = db.session.query(GenderModel).all()

        return [gender.to_dict() for gender in genders]

    def get_gender_by_id(id: int):

        gender = db.session.get(GenderModel,id)

        return gender.to_dict() if gender else None


    
    
