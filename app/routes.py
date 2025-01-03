from datetime import datetime
from flask import request
from flask import Response
from app.controllers.plan_controller import PlanController
from app.controllers.gender_controller import GenderController
from app.controllers.payment_controller import PaymentController
from app.controllers.state_controller import StateController
from app.controllers.student_controller import StudentController
from flask import Blueprint
import json

main = Blueprint('main', __name__)


def general_response(json_data: any):

    return Response(json.dumps(json_data, ensure_ascii=False), content_type='application/json; charset=utf-8')

def register_routes(app):

    ###------------------PLAN ROUTE----------------------###
    @main.route('/plan', methods=['GET', 'POST'])
    def plan():
        if request.method == 'GET':

            json_data = PlanController.get_all_plan()

        elif request.method == 'POST':

            data = request.get_json()

            json_data = PlanController.get_plan_by_id(data['id'])

        return general_response(json_data)
    
    ###-----------------PAYMENT ROUTE---------------------###
    @main.route('/payment', methods=['GET', 'POST'])
    def payment():
        if request.method == 'GET':

            json_data = PaymentController.get_all_payment()

        elif request.method == 'POST':
            
            data = request.get_json()

            json_data = PaymentController.get_payment_by_id(data['id'])

        return general_response(json_data)

    
    ###------------------STATE ROUTE----------------------###
    @main.route('/state', methods=['GET', 'POST'])
    def state():
        if request.method == 'GET':

            json_data = StateController.get_all_state()

        elif request.method == 'POST':

            data = request.get_json()

            json_data = StateController.get_state_by_id(data['id'])    

        return general_response(json_data)
    

    ###------------------GENDER ROUTE----------------------###
    @main.route('/gender', methods=['GET', 'POST'])
    def gender():
        if request.method == 'GET':

            json_data = GenderController.get_all_gender()

        elif request.method == 'POST':
        
            data = request.get_json()

            json_data = GenderController.get_gender_by_id(data['id'])

        return general_response(json_data)
    
    ###------------------STUDENT ROUTE----------------------###
    @main.route('/student', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def student():

        json_data = {}

        if request.method == 'GET':

           json_data = StudentController.get_all_student()

        elif request.method == 'POST':
            id = request.form.get('id')

            if id is not None:

                name = request.form.get('name')
                email = request.form.get('email')
                gender = request.form.get('gender')
                birthdate = datetime.strptime(request.form.get('birthdate'), "%d/%m/%Y")
                phone = request.form.get('phone')
                state = request.form.get('state')
                city = request.form.get('city')
                neighborhood = request.form.get('neighborhood')
                address = request.form.get('address')
                number = request.form.get('number')
                plan = request.form.get('plan')
                payment = request.form.get('payment')
                
                json_data = StudentController.update_student_by_id(id, name, email, gender, birthdate, phone, state, city, neighborhood, address, number)

            else:
                
                data = request.get_json()

                name = data.get('name')
                email = data.get('email')
                gender = data.get('gender')
                birthdate = datetime.strptime(data.get('birthdate'), "%d/%m/%Y")
                phone = data.get('phone')
                state = data.get('state')
                city = data.get('city')
                neighborhood = data.get('neighborhood')
                address = data.get('address')
                number = data.get('number')
                plan = data.get('plan')
                payment = data.get('payment')

                json_data = StudentController.add_new_student(name, gender, birthdate, email, phone, state, city, neighborhood, address, number, plan, payment)

        elif request.method == 'PUT':
            
            data = request.get_json()

            id = data.get('id')
            name = data.get('name')
            email = data.get('email')
            gender = data.get('gender')
            birthdate = datetime.strptime(data.get('birthdate'), "%d/%m/%Y")
            phone = data.get('phone')
            state = data.get('state')
            city = data.get('city')
            neighborhood = data.get('neighborhood')
            address = data.get('address')
            number = data.get('number')

            json_data = StudentController.update_student_by_id(id, name, email, gender, birthdate, phone, state, city, neighborhood, address, number)


        elif request.method == 'DELETE':

            data = request.get_json()  

            id = data.get('id')

            json_data = StudentController.delete_student_by_id(id) 

        return general_response(json_data)
    
    ###------------------SEARCH ROUTE----------------------###
    @main.route('/search', methods=['GET', 'POST'])
    def student_search():
    
        if request.method == 'GET':

            id = request.args.get('id')  
    
            json_data = StudentController.get_student_by_id(id)
    
        elif request.method == 'POST':    
           
            data = request.get_json()
            
            name = data.get('name')
    
            json_data = StudentController.get_search_student(name)
    
        return general_response(json_data)

    app.register_blueprint(main)

