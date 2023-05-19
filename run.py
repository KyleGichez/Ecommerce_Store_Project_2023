from app import *
from app import create_app
#from faker import create_fake_data
#from app import db

# Create application server
app = create_app('development')

if __name__ == '__main__':   
    #create_fake_data()
             
    current_app.run(debug=True)