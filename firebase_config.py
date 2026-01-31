import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

# Initialize Firebase
cred_path = 'serviceAccountKey.json'
db = None

def initialize_firebase():
    global db
    if not firebase_admin._apps:
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            db = firestore.client()
            print("Firebase initialized successfully.")
        else:
            print(f"Warning: {cred_path} not found. Firebase functionality will not work until it is added.")
            db = None
    else:
        # Already initialized, just get the client if not set (though usually handled)
        try:
            db = firestore.client()
        except ValueError:
            db = None

# Run initialization immediately on import or explicitly
initialize_firebase()
