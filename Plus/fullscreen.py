from Listeners import Listeners

class Run:
    commands=["fullscreen","max"]

    @staticmethod
    def run(command,arg1,arg2):
        root = Listeners.getInstance().root
        if arg1 != "false":
            root.attributes("-fullscreen", True)
        else:
            root.attributes("-fullscreen", False)