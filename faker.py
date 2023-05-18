from app.models import(
    Customer, Order, Product, OrderProduct
)
from app.extensions import db
from faker import Faker
import random

fake = Faker()

#Add new customers to the database
def add_customer():
    for _ in range(100):
        customer = Customer(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            address = fake.address(),
            city = fake.city(),
            postcode = fake.postcode(),
            email = fake.email()
        )
        db.session.add(customer)
    db.session.commit()
    

# Add new orders created by customers to the database
def add_orders():
    customers = Customer.query_all()

    for _ in range(1000):
        #Choose a random customer from the database
        customer = random.choice(customers)
        
        ordered_date = fake.date_time_this_year()
        shipped_date = random.choice(None, fake.date_time_between(start_date = ordered_date))[10,90][0]
        
        #Choose either a random None or a random date for both delivered and shipped dates
        delivery_date = None
        
        if shipped_date:
            delivery_date = random.choice(None, fake.date_time_between(start_date = shipped_date))[50,50]
            
            