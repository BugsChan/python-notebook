from Listeners import Listeners
from MyIO import MyIO
from Config import Config
import os

class Run:
    commands=["vi","vim","cd"]

    introduction="""
    vi/vim
    vi/vim auto
        -进入自动编辑模式 ,此时编辑的内容将会被存入固定缓存 (默认为此模式)
    vi/vim 文件路径
        -如文件存在 ,则加载改文件
        -如文件不存在,仍进入编辑模式
    cd
    cd 文件夹路径
        -进入此文件夹
    """

    @staticmethod
    def run(command,arg1,arg2):
        if arg1 != "auto":
            if MyIO.getInstance().filePath == Config.getSrc():
                MyIO().filePath = os.path.abspath(MyIO().filePath)
            MyIO().filePath = MyIO.getDictionary()
            if arg1.find(":") != -1 or arg1.startswith("\\"):
                MyIO().filePath = arg1
            elif arg1 == "..":
                MyIO().filePath = MyIO().filePath[:MyIO().filePath.rfind("\\")]
            elif MyIO().filePath.endswith("\\"):
                MyIO().filePath += arg1
            else:
                MyIO().filePath += "\\" + arg1
            if MyIO.isDictionary():
                Listeners.getInstance().attention = "--DIR " + MyIO.getInstance().filePath + "--"
            else:
                Listeners.getInstance().attention = "--INSERT IN " + MyIO.getInstance().filePath + "--"
            title = Config.getTitle(False)
            title = title.replace("${filename}", arg1)
            Listeners.getInstance().root.title()
            if MyIO.fileExist() and not MyIO.isDictionary():
                Listeners.putInput(MyIO.getInstance().read())
        else:
            Listeners.getInstance().attention = "--INSERT--"
            MyIO().filePath = Config.getSrc()

    @staticmethod
    def complete(cmd,arg1,arg2):
        path=MyIO.getDictionary()
        uncompleted=None
        def splite(path):
            tmp = path.rfind("\\")
            if tmp==len(path):
                return getParent(path[:len(path)-1])
            if tmp<0:
                tmp=path.rfind("/")
            elif path.rfind('/')>tmp:
                tmp=path.rfind("/")
            if tmp<0:
                return "ERROR FILEPATH"
            return path[:tmp+1],path[tmp+1:]

        if arg1.startswith("./"):
            uncompleted=arg1[2:]
        elif arg1.startswith("../"):
            path=splite(path)[0]
            uncompleted=arg1[3:]
        elif arg1.find(":")!=-1 or arg1.find("/")!=-1:
            path,uncompleted=splite(arg1)
        else:
            uncompleted=arg1

        ansArr=[]
        for each in os.listdir(path):
            if each.find(uncompleted)==0:
                ansArr.append(each)

        tmp = Listeners.getSame(ansArr)
        if not tmp:
            return False
        else:
            if splite(arg1)=="ERROR FILEPATH":
                return tmp
            else:
                return splite(arg1)[0]+tmp