import hashlib
from firebase_config import db

#all authentication methods for login and registration

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    doc_ref = db.collection("users").document(username)
    if doc_ref.get().exists:
        return False  
    hashed = hash_password(password)
    doc_ref.set({
        "password": hashed,
        "watchlist": []  # initialize empty watchlist for new user
    })
    return True

def verify_user(username, password):
    doc = db.collection("users").document(username).get()
    if doc.exists:
        stored_hash = doc.to_dict().get("password")
        return hash_password(password) == stored_hash
    return False
