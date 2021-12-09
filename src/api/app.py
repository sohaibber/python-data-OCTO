from src.api.db import db

class Transaction(db.Model):

    id = db.Column('transaction_id', db.Integer, primary_key = True)
    v0 = db.Column(db.String(100))
    v1 = db.Column(db.String(100))
    v2 = db.Column(db.String(100))
    v3 = db.Column(db.String(100))
    prediction = db.Column(db.String(100))


    def __init__(self, features, prediction):
        self.v0 = features[11]
        self.v1 = features[15]
        self.v2 = features[28]
        self.v3 = features[13]
        self.prediction=prediction


    def __repr__(self):
        return '<Transaction %r>' % self.prediction

db.create_all()
db.session.commit()