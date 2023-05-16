from environs import Env

env = Env()
env.read_env()

#Create application configuration
class Config:
    TESTING = False
    SECRET_KEY = env.str('S_K')
    
#Create production configuration
class ProdConfig(Config):
    pass
    DEBUG = True
    
#Create development configuration
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'
    
#Create testing configuration
class TestConfig(Config):
    DEBUG = True
    TESTING = True
    
#Create all configuration options as a dictionary object
config_options = dict(
    development = DevConfig(),
    production = ProdConfig(),
    testing = TestConfig()
)