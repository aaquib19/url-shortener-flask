from flask import Blueprint, render_template, request, redirect
from . import db
from .models import URL

from .util import generate_short_code

# Create a Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the URL from the form
        url_to_shorten = request.form['url']

        existing_url = URL.query.filter_by(original_url=url_to_shorten).first()
        if existing_url:
            short_url = request.host_url + existing_url.short_url
        else : 
            short_url = generate_short_code()
            # For now, let's just show it back. We'll add the real logic next.
            new_url = URL(original_url=url_to_shorten, short_url=short_url)
            db.session.add(new_url)
            db.session.commit()
            short_url = request.host_url + existing_url.short_url

        return f"You submitted: {url_to_shorten}. Shortened URL is: {short_url}"

    # If it's a GET request, just show the form
    return render_template('index.html')


@main_bp.route('/debug-db')
def debug_db():
    # Query all entries from the URL table
    all_urls = URL.query.all()
    
    # Create a string to display the results
    output = "<h1>Database Contents</h1>"
    for url_entry in all_urls:
        output += f"<p>ID: {url_entry.id}, Short: {url_entry.short_url}, Long: {url_entry.original_url}</p>"
        
    return output


@main_bp.route('/clear-db')
def clear_db():
    try:
        num_rows_deleted = db.session.query(URL).delete()
        db.session.commit()
        return f"Cleared the database. {num_rows_deleted} entries deleted."
    except Exception as e:
        db.session.rollback()
        return f"An error occurred: {str(e)}"

@main_bp.route('/<short_code>')
def redirect_to_url(short_code):
    # 1. Look up the short_code in the database
    url_entry = URL.query.filter_by(short_url=short_code).first()

    # 2. If found, redirect to the original long URL
    if url_entry:
        return redirect(url_entry.original_url)
    
    # 3. If not found, show a 404 Not Found error
    else:
        return "URL not found", 404