from app.models.state_model import StateModel

class StateController():
    
    def get_all_state():

        return StateModel.get_all_state()
    
    def get_state_by_id(id:int):

        return StateModel.get_state_by_id(id)