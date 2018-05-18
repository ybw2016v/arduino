from flask import Flask
from flask import abort, redirect, url_for
from ardlib import *
import numpy as np
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/fweb')
def fweb():
    s=ard()
    
    s.qfm()
    # abort(401)
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)