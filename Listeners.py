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
    def newLine(arg):
        #TODO 换行自动对齐前一行、自动补齐数字
        text = Listeners().text
        cursorPosition = text.index("insert")
        cursorPosition = cursorPosition
        content = text.get(cursorPosition.split(".")[0] + ".0", cursorPosition)
        head = re.search("^\s*(\d*\.)*", content)

        if head:
            head = head.group()
        else:
            return
        if len(head) != 0:
            def addOne(matched):
                return str(int(matched.group()[:-1]) + 1) + "."

            newLineHead = re.sub("\d*\.", addOne, head)
            text.insert("insert", '\n' + newLineHead)
            return  "break"



    @staticmethod
    def getCommand(text=False):
        if not text:
            text=Listeners.getInstance().entry.get()
        text=re.sub(" +"," ",text)
        args = text.split(" ")

        if args[0].startswith(":") or args[0].startswith("："):
            args.insert(0, ":")
            args[1] = args[1][1:]

        args[0]=args[0].lower()

        for i in range(len(args)):
            args[i] = re.sub("^-*", "", args[i])

        return args

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
        args=Listeners.getCommand()
        import Plus.Interface
        if not Plus.Interface.Runcmd().RunCommand(*args):
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
        args = Listeners.getCommand(text)
        tmp = None
        if args[0] in "：:":
            tmp = args.pop(1)
            print(args)
        command = args[0] if len(args) > 0 else ""
        arg1 = args[1] if len(args) > 1 else ""
        arg2 = args[2] if len(args) > 2 else ""
        import Plus.Interface
        ans=None
        obj=Plus.Interface.Runcmd()
        if arg.keysym=="Up":
            ans=obj.last(command,arg1,arg2)
        elif arg.keysym=="Down":
            ans=obj.next(command,arg1,arg2)
        elif arg1 == "":
            ans=obj.next(command, arg1, arg2)
        else:
            ans=obj.conplement(command, arg1, arg2)
        if ans!=False and ans!=text:
            entry.delete(0,END)
            if args[0] in "：:":
                ans = ":" + tmp + ans[1:]
            entry.insert(0,ans)
            entry.icursor(len(ans))
        return "break"

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
