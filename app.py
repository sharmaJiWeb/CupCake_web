from flask import Flask, render_template
from contact import contact_bp
from auth import auth_bp
from admin import admin_bp
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # Required for session/flashing

app.register_blueprint(contact_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/flavors')
def flavors():
    return render_template('flavors.html')

# Contact route is handled by contact_bp

@app.route('/cart')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
