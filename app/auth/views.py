from flask import render_template
from . import auth

@auth.route('/login')
def login():
    retun render_template('auth/login.html')