from flask_restful import Api, Resource

from ontzia import app

API_ROOT = '/v1/'
api = Api(app, prefix=API_ROOT)


class Root(Resource):
    def get(self):
        return {}


api.add_resource(Root, '/')
