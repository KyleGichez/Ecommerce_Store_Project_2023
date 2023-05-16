from .extensions import db
from datetime import datetime

#Create a customers table model
class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.integer, primary_key=True)
    first_name = db.Column(db.string(255), nullable=False)
    last_name = db.Column(db.string(255), nullable=False)
    address = db.Column(db.string(255), nullable=False)
    city = db.Column(db.string(255), nullable=False)
    postcode = db.Column(db.integer, nullable=False)
    email = db.Column(db.string(255), nullable=False, unique=True)
    
    #Create a database relationship that links a customer to all their orders
    orders = db.relationship('Order', backref='customer')
    
    def __init__(self, first_name, last_name, address, city, postcode, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.postcode = postcode
        self.email = email
    
    def __repr__(self):
        return f"Customer('{self.id}','{self.first_name}','{self.last_name}','{self.address}','{self.city}','{self.postcode}','{self.email}')"
    
    
#Create an orders table model
class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.integer, primary_key=True)
    ordered_date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.string(255))
    
    #Create a database relationship that links an order to the customer
    customer_id = db.Column(db.integer, db.ForeignKey('customers.id'), nullable=False) 
    
    #Create a database relationship that links an order to the products   
    products = db.relationship('Product', secondary='OrderProduct')
    
    def __init__(self, ordered_date, shipped_date, delivered_date, coupon_code):
        self.ordered_date = ordered_date
        self.shipped_date = shipped_date
        self.delivered_date = delivered_date
        self.coupon_code = coupon_code
    
    def __repr__(self):
        return f"Order('{self.id}', {self.ordered_date}, {self.shipped_date}, {self.delivered_date}, {self.coupon_code})"
    
    
#Create a products table model
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string(255), nullable=False, unique=True)
    price = db.Column(db.integer, nullable=False)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"Product('{self.id}, {self.name}, {self.price}')"
    
    
#Create an order_products table model
class OrderProduct(db.Model):
    __tablename__ = 'order_products'
    
    id = db.Column(db.integer, primary_key=True, nullable=False)
    
    #Create a database relationship that links an order to a product and vice-versa 
    order_id = db.Column(db.integer, db.ForeignKey('orders.id'), primary_key=True, nullable=False)
    product_id = db.Column(db.integer, db.ForeignKey('products.id'), primary_key=True, nullable=False)
    
    def __init__(self, order_id, product_id):
        self.order_id = order_id
        self.product_id = product_id
        
    def __repr__(self):
        return f"OrderProduct('{self.id}, {self.order_id}, {self.product_id}')"
    