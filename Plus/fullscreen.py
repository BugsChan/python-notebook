from Listeners import Listeners

class Run:
    commands=["fullscreen","max"]
    introduction="""
    fullscreen(max)
        fullscreen
            -全屏
        fullscreen false
            -取消全屏
    """

    @staticmethod
    def run(command,arg1,arg2):
        root = Listeners.getInstance().root
        if arg1 != "false":
            root.attributes("-fullscreen", True)
        else:
            root.attributes("-fullscreen", False)

    @staticmethod
    def complete(cmd, arg1, arg2):
        arg1 = arg1.lower()
        if "true".find(arg1) == 0:
            return "-true"
        else:
            return "-false"

    @staticmethod
    def next(cmd,arg1,arg2):
        if "t" in arg1:
            return "-false"
        else:
            return "-true"

    #last is a function but same to function next
    last=next