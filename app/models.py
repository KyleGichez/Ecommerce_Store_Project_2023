from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Create a customers table model
class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    
    # Create a database relationship that links a customer to all their orders
    orders = db.relationship('Order', backref=db.backref('customer', lazy = True))
    
    def __init__(self, first_name, last_name, address, city, postcode, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.postcode = postcode
        self.email = email
    
    def __repr__(self):
        return f"Customer('{self.id}', '{self.first_name}', '{self.last_name}', '{self.address}', '{self.city}', '{self.postcode}', '{self.email}')"
    
    
    # Create an association table that links an order to a product
    order_product = db.Table('order_product',
        db.Column('order.id', db.Integer, db.ForeignKey('orders.id'), primary_key = True),
        db.Column('product.id', db.Integer, db.ForeignKey('products.id'), primary_key = True)
        )
    
    
# Create an orders table model
class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    ordered_date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(255))
    
    #Create a variable that links a customer to an order
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False) 
    
    #Create a database relationship that links products to an order  
    products = db.relationship('Product', secondary='order_product')
    
    def __init__(self, ordered_date, shipped_date, delivered_date, coupon_code, customer_id):
        self.ordered_date = ordered_date
        self.shipped_date = shipped_date
        self.delivered_date = delivered_date
        self.coupon_code = coupon_code
        self.customer_id = customer_id
    
    def __repr__(self):
        return f"Order('{self.id}', '{self.ordered_date}', '{self.shipped_date}', '{self.delivered_date}', '{self.coupon_code}')"
    
    
# Create a products table model
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique = True)
    price = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"Product('{self.id}', '{self.name}', '{self.price}')"
        