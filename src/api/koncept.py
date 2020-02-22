import os
from flask import Blueprint, request, jsonify
from src.modules.item import Item
from src.definitions import root


koncept = Blueprint('koncept', __name__)
dbfile = os.path.join(root, 'db/koncept.csv')


@koncept.route('/koncept/item', methods=['POST', 'GET', 'DELETE'])
def handle():
    item = Item(dbfile)
    if request.method == 'POST':
        data = request.get_json()
        id = data['id']
        name = data['name']
        price = data['price']
        item.save(id, name, price)
        return ('OK', 201)
    elif request.method == 'GET':
        name = request.args.get('name')
        return (jsonify(item.search(name)), 200)
    elif request.method == 'DELETE':
        data = request.get_json()
        name = data['name']
        item.delete(name)
        return ('OK', 204)
