import urllib.request
from main import *

from flask import Flask, url_for, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/newPic', methods=['GET', 'POST'])
def newPic():
    if request.method == 'POST':
        data = request.form['dataUri']
        response = urllib.request.urlopen(data)
        with open('newFace/newPic.jpg', 'wb') as f:
            f.write(response.file.read())

        _, identity = who_is_it('newFace/newPic.jpg', database, FRmodel)
        return str(identity)
    else:
        return "no GET method in this route"
