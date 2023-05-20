from app import *
from app import create_app
from fake_data import create_fake_data
from app.models import db

# Create application server
app = create_app('development', db)

if __name__ == '__main__':   
    with app.app_context():
        create_fake_data()
             
    app.run(debug=True)