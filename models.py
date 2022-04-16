# import email
from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    age=db.Column(db.Integer,nullable=False)
    email=db.Column(db.String(100),nullable=False)
    dr=db.Column(db.String(100), nullable=False)
    filepath=db.Column(db.String(200),nullable=False)
    report=db.Column(db.String(200),nullable=False)
    date=db.Column(db.Date,nullable=False)

    def __repr__(self):
        return f'{self.name} on {self.date}'