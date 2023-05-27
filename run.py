from app import *
from app import create_app
from fake_data import create_fake_data

# Create application server
app = create_app('development')

if __name__ == '__main__':   
    with app.app_context():
        create_fake_data()
             
    app.run(debug=True)