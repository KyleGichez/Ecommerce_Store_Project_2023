from flask import Flask, current_app
from .config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Register blueprint
def register_blueprint(app):
    from .main import auth as auth_bp
    app.register_blueprint(auth_bp)
    

#Create and initialize a new flask application
def create_app(config_name):
    print("Flask application running on:", config_name , "server")
    
    app = Flask(__name__)
    app.config.from_object(config_options.get(config_name))      
    db.init_app(app)
    
    # register_extensions(app)
    register_blueprint(app)
    
    with app.app_context():
        current_app.run()
        
    return app
