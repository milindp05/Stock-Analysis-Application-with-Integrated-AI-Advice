from firebase_config import db

#all data collection methods for each user 

def get_user_watchlist(username):
    doc = db.collection("users").document(username).get()
    if doc.exists:
        return doc.to_dict().get("watchlist", [])
    return []

def save_user_watchlist(username, watchlist):
    db.collection("users").document(username).update({"watchlist": watchlist})
