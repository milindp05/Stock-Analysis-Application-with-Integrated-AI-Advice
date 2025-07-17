import firebase_admin
from firebase_admin import credentials, firestore

# Load the service account key
cred = credentials.Certificate("stock-analysis-project-27dd9-firebase-adminsdk-fbsvc-39f43268db.json")  
firebase_admin.initialize_app(cred)

# Get Firestore DB
db = firestore.client()
