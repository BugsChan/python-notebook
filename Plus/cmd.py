import os
from Listeners import Listeners

class Run:
    commands=["cmd"]
    introduction="""
    cmd arg1 arg2 ...:
        将"arg1 arg2 ..."作为字符串输入到命令行中
    """


    @staticmethod
    def run(cmd,*args):
        cmdstr = ""
        for each in args:
            cmdstr += each + " "
        os.system(cmdstr)
