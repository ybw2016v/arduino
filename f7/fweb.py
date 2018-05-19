import numpy as np
from flask import (Flask, abort, flash, redirect, render_template, request,
                   url_for)

from ardlib import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return render_template('test.html')

@app.route('/fweb',methods=['GET', 'POST'])
def fweb():


    if request.method == 'POST':
        flash('dog')
    # s=ard()
    
    # s.qfm()
    # abort(401)
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
