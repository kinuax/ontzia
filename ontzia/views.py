from os import listdir
from os.path import isfile, join
from tempfile import NamedTemporaryFile

from flask import redirect, render_template, request, url_for

from ontzia import app
from ontzia.utils import get_events_from_ics


@app.route('/')
def index():
    return 'Showing index'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']

        if file.content_type != 'text/calendar':
            return render_template('upload.html', error='invalid file')

        tf = NamedTemporaryFile(delete=False, suffix='.ics')

        with open(tf.name, 'wb') as f:
            f.write(file.read())

        return redirect(url_for('search'))

    return render_template('upload.html')


@app.route('/search', methods=['GET'])
def search():
    ics_files = [join('/tmp/', f) for f in listdir('/tmp/') if isfile(join('/tmp/', f)) and f.endswith('.ics')]
    events = []

    for f in ics_files:
        events.extend(get_events_from_ics(f))

    return render_template('search.html', events=events)
