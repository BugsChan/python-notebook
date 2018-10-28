from Config import Config
from MyIO import MyIO
from Listeners import Listeners

class Run:
    commands=["grep","find"]

    @staticmethod
    def run(command,arg1,arg2):
        filePath = None
        words = None
        if arg2 != None:
            filePath = arg1
            words = arg2
        else:
            words = arg1

        if not MyIO.fileExist(filePath):
            Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
            return;
        else:
            Listeners.putInput(MyIO.getInstance().grep(words, filePath))