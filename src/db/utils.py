from src.extentions import db


def save(item):
    db.session.add(item)
    db.session.commit()


def search(item_cls, name):
    return item_cls.query.filter_by(name = name).all()


def delete(item_cls, name):
    item_cls.query.filter_by(name = name).delete()
    db.session.commit()