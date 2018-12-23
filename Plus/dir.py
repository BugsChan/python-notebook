from MyIO import MyIO
from Listeners import Listeners

class Run:
    commands=["ls","dir","tree"]
    introduction="""
    ls
        ls 目录
            -获取该目录下的文件结构
        ls
            -获取当前目录下的文件结构
    dir用法相同
    """

    @staticmethod
    def run(command,arg1,arg2):
        filePath = arg1
        if filePath == None:
            filePath = MyIO.getInstance().filePath
        Listeners.putInput(MyIO.getTree(filePath,command=="tree"))