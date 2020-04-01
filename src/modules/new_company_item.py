from src.database import db


class NewCompanyItem(db.Model):

    __tablename__ = 'new_company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float())
    brand = db.Colum(db.String())

    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'price': self.price,
            'brand': self.brand
            }
    
    