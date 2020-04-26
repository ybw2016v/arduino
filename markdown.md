# 项目源代码

## arduino部分

### f7.h
``` C
#include <Servo.h>
struct pw
{
    int x;
    int y;
    float l;
    struct pw * next;
};

struct pw * h = NULL;
int a0;
int a1;
int b0;
int b1;
Servo s0;
Servo s1;
char com;
```

### f7.ino

``` C
#include "f7.h"
void readlight();
void findmaxq();
void saomiao();
void sf();
void showlight();
void setup()
{
    // 初始化舵机和串口
    s0.attach(7);
    s1.attach(8);
    Serial.begin(9600);
}
void loop()
{
    if (Serial.available())
    {
        com=Serial.read();

        switch (com)
        {
            case 's':
                saomiao();
                break;
            case 'f':
                findmaxq();
                break;
            case 'q':
                sf();
                break;
            case 'l':
                showlight();
                break;
            default:
                Serial.println("bad com");
                break;
        }
    }
}
void readlight()
{
    // 光强获取函数。
    a0=analogRead(A0)-5;
    a1=analogRead(A1)+5;
    b0=analogRead(A2)-5;
    b1=analogRead(A3)+5;
}
void saomiao()
{
    // 光强扫描函数
    float l;
    int i,j;

    for( i = 0; i < 180; i++)
    {

        for( j = 0; j < 180; j++)
        {
            delay(10);
            s0.write(i);
            delay(10);
            s1.write(j);
            delay(5);
            readlight();
            l=(a0+a1+b0+b1);
            Serial.print(l,2);
            Serial.print(',');
        }
        Serial.print('\n');
        delay(10);
    }


}

void findmaxq()
{
    // 空间光强极值获取函数。
    int flog1=0;
    int flog2=0;
    int i=90;
    int j=90;
    s0.write(i);
    s1.write(j);
    for(int ip = 0; ip <= 4096; ip++)
    {
        readlight();
        delay(2);

        if (a0>(a1+3))
        {
            // i++;
            if (i<=179)
            {
                i++;
            }
            else
            {
                flog1=1;
            }
        }
        if (a0<(a1-3))
        {
            // i--;
            if (i>=1)
            {
                i--;
                Serial.print("*");
            }
            else
            {
                flog1=1;
            }
        }
        if ((a0<=(a1+3))&&(a0>=(a1-3)))
        {
            flog1=1;
        }
        Serial.print(i);
        Serial.print(',');
        Serial.print(flog1);
        Serial.print(',');
        s0.write(i);
        if (b0>(b1+3))
        {
            // j++;
            if (j<=179)
            {
                j++;
            }
            else
            {
                flog2=1;
            }
        }
        if (b0<=(b1-3))
        {
            // i--;
            if (j>=1)
            {
                j--;
            }
            else
            {
                flog2=1;
            }
        }
        if (b0<=(b1+3)&&b0>=(b1-3))
        {
            flog2=1;
        }
        Serial.print(flog2);
        Serial.print(',');
        Serial.println(j);
        s1.write(j);
        if (flog1==1&&flog2==1)
        {
            Serial.println('p');
            Serial.print(i);
            Serial.print(',');
            Serial.print(j);
            break;
        }
    }
}
void sf()
{
    // 光强极大值扫描函数
    float l,ml;
    int i,j;
    int mx,my;
    ml=100000;
    mx=0;
    my=0;
    for( i = 0; i <= 180; i=i+10)
    {

        for( j = 0; j < 180; j=j+10)
        {
            delay(10);
            s0.write(i);
            delay(10);
            s1.write(j);
            delay(100);
            readlight();
            l=(a0+a1+b0+b1);
            // Serial.print(l,2);
            // Serial.print(',');
            if (ml>=l)
            {
                ml=l;
                mx=i;
                my=j;
            }
        }
        // Serial.print('\n');
        delay(10);
    }
    delay(1000);
    s0.write(mx);
    s1.write(my);
    delay(20);
    Serial.println('p');


}
void showlight()
{
    float l;
    readlight();
    delay(10);
    l=a0+a1+b0+b1;
    Serial.println(l);
    delay(2);
}

```

## 树莓派部分

### ardlib.py

单片机操纵模块

