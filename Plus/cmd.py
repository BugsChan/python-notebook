import os
from Listeners import Listeners

class Run:
    commands=["cmd","cmdinput"]
    introduction="""
    cmd arg1 arg2:
        将"arg1 arg2"作为字符串输入到命令行中
    inputcmd :
        将输入面板中的内容输入到命令行(shell)中
    """


    @staticmethod
    def run(cmd,arg1,arg2):
        if cmd=="cmdinput":
            myinput=Listeners.getInput()
            os.system(myinput)
        else:
            if arg1==None:
                arg1=""
            if arg2==None:
                arg2=""
            os.system(arg1+" "+arg2)