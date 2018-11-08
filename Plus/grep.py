from Config import Config
from MyIO import MyIO
from Listeners import Listeners


def grep(self, words, path=False):
    if not path:
        path = self.filePath

    ans = ""
    if Config.getSrc() != self.filePath:
        for each in self.read():
            if each.find(words) != -1:
                ans += each
    else:
        for each in self.readObj():
            if each["text"].find(words) != -1:
                ans += each["text"]

    return ans

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
            Listeners.putInput(grep(MyIO.getInstance(),words, filePath))