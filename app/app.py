from flask import Flask
from flask_cors import CORS
from app.db import db  
from app.routes import register_routes  
from app.models.base import Base
from flask_swagger_ui import get_swaggerui_blueprint

from flask_cors import CORS

def create_app():

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'


    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "FitAdmin API"
        }
    )
    
    app = Flask(__name__)
    CORS(app)
    app.debug = True

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitadmin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
 
    with app.app_context():
        from app.models.plan_model import PlanModel
        from app.models.gender_model import GenderModel
        from app.models.payment_model import PaymentModel
        from app.models.student_model import StudentModel
        db.create_all() 
   
    register_routes(app)  

    return app

