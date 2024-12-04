from sqlalchemy import DateTime
from app.models.student_model import StudentModel

class StudentController():
    
    def add_student(name: str, gender_id: int, birthday: str, email: str, phone: str, state_id: int, city: str, neighborhood: str, address: str, number: str, plan_id: int, payment_id: int):
        
        return StudentModel.add_student(name, gender_id, birthday, email, phone, state_id, city, neighborhood , address , number , plan_id , payment_id)

    def get_all_student():

        return StudentModel.get_all_student()

    def get_student_by_id(id:int):

        return StudentModel.get_student_by_id(id)
    
    def get_search_student(name:str):

        return StudentModel.get_student_by_name(name)
    
    def delete_student_by_id(id: int):

        return StudentModel.delete_student(id)

    def update_student_by_id(id: int, name: str, email: str, gender_id: int, birthday: DateTime, phone: str, state_id: int, city: str, neighborhood: str, address: str, number: str):

        try:
            return StudentModel.update_student_by_id(
                id, name, gender_id, birthday, email, phone, state_id, city, neighborhood, address, number
            )
        except Exception as e:
            return {"success": False, "message": f"Erro ao atualizar o aluno: {str(e)}"}
        
    def add_new_student(name: str, gender_id: int, birthday: DateTime, email: str, phone:str, state_id:int, city:str, neighborhood:str, address:str, number:str, plan_id: int, payment_id: int):

        try:
            return StudentModel.add_new_student(name, gender_id, birthday, email, phone, state_id, city, neighborhood, address, number, plan_id, payment_id)
        
        except Exception as e:
            
            return {"success": False, "message": f"Erro ao criar aluno:: {str(e)}"}
