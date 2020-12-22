import os
import re
import glob
import numpy as np
import sys

showtable = ["吞吐率（qps）","单张平均用时（s）","单张中位时间（s）","单张最大用时（s）"
,"单张最小用时（s）","CPU平均利用率（%）","内存最大占用（mb）","GPU平均利用率（%）","显存最大占用（mb）"]

def loadlogcontent(path):
    linelist=[]
    with open(path,'r') as f:
        lines = f.readlines()
    for l in lines:
        linelist.append(l.strip())
    return linelist

def reg(lines):
    patternlist = re.compile(r'success process.*?AlgoTime:(.*?)ms',re.S)
    timeresult = re.findall(patternlist,str(lines))
    if len(timeresult) == 0:
        return 0;
    timeresult = list(map(float,timeresult))
    return timeresult
 
def regcpuUtil(lines):
    patternlist = re.compile(r'"cpuUtil":(.*?),',re.S)
    timeresult = re.findall(patternlist,str(lines))
    if len(timeresult) == 0:
        return 0;
    timeresult = list(map(float,timeresult))
    return float(np.mean(timeresult))

def regqps(lines):
    patternlist = re.compile(r"qps:(.*?)'",re.S)
    timeresult = re.findall(patternlist,str(lines))
    if len(timeresult) == 0:
        return 0;
    timeresult = list(map(float,timeresult))
    return float(np.mean(timeresult))

def reggpuUtil(lines):
    patternlist = re.compile(r'"gpuUtil":(.*?)}',re.S)
    timeresult = re.findall(patternlist,str(lines))
    if len(timeresult) == 0:
        return 0;
    timeresult = list(map(float,timeresult))
    return float(np.mean(timeresult))

def regmaximumRSS_Mb(lines):
    patternlist = re.compile(r'"maximumRSS_Mb":(.*?),',re.S)
    timeresult = re.findall(patternlist,str(lines))
    if len(timeresult) == 0:
        return 0;
    timeresult = list(map(float,timeresult))
    return  max(timeresult)

def gpuMemUsd_Mib(lines):
    patternlist = re.compile(r'"gpuMemUsd_Mib":(.*?),',re.S)
    timeresult = re.findall(patternlist,str(lines))
    if len(timeresult) == 0:
        return 0;
    timeresult = list(map(float,timeresult))
    return  max(timeresult)

def sort_file_by_threadNum(pathnames):
    file_tem = []
    file_comp = []
    for name in pathnames:
        value = name.split("_")[2]
        file_tem.append(name)
        file_tem.append(int(value))
        file_comp.append(file_tem)
        file_tem=[]
    file_comp.sort(key = lambda x:(x[1]) )
    return [x[0] for x in file_comp]

def outtable(listput):

def outtableDM(regpath):
    logpaths = glob.glob(regpath + '/*.txt')
    pathnames = [os.path.basename(x) for x in logpaths]
    pathnames = sort_file_by_threadNum(pathnames)
    print(pathnames)
    listput = []
    for pathname in pathnames:
        logpath=os.path.join(regpath,pathname)
        logcontent = loadlogcontent(logpath)
        listresult = []
        
        
        listresult.append(round(regqps(logcontent),3))
        result = reg(logcontent)
        listresult.append(round(float(np.mean(result))/1000,3))
        listresult.append(round(np.median(result)/1000,3))
        listresult.append(round(max(result)/1000,3))
        listresult.append(round(min(result)/1000,3))
        listresult.append(round(regcpuUtil(logcontent),3))
        listresult.append(round(regmaximumRSS_Mb(logcontent),3))
#        listresult.append(round(reggpuUtil(logcontent),3))
#        listresult.append(round(gpuMemUsd_Mib(logcontent),3))
        listput.append(listresult)
    regpath = os.path.join(regpath,"logtableout.md")
    output =  open(regpath,'w')
    output.write("|线程数")
    for pathname in pathnames:
        output.write("|")
        output.write(pathname.split("_")[2])
    output.write("|\n")
    output.write("|---------------------------------|\n")
    for i in range(0,7):
        output.write("|")
        output.write(showtable[i])
        for r in listput:
            output.write("|")
            output.write(str(r[i]))
        output.write("|\n")
    output.close()

def main(argv):
    if len(argv) < 2:
        return -1;
    outtableDM(argv[1])

if __name__ == '__main__':
    main(sys.argv)