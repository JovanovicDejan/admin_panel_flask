import os
from flask import Flask, flash, redirect, request
from werkzeug.utils import secure_filename
import time



UPLOAD_FOLDER = 'static/images'


app = Flask(__name__, static_url_path="/static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_file():
    file = request.files['photoUrl']

    if not file:
        return "File is not valide! "
    
    ALLOWED_EXTENSIONS = {'png','jpg','jpeg','gif'}
    msec = int(round(time.time() * 1000))
    ext = file.filename.split('.')[-1]
    if file and ext in ALLOWED_EXTENSIONS:
        filename = secure_filename(file.filename)
        photo_name = file.filename.split('.')[0]
        photo_name += str(msec)
        photo_name += '.'
        photo_name += ext
        filename = photo_name
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return '/images/' + filename
