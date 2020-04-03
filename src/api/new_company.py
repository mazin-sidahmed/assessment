import os
from flask import Blueprint, request, jsonify
from src.modules.new_company_item import NewCompanyItem
from src.definitions import root
from src.db import utils 


new_company = Blueprint('new_company', __name__)


@new_company.route('/new_company/item', methods=['POST'])
def create():
    data = request.get_json(force = True)
    name = data['name']
    price = data['price']
    brand = data['brand']
    item = NewCompanyItem(name = name, price = price, brand = brand)
    utils.save(item)
    return ('OK', 201)


@new_company.route('/new_company/item', methods=['GET'])
def search():
    name = request.args.get('name')
    items = utils.search(NewCompanyItem, name)
    return jsonify([e.serialize() for e in items])

  
@new_company.route('/new_company/item', methods=['DELETE'])
def delete():
    data = request.get_json(force = True)
    name = data['name']
    utils.delete(NewCompanyItem, name)
    return ('OK', 204)