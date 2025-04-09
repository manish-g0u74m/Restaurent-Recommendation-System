from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db 


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))  # Store hashed password
    preferred_cuisines = db.Column(db.String(100))
    budget_preference=db.Column(db.String(10))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))          # General area/neighborhood
    locality = db.Column(db.String(100))          # Specific locality (e.g., "Bandra West")
    city = db.Column(db.String(50), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float)                  # e.g., 4.2
    votes = db.Column(db.Integer)                 # e.g., 1,200 votes
    cost = db.Column(db.Integer)                  # e.g., 500 (average cost for two)

    # Optional: Add a method to convert cost to price range ($$$)
    def price_range(self):
        if self.cost < 300:
            return "$"
        elif 300 <= self.cost < 700:
            return "$$"
        else:
            return "$$$"
        
class SuggestedRestaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    locality = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text)
    user_email = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Suggestion {self.name} ({self.date_submitted})>"