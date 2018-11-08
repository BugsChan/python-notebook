from MyIO import MyIO
import json

class Run:
    commands=["addtitle"]

    @staticmethod
    def run(*cmds):
        obj=MyIO().readObj()
        for each in obj:
            if not "title" in each:
                each["title"]=None
        wText = json.dumps(obj)
        wText = wText[1:len(wText) - 1] + ","
        MyIO().write(wText,False)

if __name__=='__main__':
    Run.run()