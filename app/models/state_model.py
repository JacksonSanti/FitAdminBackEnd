from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column , relationship
from typing import Union
from app.app import db
from datetime import datetime

class StateModel(db.Model):
    __tablename__ = 'State'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    abbreviation: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[Union[DateTime, None]] = mapped_column(DateTime, default=datetime.now())


    students = relationship("StudentModel", back_populates="state")

    def __init__(self, name:str, abbreviation:str, created_at:Union[DateTime, None] = None):
        self.name = name
        self.abbreviation = abbreviation

        if created_at:
            self.created_at = created_at

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "abbreviation": self.abbreviation
        }
  
    def get_all_state():

        states = db.session.query(StateModel).all()

        return [state.to_dict() for state in states]
    
    def get_state_by_id(id:int):

        state = db.session.get(StateModel, id)
    
        return state.to_dict() if state else None
    
    