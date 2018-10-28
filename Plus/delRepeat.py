"""
去重
"""

conf={
"from":"../tmps/2018_file.txt",
"to":"../tmps/2018_file.txt",
"encoding":"utf-8"
}

import json
import hashlib
import re

if __name__!="__main__":
    from Config import Config
    conf["from"]=Config.getSrc()
    conf["to"]=Config.getSrc()
    conf["encoding"]=Config.getFile()["encoding"]

def delrepeat():
    tmp=""
    h_cache=[]
    cache=[]
    with open(conf["from"],"r",encoding=conf["encoding"]) as in_file:
        for each in in_file:
            tmp+=each
        tmp="["+tmp[:len(tmp)-1]+"]"
        tmp=json.loads(tmp)

    for each in tmp:
        mtest=each["text"]
        mtest=re.sub("\n+$","",mtest)
        hashCode=hashlib.sha256(mtest.encode("UTF-8")).hexdigest()
        if hashCode in h_cache:
            continue
        else:
            h_cache.append(hashCode)
            cache.append(each)


    my_json=json.dumps(cache)
    my_json=my_json[1:len(my_json)-1]+","

    with open(conf["to"],"w",encoding=conf["encoding"]) as file:
        file.write(my_json)

class Run:
    commands=["delrepeat"]

    @staticmethod
    def run(command,arg0,arg1):
        delrepeat()


if __name__=="__main__":
    delrepeat()


    #input("Press any key to continue")