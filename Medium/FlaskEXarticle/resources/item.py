from flask import request
from flask_restplus import Resource, fields, Namespace
from models.item import ItemModel
from schemas.item import ItemSchema
import http

ITEM_NOT_FOUND = "Item not found"

item_ns = Namespace('item', description='Item related operations')
items_ns = Namespace('items', description='Items related operations')

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

# Model required by flask_restplus for expect
item = items_ns.model('Item', {
    'name': fields.String('Name of the Item'),
    'price': fields.Float(0.00),
    'store_id': fields.Integer
})


class Item(Resource):

    @staticmethod
    def get(_id):
        item_data = ItemModel.find_by_id(_id)
        if item_data:
            return item_schema.dump(item_data)
        return {'message': ITEM_NOT_FOUND}, http.HTTPStatus.NOT_FOUND

    @staticmethod
    def delete(_id):
        item_data = ItemModel.find_by_id(_id)
        if item_data:
            item_data.delete_from_db()
            return {'message': "Item Delete successfully"}, http.HTTPStatus.NO_CONTENT
        return {'message': ITEM_NOT_FOUND}, http.HTTPStatus.NOT_FOUND

    @item_ns.expect(item)
    def put(self, _id):
        item_data = ItemModel.find_by_id(_id)
        item_json = request.get_json()

        if item_data:
            item_data.price = item_json['price']
            item_data.name = item_json['name']
        else:
            item_data = item_schema.load(item_json)

        item_data.save_to_db()
        return item_schema.dump(item_data), http.HTTPStatus.OK


class ItemList(Resource):
    @items_ns.doc('Get all the Items')
    def get(self):
        return item_list_schema.dump(ItemModel.find_all()), http.HTTPStatus.OK

    @item_ns.expect(item)
    @item_ns.doc('Create an Item')
    def post(self):
        item_json = request.get_json()
        item_data = item_schema.load(item_json)
        item_data.save_to_db()

        return item_schema.dump(item_data), http.HTTPStatus.CREATED
