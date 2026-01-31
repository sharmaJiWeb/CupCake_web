import firebase_admin
# Removed direct credentials/firestore import as we use firebase_config
from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from firebase_config import db # Import centralized db instance

contact_bp = Blueprint('contact', __name__)

# Firebase init removed from here - handled in firebase_config.py

def send_auto_reply(to_email, user_name):
    # Email Configuration
    # REPLACE WITH YOUR ACTUAL EMAIL CREDENTIALS OR USE ENVIRONMENT VARIABLES
    sender_email = os.environ.get('MAIL_USERNAME', 'your_email@gmail.com')
    sender_password = os.environ.get('MAIL_PASSWORD', 'your_app_password')
    smtp_server = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('MAIL_PORT', 587))
    
    if sender_email == 'your_email@gmail.com':
        print("SMTP Config: Please update email credentials in contact.py or set environment variables to send emails.")
        return

    subject = "Thank you for contacting CupcakeWin! 🧁"
    body = f"""
    Hi {user_name},

    Thank you for reaching out to us at CupcakeWin! 
    
    We have received your message and one of our sweet team members will get back to you shortly.
    
    In the meantime, feel free to browse our latest flavors on our website.

    Stay Sweet,
    The CupcakeWin Team
    www.cupcakewin.com
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, to_email, text)
        server.quit()
        print(f"Auto-reply sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('Please fill out all fields.', 'error')
            return redirect(url_for('contact.contact'))
            
        # Logic to send email (Best effort, doesn't block UI if fails)
        send_auto_reply(email, name)

        if db:
            try:
                doc_ref = db.collection('contacts').document()
                doc_ref.set({
                    'name': name,
                    'email': email,
                    'message': message,
                    'timestamp': datetime.utcnow()
                })
                flash('Message sent successfully! Check your inbox for a confirmation.', 'success')
            except Exception as e:
                print(f"Error saving to Firebase: {e}")
                flash('An error occurred while saving your message, but we are looking into it.', 'error')
        else:
             # Fallback for when DB isn't set up yet
            print(f"Mock Save: Name={name}, Email={email}, Msg={message}")
            flash('Message received (Demo mode)! Check console for email attempt.', 'info')
            
        return redirect(url_for('contact.contact'))
        
    return render_template('contact.html')
