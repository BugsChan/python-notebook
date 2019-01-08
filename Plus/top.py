from Listeners import Listeners

class Run:
    commands=["top"]
    introduction="""
    top
        top
            -置顶
        top false
            -取消置顶
    """

    @staticmethod
    def run(command,arg1,arg2):
        root = Listeners.getInstance().root
        if arg1 != "false":
            root.attributes('-topmost', True)
        else:
            root.attributes('-topmost', False)

    @staticmethod
    def complete(cmd,arg1,arg2):
        arg1=arg1.lower()
        if "true".find(arg1)==0:
            return "-true"
        else:
            return "-false"

    @staticmethod
    def next(cmd, arg1, arg2):
        if "t" in arg1:
            return "-false"
        else:
            return "-true"

    #last is a function as same as function next
    last=next
