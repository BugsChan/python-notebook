from MyIO import MyIO
from Listeners import Listeners

class Run:
    commands=["ls","dir"]

    @staticmethod
    def run(command,arg1,arg2):
        filePath = arg1
        if filePath == None:
            filePath = MyIO.getInstance().filePath
        Listeners.putInput(MyIO.getTree(filePath))