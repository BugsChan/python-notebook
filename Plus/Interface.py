import Plus
from Listeners import Listeners
from Config import Config
class Runcmd:

    cmds=None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super().__new__(cls)

        return cls._instance

    def __init__(self):
        if self.cmds!=None:
            return

        self.cmds={}
        for each in Plus.all:
            obj=__import__("Plus."+each,fromlist=True)
            if hasattr(obj,"Run"):
                for i in obj.Run.commands:
                    self.cmds[i]=each

        print(self.cmds)

    def RunCommand(self,command,*args):
        if command in self.cmds:
            use=self.cmds[command]
            obj=__import__("Plus."+use,fromlist=True)
            try:
                #新版api
                return obj.Run.run(command, *args)
            except TypeError as e:
                #旧版api
                return obj.Run.run(command, \
                args[0] if len(args)>=1 else "", \
                args[1] if len(args)>=2 else "")
        else:
            return False

    def conplement(self,cmd,arg1,arg2):
        if not cmd:
            return False
        elif not arg1:
            canBeUsed = []
            for each in self.cmds:
                if each.find(cmd)==0:
                    canBeUsed.append(each)
            return Listeners.getSame(canBeUsed)
        else:
            if cmd in self.cmds:
                use=self.cmds[cmd]
                obj=__import__("Plus."+use,fromlist=True)
                if hasattr(obj.Run,"complete"):
                    tmp=obj.Run.complete(cmd,arg1,arg2)
                    if not tmp:
                        return False
                    else:
                        return cmd+" "+tmp
                else:
                    return False
            else:
                return False

    def next(self,cmd,arg1,arg2,mcmds=False,callBack="next"):
        if not mcmds:
            mcmds=list(self.cmds.keys())
            mcmds.sort(reverse=False)
        if not cmd:
            return mcmds[0]
        elif arg1==None:
            tmp=False
            for each in mcmds:
                if each==cmd:
                    tmp=True
                elif tmp:
                    return each
            for each in mcmds:
                if each.find(cmd)==0:
                    return each
        else:
            if cmd in mcmds:
                use=self.cmds[cmd]
                obj=__import__("Plus."+use,fromlist=True)
                if hasattr(obj.Run,callBack):
                    mfunc=getattr(obj.Run,callBack)
                    tmp=mfunc(cmd,arg1,arg2)
                    if not tmp:
                        return False
                    else:
                        return cmd+" "+tmp
            return False




    def last(self,cmd,arg1,arg2):
        mcmds=list(self.cmds.keys())
        mcmds.sort(reverse=True)
        if not cmd or arg1==None:
            return self.next(cmd,arg1,arg2,mcmds)
        else:
            return self.next(cmd,arg1,arg2,mcmds,"last")


class Run:
    commands=["man"]
    introduction="""
    man
        获取说明书
    man 命令
        获取单个命令的说明
    """
    @staticmethod
    def run(command,arg1,arg2):
        if arg1==None:
            intro=""
            with open(Config.getIntroSrc(),"r",encoding=Config.getFile()["encoding"]) as file:
                for each in file:
                    intro+=each
            Listeners.putInput(intro)
        elif arg1 in Runcmd().cmds:
            use=Runcmd().cmds[arg1]
            obj = __import__("Plus." + use, fromlist=True)
            intro=None
            if hasattr(obj.Run,"introduction"):
                intro=obj.Run.introduction
            else:
                intro="Sorry,没有关于这个命令的介绍"

            Listeners.putInput(intro)
