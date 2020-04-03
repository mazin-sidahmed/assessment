import os
from flask import Blueprint, request, jsonify
from src.modules.koncept_item import KonceptItem
from src.definitions import root
from src.db import utils


koncept = Blueprint('koncept', __name__)


@koncept.route('/koncept/item', methods=['POST'])
def create():
    data = request.get_json(force = True)
    name = data['name']
    price = data['price']     
    item = KonceptItem(name = name, price = price)
    utils.save(item)
    return ('OK', 201)


@koncept.route('/koncept/item', methods=['GET'])
def search(): 
    name = request.args.get('name')
    items = utils.search(KonceptItem, name)
    return jsonify([e.serialize() for e in items])


@koncept.route('/koncept/item', methods=['DELETE'])
def delete():
    data = request.get_json(force = True)
    name = data['name']
    utils.delete(KonceptItem, name)
    return ('OK', 204)
