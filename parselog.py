import os
import re
import glob
import numpy as np
import sys

class ParseLog:
    lines = ""
    listresult = []
    def _init_(self,lines):
        ParseLog.lines = lines
        __regqps()
        __regImageRuntime()
        __regcpuUtil()
        __regmaximumRSS_Mb()
        __reggpuUtil()
    
    def __regImageRuntime(self):
        patternlist = re.compile(r'success process.*?AlgoTime:(.*?)ms',re.S)
        timeresult = re.findall(patternlist,str(lines))
        if len(timeresult) == 0:
            return 0;
        timeresult = list(map(float,timeresult))
        listresult.append(round(float(np.mean(timeresult))/1000,3))
        listresult.append(round(np.median(timeresult)/1000,3))
        listresult.append(round(max(timeresult)/1000,3))
        listresult.append(round(min(timeresult)/1000,3))
    
    def __regqps(self):
        patternlist = re.compile(r"qps:(.*?)'",re.S)
        timeresult = re.findall(patternlist,str(lines))
        if len(timeresult) == 0:
            return 0;
        timeresult = list(map(float,timeresult))
        listresult.append(round(float(np.mean(timeresult),3))
 
    def __regcpuUtil(self):
        patternlist = re.compile(r'"cpuUtil":(.*?),',re.S)
        timeresult = re.findall(patternlist,str(lines))
        if len(timeresult) == 0:
            return 0;
        timeresult = list(map(float,timeresult))
        listresult.append(round(float(np.mean(timeresult)),3)) 
    
    def __regmaximumRSS_Mb(self):
        patternlist = re.compile(r'"maximumRSS_Mb":(.*?),',re.S)
        timeresult = re.findall(patternlist,str(lines))
        if len(timeresult) == 0:
            return 0;
        timeresult = list(map(float,timeresult))
        listresult.append(round(max(timeresult),3)) 
        
    def __reggpuUtil(self):
        patternlist = re.compile(r'"gpuUtil":(.*?)}',re.S)
        timeresult = re.findall(patternlist,str(lines))
        if len(timeresult) == 0:
            return 0;
        timeresult = list(map(float,timeresult))
        listresult.append(round(float(np.mean(timeresult)),3))

    def __gpuMemUsd_Mib(self):
        patternlist = re.compile(r'"gpuMemUsd_Mib":(.*?),',re.S)
        timeresult = re.findall(patternlist,str(self))
        if len(timeresult) == 0:
            return 0;
        timeresult = list(map(float,timeresult))
        listresult.append(round(max(timeresult),3))
    
    def getList():
        return listresult