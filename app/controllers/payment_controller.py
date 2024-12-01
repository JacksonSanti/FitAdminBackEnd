from app.models.payment_model import PaymentModel

class PaymentController():
    
    def get_all_payment():

        return PaymentModel.get_all_payment()
    
    def get_payment_by_id(id:int):

        return PaymentModel.get_payment_by_id(id)