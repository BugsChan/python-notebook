from Listeners import Listeners

class Run:
    commands=["top"]

    @staticmethod
    def run(command,arg1,arg2):
        root = Listeners.getInstance().root
        if arg1 != "false":
            root.attributes('-topmost', True)
        else:
            root.attributes('-topmost', False)
