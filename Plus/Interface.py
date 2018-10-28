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
            return obj.Run.run(command,*args)
        else:
            return False


class Run:
    commands=["man"]
    @staticmethod
    def run(command,arg1,arg2):
        intro=""
        with open(Config.getIntroSrc(),"r",encoding=Config.getFile()["encoding"]) as file:
            for each in file:
                intro+=each
        Listeners.putInput(intro)
