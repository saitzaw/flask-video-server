"""Routes for main flask application."""
from flask import Blueprint, render_template 
from flask import current_app as app 

from . import views 

main = Blueprint('main', __name__, 
                            template_folder='templates',
                            static_folder='static')

@main.route('/')
def home_page(): 
    """Loading the Home page"""
    return render_template('index.html')