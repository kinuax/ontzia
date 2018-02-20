from ontzia import app


@app.route('/')
def index():
    return 'Showing index'
