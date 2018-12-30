import re
from Config import Config
from MyIO import *
from tkinter import *

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
    def getCommand(text=False):
        if not text:
            text=Listeners.getInstance().entry.get()
        text=re.sub(" +"," ",text)
        command=None
        arg1=None
        arg2=None
        if text.startswith(":") or text.startswith("："):
            command=":"
            if " " in text:
                arg1=text[1:text.find(" ")]
                arg2=text[text.find(" ")+1:]
            elif len(text)>=2:
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
    def getInput():
        return Listeners.getInstance().text.get("0.0", "end")

    @staticmethod
    def putInput(input_str):
        textObj = Listeners.getInstance().text
        textObj.delete("1.0", "end")
        textObj.insert("1.0", input_str)

    @staticmethod
    def entry_Return(arg):
        command,arg1,arg2=Listeners.getCommand()
        import Plus.Interface
        if not Plus.Interface.Runcmd().RunCommand(command,arg1,arg2):
            Listeners.getInstance().text.focus_set()


    @staticmethod
    def start_insert(arg):
        text=Listeners.getInstance().entry.get()
        import Plus.Interface
        cmds=Plus.Interface.Runcmd().cmds
        if text!="":
            for each in cmds:
                if each.find(text+"i")!=-1 or (text.find(each)!=-1 and text.find(" ")!=-1):
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

    @staticmethod
    def conplement(arg):
        #补全算法
        entry=Listeners().entry
        text = entry.get()
        command, arg1, arg2 = Listeners.getCommand(text)
        import Plus.Interface
        ans=None
        obj=Plus.Interface.Runcmd()
        if arg.keysym=="Up":
            ans=obj.last(command,arg1,arg2)
        elif arg.keysym=="Down":
            ans=obj.next(command,arg1,arg2)
        else:
            ans=obj.conplement(command, arg1, arg2)
        if ans!=False and ans!=text:
            entry.delete(0,END)
            print("ans=",ans)
            entry.insert(0,ans)
            entry.icursor(len(ans))

    @staticmethod
    def getSame(arr):
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 0:
            return False
        else:
            tmp1 = arr.pop()
            tmp2 = arr.pop()
            if tmp1==tmp2:
                arr.append(tmp1)
                return Listeners.getSame(arr)
            length = len(tmp1)
            if len(tmp2) < length:
                length = len(tmp2)
            for each in range(length):
                if tmp1[each] != tmp2[each]:
                    arr.append(tmp1[:each])
                    return Listeners.getSame(arr)
            arr.append(tmp1[:each+1])
            return Listeners.getSame(arr)


if __name__=="__main__":
    print(Listeners.getSame(["alltitles","a"]))