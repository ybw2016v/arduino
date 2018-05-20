import numpy as np
from flask import (Flask, abort, flash, redirect, render_template, request,
                   url_for)
import datetime

from ardlib import *
from testlib import *
import json
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    a=[]
    a.append(nowTime)
    a.append("you are a dog")
    return render_template('test.html',time=a)

@app.route('/fweb',methods=['GET', 'POST'])
def fweb():
    if request.method == 'POST':
        s.tes1()
    else:
        abort(403)
            
    # s=ard()
    
    # s.qfm()
    # abort(401)
    return "dog"

@app.route('/test1',methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        print("666")
        s.tes1()
        return redirect(url_for('hello_world'))
    else:
        abort(403)

@app.route('/test2',methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        s.tes2()
    else:
        abort(403)
    pass

    
@app.route('/real1',methods=['GET','POST'])
def real1():
    if request.method == 'POST':
        a=ss.qfm()
        return redirect(url_for('hello_world'))
    else:
        abort(403)

@app.route('/real2',methods=['GET','POST'])
def real2():
    if request.method == 'POST':
        a=ss.saomiao()
        return redirect(url_for('hello_world'))
    else:
        abort(403)

@app.route('/res1')
def res1():
    a=os.listdir('./static/res1/')
    return render_template('result.html',urls=a)

@app.route('/res2')
def res2():
    a=os.listdir('./static/res2/')
    return render_template('result2.html',urls=a)

if __name__ == '__main__':
    s=testlib()
    ss=ard()
    app.run(debug=True,host='0.0.0.0')
