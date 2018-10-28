import ctypes
import json
from my_time import *

class Config:
    ui = None
    screen_width=None
    screen_height=None
    file=None
    title=None
    inputConf=None
    commandConf=None
    font=None

    def __new__(cls):
        if not hasattr(cls,"_instance"):
            cls._instance=object.__new__(cls)

        return cls._instance


    def __init__(self):
        if self.ui==None:
            with open("pim-config.json",encoding="utf-8") as conf:
                config = json.load(conf)
                self.ui=config["ui"]
                self.file=config["file"]
                self.title=config["title"]
                self.inputConf=config["text"]
                self.commandConf=config["command_line"]
                if type(self.commandConf)==str:
                    self.commandConf=self.inputConf
                self.font=config["font"]

            winapi = ctypes.windll.user32
            self.screen_width = winapi.GetSystemMetrics(0)
            self.screen_height = winapi.GetSystemMetrics(1)

    @staticmethod
    def getConf():
        return Config()

    @staticmethod
    def getUI():
        return Config.getConf().ui

    @staticmethod
    def getScreenSize():
        conf=Config.getConf()
        return conf.screen_width,conf.screen_height

    @staticmethod
    def getLength(length,type):
        if length.endswith("px"):
            return length[:len(length)-2]
        elif length.endswith("%"):
            length=float(length[:len(length)-1])/100
            totle=None
            if type=="width":
                totle=Config.getScreenSize()[0]
            else:
                totle=Config.getScreenSize()[1]
            length=int(totle*length)
            return str(length)



    @staticmethod
    def getWidth():
        width=Config.getUI()["width"]
        return Config.getLength(width,"width")

    @staticmethod
    def getHeight():
        height=Config.getUI()["height"]
        return Config.getLength(height,"height")

    @staticmethod
    def getOffset(offset,type):
        end=None

        if offset.endswith("%"):
            end=-1
        elif offset.endswith("px"):
            end=-2

        offset=offset[:len(offset)+end]

        if end==-1:
            totle=None
            if type=="x":
                totle=0
            else:
                totle=1
            totle = Config.getScreenSize()[totle]
            offset=float(offset)/100*totle

        offset=int(offset)
        if offset<0:
            if type=="x":
                totle=0
            else:
                totle=1
            totle = Config.getScreenSize()[totle]
            offset=totle+offset

        return str(offset)

    @staticmethod
    def getX():
        x=Config.getUI()["x"]
        return Config.getOffset(x,"x")

    @staticmethod
    def getY():
        y=Config.getUI()["y"]
        return Config.getOffset(y,"y")

    @staticmethod
    def getResizable(type):
        if type=='x':
            return Config.getUI()["x_resizable"]
        else:
            return Config.getUI()["y_resizable"]

    @staticmethod
    def fullScreen():
        return Config.getUI()["fullScreen"]

    @staticmethod
    def alwaysOnTop():
        return Config.getUI()["alwaysOnTop"]

    @staticmethod
    def getFile():
        return Config.getConf().file

    @staticmethod
    def getSrc():
        res=Config.getFile()["src"]
        return MyTime.dump(res)

    @staticmethod
    def getTitle(dumpFileName=True):
        res=Config.getConf().title
        res=MyTime.dump(res)
        if not dumpFileName:
            return res
        return res.replace("${filename}",Config.getSrc())

    @staticmethod
    def getInputConf():
        return Config.getConf().inputConf

    @staticmethod
    def getCommandConf():
        return Config.getConf().commandConf

    @staticmethod
    def getFontStyle():
        return Config.getConf().font

    @staticmethod
    def getLinuxGrepSrc():
        res = Config.getFile()["linux_grep_src"]
        return MyTime.dump(res)

if __name__=="__main__":
    ans=Config.getSrc()
    print(ans)

