from Listeners import Listeners
from MyIO import MyIO
from Config import Config
import os

class Run:
    commands=["vi","vim","cd"]

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