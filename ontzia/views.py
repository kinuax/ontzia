from flask import render_template, request

from ontzia import app


@app.route('/')
def index():
    return 'Showing index'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']

        if file.content_type != 'text/calendar':
            return render_template('upload.html', error='invalid file')

    return render_template('upload.html')
