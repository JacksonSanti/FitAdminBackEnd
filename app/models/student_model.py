from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import date, datetime
from typing import Union
from app.app import db

from app.models.gender_model import GenderModel
from app.models.payment_model import PaymentModel
from app.models.plan_model import PlanModel
from app.models.state_model import StateModel

class StudentModel(db.Model):
    __tablename__ = 'Student'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    
    gender_id: Mapped[int] = mapped_column(Integer, ForeignKey("Gender.id")) 
    gender: Mapped["GenderModel"] = relationship("GenderModel", back_populates="students") 
    
    birthday: Mapped[DateTime] = mapped_column(DateTime)
    email: Mapped[str] = mapped_column(String, unique=True)
    phone: Mapped[str] = mapped_column(String)

    state_id: Mapped[str] = mapped_column(String, ForeignKey("State.id"))
    state: Mapped["StateModel"] = relationship("StateModel", back_populates="students") 


    city: Mapped[str] = mapped_column(String)
    neighborhood: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String)
    
    plan_id: Mapped[int] = mapped_column(Integer, ForeignKey("Plan.id"))  
    plan: Mapped["PlanModel"] = relationship("PlanModel", back_populates="students")  

    payment_id: Mapped[int] = mapped_column(Integer, ForeignKey("Payment.id"))  
    payment: Mapped["PaymentModel"] = relationship("PaymentModel", back_populates="students") 

    created_at: Mapped[Union[DateTime, None]] = mapped_column(DateTime, default=datetime.now)

    def __init__(self, name: str, gender_id: int, birthday: DateTime, email: str, phone:str, state_id:int, city:str, neighborhood:str, address:str, number:str, plan_id:int, payment_id: int, created_at: Union[DateTime, None] = None):
        self.name = name
        self.gender_id = gender_id
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.state_id = state_id
        self.city = city
        self.neighborhood = neighborhood
        self.address = address
        self.number = number
        self.plan_id = plan_id
        self.payment_id = payment_id

        if created_at:
            self.created_at = created_at

    def to_dict_all(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": GenderModel.get_gender_by_id(self.gender_id),
            "birthday": self.birthday.strftime('%d/%m/%Y'),  
            "email": self.email,
            "phone": self.phone,
            "state": StateModel.get_state_by_id(self.state_id),
            "city": self.city,
            "neighborhood": self.neighborhood,
            "address": self.address,
            "number": self.number,
            "plan": PlanModel.get_plan_by_id(self.plan_id),
            "payment": PaymentModel.get_payment_by_id(self.payment_id),
        }
    
    def to_dict_info(self):

        return {
            "id":self.id,
            "name":self.name,
            "plan": PlanModel.get_plan_by_id(self.plan_id),
            "payment": PaymentModel.get_payment_by_id(self.payment_id),
        }

    def get_all_student():

        query = db.session.query(StudentModel)

        students  = query.limit(9)

        return [student.to_dict_info() for student in students]
    
    def get_student_by_id(id: int):

        student = db.session.get(StudentModel, id)

        return student.to_dict_all() if student else None
    
    def get_student_by_name(name: str):

        student = db.session.get(StudentModel, name)

        return student.to_dict_info() if student else None

    def delete_student(id: int):

        student = StudentModel.query.get(id) 

        if not student:
            return None 

        db.session.delete(student)  

        db.session.commit()  

        return True

    
    def update_student(self, id:int, name: str, gender_id: int, birthday: DateTime, email: str, phone:str, state_id:int, city:str, neighborhood:str, address:str, number:str, plan_id:int, payment_id: int):

        student = db.session.get(StudentModel, id)

        if not student:

            return None
        
        else:
            student.name = name
            student.gender_id = gender_id
            student.birthday = birthday
            student.email = email
            student.phone = phone
            student.state_id = state_id
            student.city = city
            student.neighborhood = neighborhood
            student.address = address
            student.number = number
            student.plan_id = plan_id
            student.payment_id = payment_id

        return True

