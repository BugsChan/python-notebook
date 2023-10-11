from MyIO import MyIO
import json

class Run:
    commands=["addtitle"]
    introduction="""
    该命令用于将旧版缓存文件(没有title属相)转化为新版缓存,title默认写入为None
    """

    @staticmethod
    def run(*cmds):
        obj=MyIO().readObj()
        for each in obj:
            if not "title" in each:
                each["title"]=None
            if not "encrypt" in each:
                each["encrypt"] = False
        wText = json.dumps(obj, ensure_ascii=False)
        wText = wText[1:len(wText) - 1] + ","
        MyIO().write(wText,False)

if __name__=='__main__':
    Run.run()
