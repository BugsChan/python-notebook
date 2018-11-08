from Listeners import Listeners
from MyIO import MyIO


def grepByTitle(self, title):
    ans = ""
    if title == None:
        return ans

    for each in self.readObj():
        if each["title"] == title:
            ans += each["text"] + "\n"

    return ans

class Run:
    commands=["title","alltitles"]

    @staticmethod
    def run(cmd,arg1,arg2):
        if cmd=="alltitles":
            tmp="TITLE\tTIME\n"
            titles=MyIO.getInstance().alltitles()
            for each in titles:
                tmp+=each+"\t"+titles[each]+"\n"
            Listeners.putInput(tmp)
        elif arg1!=None:
            Listeners.putInput(grepByTitle(MyIO.getInstance(),arg1))

