#!/usr/bin/env python2
import time
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
# import matplotlib as mpl
def update_and_plot(fname):
    namesdog=['time','Humidity (%)','Temperature (oC)','scode']
    df = pd.read_csv(fname,parse_dates=[0],header=None,index_col=0,names=namesdog)
    # df.rename(columns={'0': 'time', '1': 'h', '2': 'c', '3': 's'}, inplace=True) 
    # print(df)
    ab=df.tail(3000)
    ab.cumsum()
    hh=ab[['Temperature (oC)','Humidity (%)']]
    hhp=hh.plot(secondary_y=['Humidity (%)'],mark_right=False,figsize=(16,9),title='Temperature (oC)&Humidity (%)')
    hhp.set_ylabel('Temperature (oC)')
    hhp.right_ax.set_ylabel('Humidity (%)')
    hhp.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M:%S'))
    # hhp.title(u'Temperature (oC)&Humidity (%)')
    # hhp.legend(loc='best',labels = ['Temperature (oC)','Humidity (%)'])  
    # cd=ab['Humidity (%)']
    # ef=ab['Temperature (oC)']
    # cd.plot()
    # ef.plot(secondary_y=True)
    plt.savefig('data.jpg')
    ab.to_csv(fname,header=0,index=0)
    plt.close()
    # print(ab[['Humidity (%)','Temperature (oC)']])
update_and_plot('data.csv')
print 'ok'