from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import json
import requests
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class tvs(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/8', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content)
        
class tablets(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/7', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content)

class refrigeratorsfreezers(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/6', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content) 

class mobiles(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/5', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content) 

class microwaveovens(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/4', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content) 

class laptops(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/3', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content) 

class desktops(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/2', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content) 

class airconditioners(Resource):
    def get(self):
        r = requests.get('https://storage.scrapinghub.com/items/205634/1', auth=('3463c7e3c61346718c5b79605832e30e', ''))
        return jsonify(r.content) 


api.add_resource(tvs, '/tvs') # Route_1
api.add_resource(tablets, '/tablets')
api.add_resource(refrigeratorsfreezers, '/refrigeratorsfreezers')
api.add_resource(mobiles, '/mobiles')
api.add_resource(microwaveovens, '/microwaveovens')
api.add_resource(laptops, '/laptops')
api.add_resource(desktops, '/desktops')
api.add_resource(airconditioners, '/airconditioners')



if __name__ == '__main__':
     app.run(port='9994')