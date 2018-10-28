import json
from my_time import *
from Config import *
import os

class MyIO:
    filePath=None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super().__new__(cls)

        return cls._instance

    def __init__(self):
        if self.filePath==None:
            self.filePath=Config.getSrc()

    @staticmethod
    def getInstance():
        return MyIO()

    @staticmethod
    def fileExist(path=False):
        if not path:
            path=MyIO.getInstance().filePath
        return os.path.exists(path)

    @staticmethod
    def isDictionary(path=False):
        if not path:
            path=MyIO.getInstance().filePath
        return os.path.isdir(path)

    @staticmethod
    def getDictionary(path=False):
        if not path:
            path=MyIO.getInstance().filePath

        if MyIO.isDictionary(path):
            return path
        else:
            absPath=os.path.abspath(path)
            return absPath[:absPath.rfind("\\")]

    @staticmethod
    def getTree(path=False):
        path=MyIO.getDictionary(path)
        ans=path+"\nname\ttype\n"
        for each in os.listdir(path):
            tmp=str(each)
            if MyIO.isDictionary(path+"\\"+each):
                tmp+="\tdir\n"
            else:
                tmp+="\tfile\n"
            ans+=tmp

        return ans

    def write(self,text):
        type=Config.getSrc()==self.filePath
        if type:
            type="a"
        else:
            type="w"

        encoding=Config.getFile()["encoding"]
        with open(self.filePath,type,encoding=encoding) as file:
            file.write(text)

    def to_json(self,text):
        ans={"time":MyTime.toString(),"text":text}
        return json.dumps(ans)

    def read(self):
        ans=""
        with open(self.filePath,"r",encoding=Config.getFile()["encoding"]) as file:
            for each in file:
                ans+=each
        return ans

    def grep(self,words,path=False):
        if not path:
            path=self.filePath

        ans=""
        with open(path,"r",encoding=Config.getFile()["encoding"]) as file:
            if Config.getSrc()!=self.filePath:
                for each in file:
                    if each.find(words)!=-1:
                        ans+=each
            else:
                tmp=""
                for each in file:
                    tmp+=each
                tmp="["+tmp[:len(tmp)-1]+"]"
                tmp=json.loads(tmp)
                for each in tmp:
                    if each["text"].find(words)!=-1:
                        ans+=each["text"]

        return ans

    def getByDate(self,date_str):
        ans=""
        with open(self.filePath,"r") as file:
            tmp = ""
            for each in file:
                tmp += each
            tmp = "[" + tmp[:len(tmp) - 1] + "]"
            tmp = json.loads(tmp)
            for each in tmp:
                if each["time"]==date_str:
                    ans += each["text"]+"\n"

        return ans

    @staticmethod
    def mkdir(dirname):
        if MyIO().filePath!=Config.getSrc():
            MyIO().filePath=os.path.abspath(MyIO().filePath)
        path=MyIO.getDictionary()
        if path.endswith("\\"):
            path+=dirname
        else:
            path+="\\"+dirname
        os.makedirs(path)

    @staticmethod
    def rm(dirname):
        if MyIO().filePath!=Config.getSrc():
            MyIO().filePath=os.path.abspath(MyIO().filePath)
        path=MyIO.getDictionary()
        if path.endswith("\\"):
            path+=dirname
        else:
            path+="\\"+dirname
        if MyIO.isDictionary(path):
            try:
                os.rmdir(path)
            except:
                return False
        else:
            os.remove(path)

    @staticmethod
    def write_for_linux(text):
        if MyIO().filePath == Config.getSrc():
            encoding = Config.getFile()["encoding"]
            with open(Config.getLinuxGrepSrc(), "a", encoding=encoding) as file:
                file.write(MyTime.toString() + ":" + text + "\n")



if __name__=="__main__":
    print(MyIO.getTree("G:\\test"))