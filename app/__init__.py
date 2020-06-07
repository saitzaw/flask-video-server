""" register the module """  
from flask import Flask 

def create_app(): 
    """ For the core application """ 

    app = Flask(__name__,instance_relative_config=False) 
    app.config.from_object('config.Config')
    with app.app_context(): 
        from app import routes 
        app.register_blueprint(routes.main)
        return app