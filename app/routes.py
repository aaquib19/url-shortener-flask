from flask import Blueprint, render_template, request
from . import db
from .models import URL

# Create a Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the URL from the form
        url_to_shorten = request.form['url']
        
        # For now, let's just show it back. We'll add the real logic next.
        return f"You submitted: {url_to_shorten}"

    # If it's a GET request, just show the form
    return render_template('index.html')