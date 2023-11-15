from flask_app import db

class Stocks(db.Model):
    __tablename__ = "stocks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(8), nullable=False)
    amount = db.Column(db.Integer, nullable=False)