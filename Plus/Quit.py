from Config import *
from Listeners import Listeners
from MyIO import MyIO

class Run:
    commands=[":","：","quit"]
    @staticmethod
    def run(command,arg1,arg2):
        if "q" in arg1:
            if "w" in arg1:
                my_io = MyIO()
                wText = Listeners.getInput()
                if my_io.filePath == Config.getSrc():
                    my_io.write_for_linux(wText)
                    wText = my_io.to_json(wText) + ","
                my_io.write(wText)
                exit(0)
            elif "!" in arg1 or "！" in arg1:  # 强制退出
                exit(0)
            else:
                Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
                return True
