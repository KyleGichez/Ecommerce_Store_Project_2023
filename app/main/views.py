from flask import(
    Flask,render_template,make_response
)
from . import auth

@auth.route('/')
def homepage():
    title = 'E-commerce Store Project 2023'
    template = render_template('pages/index.html', title=title)
    response = make_response(template)
    
    return response