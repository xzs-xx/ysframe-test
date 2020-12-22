import os
import re
import glob
import numpy as np
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
def load_txt(path):
    linelist=[]
    with open(path,'r') as f:
        lines = f.readlines()
    for l in lines:
        linelist.append(l.strip())
    return linelist
def regmaximumRSS_Mb(lines,w):
    patternlist = re.compile(r'\[(\d*?-\d*?-\d*? \d*?:\d*?:\d*?).\d*?\]\[thread \d*?\]\[info\] {"currentRSS_Mb":(\d*?),',re.S)
    timeresult = re.findall(patternlist,str(lines))
    time_date = []
    CPU = []
    t = 0;
    for value in timeresult:
      timeArray = time.strptime(value[0], "%Y-%m-%d %H:%M:%S")
      if(t != 0):
        time_date.append(int(time.mktime(timeArray)) - t)
      else:
        t = int(time.mktime(timeArray))
        time_date.append(0)
      CPU.append(int(value[1]))
    #dirpath = os.path.dirname(w)
    portion = os.path.splitext(w)
    wt =portion[0] + ".png"
    plt.plot(time_date,CPU)
    plt.xlabel('time(s)',fontsize=14)
    plt.ylabel('CPU(mb)',fontsize=14)
    plt.title('',fontsize=24)
    plt.savefig(wt)
    plt.close()
    
if __name__ == '__main__':
    path=r'./'
    paths = glob.glob('./@ft-multidirect-mnn-th1.cfg/*.txt')
    for p in paths:
      #print(p)
      #w = os.path.basename(p)
      lines = load_txt(p)
      regmaximumRSS_Mb(lines,p)