

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
        a=os.popen('touch '+p+p2)
        print(b,a)
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