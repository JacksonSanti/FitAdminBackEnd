from app.models.plan_model import PlanModel

class PlanController():

    def get_all_plan():

        return PlanModel.get_all_plan()
    
    def get_plan_by_id(id: int):

        return PlanModel.get_plan_by_id(id)