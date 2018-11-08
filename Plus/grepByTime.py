from MyIO import MyIO
from Listeners import Listeners
from Config import Config

class Run:
    commands=["time","date"]
    introduction="""
    date (time)
        date 日期
            -查询该日期中写入的内容
    """


    @staticmethod
    def run(command,arg1,arg2):
        if MyIO.getInstance().filePath != Config.getSrc():
            Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
            return;
        else:
            ans=""
            tmp=MyIO.getInstance().readObj()
            for each in tmp:
                if each["time"].find(arg1) != -1:
                    ans += each["text"] + "\n"

            Listeners.putInput(ans)