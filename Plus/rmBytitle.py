from MyIO import MyIO
from Listeners import Listeners
import json

class Run:
    commands=["titlerm","rmbytitle"]
    introduction="删除title"

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

    @staticmethod
    def complete(cmd, arg1, arg2, loop=False):
        titlelist = []
        if cmd == "alltitles":
            return False
        else:
            titles = MyIO.getInstance().alltitles()
            for each in titles:
                if each.find(arg1) == 0:
                    titlelist.append(each)
            if loop:
                return list(titles.keys())
            return Listeners.getSame(titlelist)

    @staticmethod
    def next(cmd, arg1, arg2, prev=False):
        titlelist = Run.complete(cmd, arg1, arg2, True)
        if len(titlelist) == 0:
            return False
        titlelist.sort(reverse=prev)
        if not arg1:
            return titlelist[0]
        else:
            tmp = False
            for each in titlelist:
                if each == arg1:
                    tmp = True
                elif tmp:
                    return each
            for each in titlelist:
                if each.find(arg1) == 0:
                    return each
            return False

    @staticmethod
    def last(cmd, arg1, arg2):
        return Run.next(cmd, arg1, arg2, True)