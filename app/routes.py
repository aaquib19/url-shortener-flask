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


@main_bp.route('/debug-db')
def debug_db():
    # Query all entries from the URL table
    all_urls = URL.query.all()
    
    # Create a string to display the results
    output = "<h1>Database Contents</h1>"
    for url_entry in all_urls:
        output += f"<p>ID: {url_entry.id}, Short: {url_entry.short_code}, Long: {url_entry.long_url}</p>"
        
    return output