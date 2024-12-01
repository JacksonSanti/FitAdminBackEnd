from app.models.gender_model import GenderModel

class GenderController():
    
    
    def get_all_gender():

        return GenderModel.get_all_gender()
    
    
    def get_gender_by_id(id:int):

        return GenderModel.get_gender_by_id(id)