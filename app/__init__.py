from flask import Flask
from .config import config_options

#Register blueprint
def register_blueprint(app):
    from .main import auth as auth_bp
    app.register_blueprint(auth_bp)

#Create and initialize a new flask application
def create_app(config_name):
    print("Flask application running on:", config_name , "server")
    
    app = Flask(__name__)
    app.config.from_object(config_options.get(config_name))
    
    register_blueprint(app)
    
    return app
