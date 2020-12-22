import os
import json
import subprocess
import io
import time
import sys
logsavefile = []
runpaths = []
changepath = []
def getlogsave(i,logsave):
    if i < len(changepath):
        if isinstance(changepath[i],list):
            for key in changepath[i]:
                logsaveq = logsave + "/" + key
                getlogsave(i + 1,logsaveq)
        else:
            logsave = logsave + "/" + changepath[i]
            getlogsave(i + 1,logsave)
    elif i >= len(changepath):
        logsavefile.append(logsave)
if __name__ == '__main__':
    with io.open("./src.json",'r',encoding='utf-8') as f:
        runpaths = json.load(f)
    for key in runpaths:
        t = list(runpaths[key])
        changepath.append(t)
    getlogsave(0,"")
    print(logsavefile)