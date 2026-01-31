from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from functools import wraps
import os
from firebase_config import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Configuration for Admin
# In production, use environment variables or a database flag
ADMIN_EMAILS = ['admin@cupcakewin.com'] 

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 1. Check if logged in
        if 'user_id' not in session:
            flash('Please login to access the admin area.', 'error')
            return redirect(url_for('auth.login', next=request.url))
        
        # 2. Check if user is admin
        user_email = session.get('email')
        if user_email not in ADMIN_EMAILS:
            flash('Access denied. You do not have admin privileges.', 'error')
            return redirect(url_for('index'))
            
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/')
@admin_required
def dashboard():
    # Fetch recent messages/contacts if DB is connected
    contacts = []
    if db:
        try:
            # Fetch last 20 messages, ordered by timestamp desc
            docs = db.collection('contacts').order_by('timestamp', direction='DESCENDING').limit(20).stream()
            for doc in docs:
                data = doc.to_dict()
                # Handle Firestore Timestamp conversion safely
                ts = data.get('timestamp')
                if ts:
                    if hasattr(ts, 'to_datetime'):
                        data['timestamp'] = ts.to_datetime()
                contacts.append(data)
        except Exception as e:
            print(f"Error fetching contacts: {e}")
            flash('Could not load data from database.', 'error')
    
    return render_template('admin.html', contacts=contacts)
