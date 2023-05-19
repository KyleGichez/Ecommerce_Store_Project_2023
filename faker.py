from app.models import(
    Customer, Order, Product
)
from app.extensions import db
from faker import Faker
import random

fake = Faker()

# Add new customers to the database
def add_customers():
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
    

# Add new orders to the database
def add_orders():
    customers = Customer.query_all()

    for _ in range(1000):
        # Choose a random customer from the database
        customer = random.choice(customers)
        
        ordered_date = fake.date_time_this_year()
        shipped_date = random.choices([None, fake.date_time_between(start_date = ordered_date)], [10,90])[0]
        
        # Choose either random None or any random date for both delivered and shipped orders
        delivered_date = None
        
        if shipped_date:
            delivered_date = random.choices([None, fake.date_time_between(start_date = shipped_date)], [50,50])[0]
            
            # Choose either random None or one of the coupon codes for the customer orders
            coupon_code = random.choices([None,'FLASH50', 'TODAY30', 'FUN20', 'WELCOME10'], [70,10,10,10])[0]
            
            order = Order(
                customer_id = customer.id,
                ordered_date = ordered_date,
                delivered_date = delivered_date,
                shipped_date = shipped_date,
                coupon_code = coupon_code
            )
            db.session.add(order)
        db.session.commit()
        

# Add products to the database
def add_products():
    for _ in range(10):
        product = Product(
            name = fake.color_name(),
            price = random.randint(10,1000)
        )
        db.session.add(product)
    db.session.commit()
    

# Add order_products items to the database
def add_order_products():
    orders = Order.query_all()
    products = Product.query_all()
    
    for order in orders:
        # Choose random orders from the orders list
        random_orders = random.randint(1,5)
        
        # Create purchased products by sampling products against random_orders
        purchased_products = random.sample(products, random_orders)
        order.products.extend(purchased_products)
    
    db.session.commit()    
    
    
# Generate fake data
def create_fake_data():
    db.create_all()
    add_customers()
    add_orders()
    add_products()
    add_order_products()
    
    print("Fake data successfully generated.....")
    
