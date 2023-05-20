from flask import(
    Flask,render_template,make_response
)
from app.models import(
    Customer, Product, Order, db
)

from . import auth

@auth.route('/')
def homepage():
    title = 'E-commerce Store Project 2023'
    
    # Count all customers
    total_customers = Customer.query.count()
    
    # Get all customer info
    customers = Customer.query.all()
    
    # Get customer orders by customer_id
    customer_id = 1
    customer_orders = Order.query.filter_by(customer_id = customer_id).all()
    
    # Get all pending orders
    pending_orders = Order.query.filter_by(customer_id = customer_id).filter(Order.shipped_date.is_(None)).order_by(Order.ordered_date.desc()).all()
        
        
    template = render_template('pages/index.html', title=title, customers = customers, total_customers = total_customers, customer_orders = customer_orders, order = pending_orders)
    response = make_response(template)
    
    return response
