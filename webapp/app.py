from pypdf import PdfMerger
# Convert bad filename into secure filename
from werkzeug.utils import secure_filename
import os
import flask

app = flask.Flask(__name__)
# Max file size of 10 MB
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'uploads'

def merge_pdf():
    merger = PdfMerger()
    file_directory = app.config['UPLOAD_PATH']

    files = [f for f in os.listdir(file_directory) if f.endswith('.pdf')]

    for pdf in files:
        merger.append(pdf)
    with open(os.path.join(file_directory, 'Test.pdf'), 'wb') as append:
        merger.write(append)

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        files = os.listdir(app.config['UPLOAD_PATH'])
        return flask.render_template('upload.html', upfiles=files)
    elif flask.request.method == 'POST':
        uploaded_file = flask.request.files.get('file')
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            # Get file extension ['abc', '.png']
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                flask.abort(400)
            path = os.path.join(app.config['UPLOAD_PATH'], filename)
            uploaded_file.save(path)
        elif flask.request.form.get('file') == 'Merge PDF':
            merge_pdf()
        return flask.redirect(flask.url_for('index'))

@app.route('/uploads/<filename>')
def upload(filename):
    return flask.send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.errorhandler(413)
def too_large(e):
    return 'File is too large for use', 413

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True, use_reloader=False)
