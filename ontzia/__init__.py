# flask
from flask import Flask

app = Flask(__name__)

import ontzia.views

# flask_restful
from os.path import join

from flask_restful import Api

API_VERSION = 'v1'
api = Api(app, prefix=join('/', API_VERSION))

from ontzia.resources import Root

api.add_resource(Root, '/')
