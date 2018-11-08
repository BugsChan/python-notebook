from MyIO import MyIO
from Listeners import Listeners
import json

class Run:
    commands=["titlerm"]

    @staticmethod
    def run(cmd,arg1,arg2):
        if not arg1 in MyIO.getInstance().alltitles():
            from Config import Config
            Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
            return True
        else:
            tmp=MyIO.getInstance().readObj()
            for each in tmp:
                if each["title"]==arg1:
                    tmp.remove(each)
            text=json.dumps(tmp)
            text=text[1:len(text)-1]+","
            MyIO().write(text,False)
            if MyIO()._alltitles!=None:
                del MyIO()._alltitles[arg1]