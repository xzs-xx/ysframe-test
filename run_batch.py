import os
import json
import subprocess
import io
import time
import sys
os.environ['LD_LIBRARY_PATH']="../bin"
imgdir=['826x1169','1240x1753','1653x2338']
startthread=[1,4,8,12,16]
test_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

def loadjson(path):
    with io.open(path,'r',encoding='utf-8') as f:
        return json.load(f)
def run(inpath,jsonpath,resultout):
    jsondict=loadjson(jsonpath)
    for d in imgdir:
        resultsave = os.path.join(resultout,d)
        imgpath=os.path.join(inpath,d)
        logSaveDir = os.path.join(resultout,d,str(test_time))
        for threadNum in startthread:
            jsondict['imgpath']=imgpath
            jsondict['saveDir']=resultsave
            jsondict['logDir']=logSaveDir
            jsondict['threadNum']=threadNum
            with open(jsonpath,'w') as f:
                json.dump(jsondict ,f)
            os.system('./run.sh')
def main(argv):
    if len(argv) < 2:
        return -1;
    else:
        run(argv[1],'ftConfig.json','log')
if __name__ == '__main__':
    main(sys.argv)