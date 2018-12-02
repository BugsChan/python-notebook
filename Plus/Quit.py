from Config import *
from Listeners import Listeners
from MyIO import MyIO
from my_time import MyTime
import json

class Run:
    commands=[":","：","quit"]

    introduction="""
    :q!
        退出编辑,但不保存
    :wq
        保存并退出
    :wq title
        将内容保存在title下并退出
    """

    @staticmethod
    def run(command,arg1,arg2):
        if "w" in arg1:
            my_io = MyIO()
            wText = Listeners.getInput()
            append = False
            if my_io.filePath == Config.getSrc():
                my_io.write_for_linux(wText)
                if arg2 == None or not arg2 in my_io.alltitles():
                    append = True
                    wText = my_io.to_json(arg2, wText) + ","
                else:
                    tmp = my_io.readObj()
                    for each in tmp:
                        if each['title'] == arg2:
                            each['time'] = MyTime.toString()
                            each["text"] = wText
                    wText = json.dumps(tmp)
                    wText = wText[1:len(wText) - 1] + ","

            my_io.write(wText, append)
            Listeners.putInput("文件已写入...")

        if "q" in arg1:
            if "!" in arg1 or "！" in arg1 or "w" in arg1:  # 强制退出
                exit(0)
            else:
                Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
                return True
