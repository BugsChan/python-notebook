from Config import Config
from MyIO import MyIO
from Listeners import Listeners


def grep(myio, words, path=False):
    if not path:
        path = myio.filePath

    ans = ""
    if Config.getSrc() != myio.filePath:
        for each in myio.read():
            if each.find(words) != -1:
                ans += each
    else:
        gapline=Config.getUI()["gapline"]

        for each in myio.readObj():
            if each["text"].find(words) != -1:
                ans += each["text"]+gapline

    return ans

class Run:
    commands=["grep","find"]
    introduction="""
    grep (find)
        grep 关键字
            -在当前文件中查询
    """


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