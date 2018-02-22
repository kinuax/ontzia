from flask import json

from ontzia import app
from ontzia.resources import API_ROOT


def test_root_supported_methods():
    c = app.test_client()

    for method in ('get', 'head'):
        rv = getattr(c, method)(API_ROOT)
        assert rv.status_code == 200
        assert rv.content_type == 'application/json'
        assert rv.content_length == 3

        if method == 'get':
            assert json.loads(rv.get_data()) == {}


def test_root_unsupported_methods():
    c = app.test_client()

    for method in ('post', 'put', 'delete'):
        rv = getattr(c, method)(API_ROOT)
        assert rv.status_code == 405