``` python
#!/usr/bin/env python3
import serial
import numpy as np
import os
import time
import datetime
import shutil
import matplotlib
matplotlib.use("Pdf")
import matplotlib.pyplot as plt

class ard(object):
#面向对象的编程语言
    def __init__(self):#初始化函数
        self.ser=serial.Serial('/dev/ttyUSB0', 9600)
        time.sleep(1)
        sser=self.ser
        try:
            sser.open()
        except:
            pass
    def saomiao(self):#扫描函数
        nmp=np.zeros([180,180])
        self.nowTime=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        sser=self.ser
        sser.write('s'.encode())
        sser.flushInput()
        for i in range(0,180):
            time.sleep(1)
            shi = str(sser.readline())
            shi=shi[2:len(shi)-5]
            shi=shi.strip()
            shi=shi.split(',')
            nmp[i,:]=np.array(shi)
            pass
        p=os.path.abspath('.')
        ba=os.popen('mkdir '+p+'/static/res2/'+self.nowTime)
        time.sleep(0.001)
        plt.figure(dpi=500)
        plt.imshow(nmp)
        plt.title('space')
        plt.colorbar()
        plt.savefig('data.jpg')
        b=os.popen('cp data.jpg '+p+'/static/res2/'+self.nowTime)
        shutil.copyfile('./static/res2.html','./static/res2/'+self.nowTime+r'/res.html')


    def qfm(self):#光强最大值寻找函数
        self.nowTime=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        sser=self.ser
        time.sleep(1)
        sser.write(b'q')
        self.takephoto()
        p=os.path.abspath('.')
        print(p)
        p2=os.path.join(p,'/static/res1/'+self.nowTime+r'/res1.html')

        b=os.popen('mkdir '+p+'/static/res1/'+self.nowTime)
        time.sleep(0.001)
        a=os.popen('touch '+p+p2)
        print(b)
        print(a)
        print(p+p2)
        with open(p+p2,'w') as f:
            f.write('dog\n'+self.nowTime)
            shutil.copyfile('./static/res1.html','./static/res1/'+self.nowTime+r'/res.html')
    def takephoto(self):#拍照函数
        timedog=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        str = os.popen("echo takephoto"+timedog).read()
        print(str)
        pass
    def test(self):
        print("OK")
        pass

    pass

```

### testlib.py

测试模块

``` python
mport time
import datetime
import os
import shutil

class testlib(object):
    def __init__(self):
        self.nowTime=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        pass
    def tes1(self):
        self.nowTime=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        print("开始执行全域扫描")
        p=os.path.abspath('.')
        print(p)
        p2=os.path.join(p,'/static/res1/'+self.nowTime+r'/res1.html')
        # os.mkdir(os.path.join(p,'/static/res1/'+self.nowTime))
        b=os.popen('mkdir '+p+'/static/res1/'+self.nowTime)
        time.sleep(0.001)
        a=os.popen('touch '+p+p2)
        print(b)
        print(a)
        print(p+p2)
        with open(p+p2,'w') as f:
            f.write('dog\n'+self.nowTime)
            shutil.copyfile('./static/res1.html','./static/res1/'+self.nowTime+r'/res.html')

    def tes2(self):
        print("开始寻找光污染源")
        pass
    def test3(self):
        return self.nowTime
    pass

```

### fweb.py

互联网模块

``` python

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

@app.route('/test1/',methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        print("666")
        s.tes1()
        return redirect(url_for('hello_world'))
    else:
        abort(403)

@app.route('/test2/',methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        s.tes2()
    else:
        abort(403)
    pass


@app.route('/real1',methods=['GET','POST'])
def real1():
    if request.method == 'POST':
        ss=ard()
        a=ss.qfm()
        return redirect(url_for('hello_world'))
    else:
        abort(403)

@app.route('/real2',methods=['GET','POST'])
def real2():
    if request.method == 'POST':
        ss=ard()
        time.sleep(1)
        a=ss.saomiao()
        return redirect(url_for('hello_world'))
    else:
        abort(403)

@app.route('/res1')
def res1():
    a=os.listdir('./static/res1/')
    bu=sorted(a,reverse = True)
    return render_template('result.html',urls=bu)

@app.route('/res2')
def res2():
    a=os.listdir('./static/res2/')
    bu=sorted(a,reverse = True)
    return render_template('result2.html',urls=bu)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
```

## HTML部分

### result.html

结果显示模块

``` html
<!DOCTYPE html>
光强测试结果
<ul>
    {% for url in urls %}
    <li>{{url}}</li><a href="/static/res1/{{url}}/res1.html">{{url}}</a>
    {% endfor %}
</ul>

```

``` html
<!DOCTYPE html>
全域扫描结果
<ul>
    {% for url in urls %}
    <li>{{url}}</li><a href="/static/res2/{{url}}/res.html">{{url}}</a>
    {% endfor %}
</ul>

```

### test.html

测试页

``` html
<!DOCTYPE html>
<!-- <form>
    First name: <input type="text" name="firstname"><br>
    Last name: <input type="text" name="lastname">
</form>

<form name="input" action="/fweb" method="post">
    Username: <input type="text" name="user">
    <input type="submit" value="Submit">
</form>

<title>My Application</title>
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
{% block body %}{% endblock %} -->


<html>
<!-- <head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head> -->
<body>

<form action="/test1" method="post" onclick="alert('光强测试请求已受理，请稍后查看结果。')">
<input type="button" value="开始光强测试">
	</form>

</body>
</html>

<button type="button" action="/fweb" method="post" onclick="alert('你好，世界!')">点我!</button>


<form name="input" action="/test1" method="post" onclick="alert('光强测试请求已受理，请稍后查看结果。')">
  <input type="submit" value="Submit">
</form>

<form name="input" action="/real1" method="post" onclick="alert('光强测试请求已受理，请稍后查看结果。')">
  <input type="submit" value="光源寻找">
</form>
<form name="input" action="/real2" method="post" onclick="alert('光强测试请求已受理，请稍后查看结果。')">
  <input type="submit" value="全域扫描">
</form>
<a href="/res1">光源寻找结果</a>

<br>

<a href="/res2">全域扫描结果</a>

```
