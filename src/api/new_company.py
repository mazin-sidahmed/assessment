import os
from flask import Blueprint, request, jsonify
from src.modules.new_company_item import NewCompanyItem
from src.definitions import root


new_company = Blueprint('new_company', __name__)
dbfile = os.path.join(root, 'db/new_company.csv')


@new_company.route('/new_company/item', methods=['POST', 'GET', 'DELETE'])
def handle():
    item = NewCompanyItem(dbfile)
    if request.method == 'POST':
        data = request.get_json(force = True)
        id = data['id']
        name = data['name']
        price = data['price']
        brand = data['brand']
        item.save(id, name, price, brand)
        return ('OK', 201)
    elif request.method == 'GET':
        name = request.args.get('name')
        return (jsonify(item.search(name)), 200)
    elif request.method == 'DELETE':
        data = request.get_json(force = True)
        id = data['id']
        item.delete(id)
        return ('OK', 204)
