from flask import request
from flask_restplus import Resource, fields, Namespace
from models.store import StoreModel
from schemas.store import StoreSchema
import http

STORE_NOT_FOUND = "Store not found."
STORE_ALREADY_EXISTS = "Store '{}' Already exists."

store_ns = Namespace('store', description='Store related operations')
stores_ns = Namespace('stores', description='Stores related operations')

store_schema = StoreSchema()
store_list_schema = StoreSchema(many=True)

# Model required by flask_restplus for expect
store = stores_ns.model('Store', {
    'name': fields.String('Name of the Store')
})


class Store(Resource):
    @staticmethod
    def get(_id):
        store_data = StoreModel.find_by_id(_id)
        if store_data:
            return store_schema.dump(store_data)
        return {'message': STORE_NOT_FOUND}, http.HTTPStatus.NOT_FOUND

    @staticmethod
    def delete(_id):
        store_data = StoreModel.find_by_id(_id)
        if store_data:
            store_data.delete_from_db()
            return {'message': "Store Deleted successfully"}, http.HTTPStatus.OK
        return {'message': STORE_NOT_FOUND}, http.HTTPStatus.NOT_FOUND


class StoreList(Resource):
    @stores_ns.doc('Get all the Stores')
    def get(self):
        return store_list_schema.dump(StoreModel.find_all()), http.HTTPStatus.OK

    @stores_ns.expect(store)
    @stores_ns.doc('Create a Store')
    def post(self):
        store_json = request.get_json()
        name = store_json['name']
        if StoreModel.find_by_name(name):
            return {'message': STORE_ALREADY_EXISTS.format(name)}, http.HTTPStatus.BAD_REQUEST

        store_data = store_schema.load(store_json)
        store_data.save_to_db()

        return store_schema.dump(store_data), http.HTTPStatus.CREATED
