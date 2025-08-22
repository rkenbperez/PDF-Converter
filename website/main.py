from flask import Flask
from os import path


import tempfile
from pathlib import Path

from flask import Flask, request, render_template, send_from_directory

import pdfy
from config import EXPORTS_DIR, UPLOADS_DIR

app = Flask(__name__)


# Home Route
@app.route('/')
def home():
    return render_template('home.html.j2')


@app.route('/convert', methods = ['POST'])
def convert_to_pdf():

    with tempfile.TemporaryDirectory(dir=UPLOADS_DIR) as temp_dir_name:
        temp_dir = Path(temp_dir_name)

        files = request.files.getlist("files")
        for file in files:
            file.save(temp_dir / file.filename)

        output_pdf = pdfy.pdf(temp_dir)

        if output_pdf.exists():
            return render_template("output.html.j2", output_pdf = output_pdf.name)

    return '<html><body><h1>Sorry we are down. Please Contact Us.</h1></body></html>'


@app.route('/download/<path:pdf_name>')
def download_pdf(pdf_name):
    """Route for sharing generated files to users"""

    return send_from_directory(
        EXPORTS_DIR,
        pdf_name,
        mimetype='application/pdf',
        download_name='export.pdf',
        as_attachment=True
    )


def create_app():
    app = Flask(__name__)


    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app

if __name__ == '__main__':
    app.run(debug=True)