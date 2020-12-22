import os,sys
import re
import hashlib
def getfilemd5(path):
    f = open(path,'rb')
    content= f.read()
    f.close()
    return hashlib.md5(content).hexdigest()
if __name__ == '__main__':
    a = ".//checkver.out .//testlib"
    b = os.popen(a,'r',1)
    out = b.read()
    listout = out.splitlines()
    list_so = []
    output = open('version.MD','w') 
    output.write("### 当前测试版本\n")
    output.write("|  so文件   |   版本   |    md5   |\n")
    output.write("|---------------------------------|\n")
    for l in listout:
        file = l.split("->")
        file.append(getfilemd5(os.path.join(".//testlib",file[0].replace(" ", ""))))
        rowtxt = '|{}|{}|{}|'.format(file[0],file[1],file[2])
        output.write(rowtxt)
        output.write('\n')
    output.close()