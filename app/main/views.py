from flask import(
    Flask,render_template,make_response
)
from app.models import(
    Customer, Product, Order, db
)
from datetime import datetime, timedelta

from . import auth

@auth.route('/')
def homepage():
    title = 'E-commerce Store Project 2023'
    
    # How many customers?
    def count_all_customers():
        print("How many customers?")
        
        total_customers = Customer.query.count()
        print(total_customers)
        
        return count_all_customers(total_customers)        
    
    
    # Get all customer orders by customer_id
    def get_customer_orders(customer_id = 1):
        customer_orders = Order.query.filter_by(customer_id = customer_id).all()
        print(customer_orders)
        
        for order in customer_orders:
            print(order.id, order.order_id, order.customer.first_name)
        
        return get_customer_orders(customer_orders)
    
    
    # Get all pending orders
    def get_pending_orders(): 
        pending_orders = Order.query.filter(Order.shipped_date.is_(None)).order_by(Order.ordered_date.desc()).all()
        print(pending_orders)
        
        for order in pending_orders:
            print(order.id, order.ordered_date)
        
        return get_pending_orders(pending_orders)
    
    
    # Get all orders with a coupon code except FLASH50
    def orders_with_coupon_code():
        coupon_codes = Order.query.filter(Order.coupon_code.isnot(None)).filter(Order.coupon_code != 'FLASH50').all()
        print(coupon_codes)
        
        for order in coupon_codes:
            print(order.id, order.coupon_code, order.ordered_date)
            
        return orders_with_coupon_code()
    
    
    # Get revenue in last X days
    def get_revenue(x_days = 30):
        order_product = order_product
        total_revenue = db.session.query(db.func.sum(Product.price)).join(order_product).join(Order).filter(Order.ordered_date > (datetime.now())- timedelta(days=x_days)).scalar()
        print(total_revenue)
        
        return get_revenue(total_revenue)
    
    
    # Get average fulfilment time
    def get_average_time():
        fulfilment_time = db.session.query(db.func.time(db.func.avg(db.func.strftime('%s', Order.shipped_date) - db.fuc.strftime('%s', Order.ordered_date)), 'uniexpoch')).filter(Order.shipped_date.isnot(None)).scalar()
        print(fulfilment_time)
        
        return get_average_time(fulfilment_time)
    
    
    # Get customers who have spent X amount of dollars 
    
        
    template = render_template('pages/index.html', title=title)
    response = make_response(template)
    
    return response
