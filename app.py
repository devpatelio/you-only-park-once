from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from jinja2 import escape
from markupsafe import escape

import os
app = Flask(__name__)

UPLOAD = '/projects/07cb54a4-9729-4508-ad4f-95fc7891551c/Team Members/Dev Patel/deploy_template/'
app.config['UPLOAD_FOLDER'] = 'user_inputs/'

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/uploads', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template('prediction_results.html', user_img_name='user_img.jpg')

if __name__ == '__main__':
    app.run()

