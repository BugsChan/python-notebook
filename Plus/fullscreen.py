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