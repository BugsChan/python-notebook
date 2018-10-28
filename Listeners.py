import re
from Config import Config
from MyIO import *
from tkinter import *
import plusIn

class Listeners:

    root=None
    text=None
    entry=None
    attention="--INSERT--"

    def __new__(cls,*args):
        if not hasattr(cls,"_instance"):
            cls._instance=super().__new__(cls)

        return cls._instance

    def __init__(self,root=None,text=None,entry=None):
        if self.root==None:
            self.root=root
            self.text=text
            self.entry=entry

    @staticmethod
    def getInstance():
        return Listeners()

    @staticmethod
    def getCommand(text):
        text=re.sub(" +"," ",text)
        command=None
        arg1=None
        arg2=None
        if text.startswith(":") or text.startswith("："):
            command=":"
            arg1=text[1:]
        else:
            res=text.split(" ")
            if len(res)>=3:
                arg2=res[2]
            if len(res)>=2:
                arg1=res[1]
            command=res[0]

        command=command.lower()
        if arg1!=None:
            arg1=re.sub("^-*","",arg1)
        if arg2!=None:
            arg2=re.sub("^-*","",arg2)

        return command, arg1, arg2


    @staticmethod
    def entry_Return(arg):
        def putInput(input_str):
            textObj = Listeners.getInstance().text
            textObj.delete("1.0", "end")
            textObj.insert("1.0", input_str)

        text=Listeners.getInstance().entry.get()
        command,arg1,arg2=Listeners.getCommand(text)

        if command==":" or command=="：":
            if "q" in arg1:
                if "w" in arg1:
                    my_io=MyIO()
                    wText=Listeners.getInstance().text.get("0.0","end")
                    if my_io.filePath==Config.getSrc():
                        my_io.write_for_linux(wText)
                        wText=my_io.to_json(wText)+","
                    my_io.write(wText)
                    exit(0)
                elif "!" in arg1 or "！":#强制退出
                    exit(0)
                else:
                    Listeners.getInstance().entry["background"]=Config.getUI()["alert_color"]
                    return;
        elif command=="vi" or command=="vim" or command=="cd":
            if arg1!="auto":
                if MyIO.getInstance().filePath==Config.getSrc():
                    MyIO().filePath=os.path.abspath(MyIO().filePath)
                MyIO().filePath=MyIO.getDictionary()
                if arg1.find(":")!=-1 or arg1.startswith("\\"):
                    MyIO().filePath=arg1
                elif arg1=="..":
                    MyIO().filePath=MyIO().filePath[:MyIO().filePath.rfind("\\")]
                elif MyIO().filePath.endswith("\\"):
                    MyIO().filePath+=arg1
                else:
                    MyIO().filePath+="\\"+arg1
                Listeners.getInstance().attention = "--INSERT IN " + MyIO.getInstance().filePath + "--"
                title=Config.getTitle(False)
                title=title.replace("${filename}", arg1)
                Listeners.getInstance().root.title()
                if MyIO.fileExist() and not MyIO.isDictionary():
                    putInput(MyIO.getInstance().read())
            else:
                Listeners.getInstance().attention="--INSERT--"
                MyIO().filePath=Config.getSrc()
        elif command=="fullscreen" or command=="max":
            root=Listeners.getInstance().root
            if arg1!="false":
                root.attributes("-fullscreen", True)
            else:
                root.attributes("-fullscreen", False)
        elif command=="top":
            root=Listeners.getInstance().root
            if arg1!="false":
                root.attributes('-topmost', True)
            else:
                root.attributes('-topmost', False)
        elif command=="grep" or command=="find":
            filePath=None
            words=None
            if arg2!=None:
                filePath=arg1
                words=arg2
            else:
                words=arg1

            if not MyIO.fileExist(filePath):
                Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
                return;
            else:
                putInput(MyIO.getInstance().grep(words,filePath))
        elif command=="date" or command=="time":
            if MyIO.getInstance().filePath!=Config.getSrc():
                Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
                return;
            else:
                putInput(MyIO.getInstance().getByDate(arg1))
        elif command=="ls":
            filePath=arg1
            if filePath==None:
                filePath=MyIO.getInstance().filePath
            putInput(MyIO.getTree(filePath))
        elif command=="mkdir":
            MyIO.mkdir(arg1)
        elif command=="rm":
            MyIO.rm(arg1)

        Listeners.getInstance().text.focus_set()


    @staticmethod
    def start_insert(arg):
        text=Listeners.getInstance().entry.get()
        if text.startswith("v") or text.startswith("mkd") or text.startswith("rm") or text.startswith("grep"):
            return
        textObj=Listeners.getInstance().text
        m_listener=Listeners.getInstance()
        textObj.focus_set()

    @staticmethod
    def input_focus(arg):
        entry=Listeners.getInstance().entry
        entry.delete(0,END)
        entry["background"]=Config.getCommandConf()["background"]
        entry.insert(0,Listeners.getInstance().attention)

    @staticmethod
    def command_mod(arg):
        entry = Listeners.getInstance().entry
        entry.focus_set()

    @staticmethod
    def command_focus(arg):
        entry = Listeners.getInstance().entry
        entry.delete(0, END)



                