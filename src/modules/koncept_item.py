from src.database import db


class KonceptItem(db.Model):

    __tablename__ = 'koncept'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float())

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
            }