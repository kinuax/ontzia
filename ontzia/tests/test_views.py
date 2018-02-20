from ontzia import app


def test_index():
    c = app.test_client()
    rv = c.get('/')
    assert rv.status_code == 200
    assert 'index' in str(rv.data).lower()
