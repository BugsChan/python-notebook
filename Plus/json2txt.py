"""
该软件用于将 2018_file.txt以方便linux grep 的格式复制到2018_grep_for_linux.txt
可酌情修改
"""

conf={
"from":"../tmps/2018_file.txt",
"to":"../tmps/2018_grep_for_linux.txt"
}

import json

if __name__!="__main__":
    from Config import Config
    conf["from"]=Config.getSrc()
    conf["to"]=Config.getLinuxGrepSrc()

def json2txt():
    tmp=""
    with open(conf["from"],"r",encoding="utf-8") as in_file:
        with open(conf["to"],"w",encoding="utf-8") as out_file:
            for each in in_file:
                tmp+=each
            tmp="["+tmp[:len(tmp)-1]+"]"
            tmp=json.loads(tmp)
            for each in tmp:
                text=each["text"]
                date=each["time"]
                out_file.write(date+": "+text)

class Run:
    commands=["json2txt"]

    @staticmethod
    def run(command,arg0,arg1):
        json2txt()


if __name__=="__main__":
    json2txt()
    #input("Press any key to continue")