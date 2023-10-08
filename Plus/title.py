from Listeners import Listeners
from MyIO import MyIO
from Plus.Quit import MyCrypt

from tkinter.messagebox import showerror

def grepByTitle(self, title, password=False):
    ans = ""
    if title == None:
        return ans

    for each in self.readObj():
        if each["title"] == title:
            ans += each["text"] + "\n"
            if each["encrypt"]:
                if password:
                    ans = MyCrypt().decrypt(password, ans)
                    if not ans:
                        showerror("密码错误", "密码错误, 请更正! ")
                else:
                    ans = False
                    showerror("密码错误", "笔记已加密, 请键入密码! ")
    return ans

class Run:
    commands=["title", "read","alltitles"]
    introduction="""
    title title
        根据title查找写入的内容
    alltitles
        查找所有的title
    """

    @staticmethod
    def run(cmd,arg1,arg2):
        if cmd=="alltitles":
            tmp="TITLE\tTIME\n"
            titles=MyIO.getInstance().alltitles()
            for each in titles:
                tmp+=each+"\t"+titles[each]+"\n"
            Listeners.putInput(tmp)
        elif arg1!=None:
            ans = grepByTitle(MyIO.getInstance(),arg1, arg2)
            if ans:
                Listeners.putInput(ans)
            else:
                return True

    @staticmethod
    def complete(cmd,arg1,arg2,loop=False):
        titlelist=[]
        if cmd=="alltitles":
            return False
        else:
            titles=MyIO.getInstance().alltitles()
            for each in titles:
                if each.find(arg1)==0:
                    titlelist.append(each)
            if loop:
                return list(titles.keys())
            return Listeners.getSame(titlelist)

    @staticmethod
    def next(cmd,arg1,arg2,prev=False):
        titlelist=Run.complete(cmd,arg1,arg2,True)
        if len(titlelist)==0:
            return False
        titlelist.sort(reverse=prev)
        if not arg1:
            return titlelist[0]
        else:
            tmp=False
            for each in titlelist:
                if each==arg1:
                    tmp=True
                elif tmp:
                    return each
            for each in titlelist:
                if each.find(arg1)==0:
                    return each
            return False

    @staticmethod
    def last(cmd,arg1,arg2):
        return Run.next(cmd,arg1,arg2,True)
