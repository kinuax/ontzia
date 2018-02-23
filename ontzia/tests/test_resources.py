from flask import json

from ontzia import api, app
from ontzia.resources import Root


def test_root_supported_methods():
    c = app.test_client()

    for method in ('get', 'head'):
        with app.test_request_context():
            root_url = api.url_for(Root)

        rv = getattr(c, method)(root_url)
        assert rv.status_code == 200
        assert rv.content_type == 'application/json'
        assert rv.content_length == 3

        if method == 'get':
            assert json.loads(rv.get_data()) == {}


def test_root_unsupported_methods():
    c = app.test_client()

    for method in ('post', 'put', 'delete'):
        with app.test_request_context():
            root_url = api.url_for(Root)

        rv = getattr(c, method)(root_url)
        assert rv.status_code == 405
