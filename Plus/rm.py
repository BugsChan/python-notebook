from MyIO import MyIO
from Listeners import Listeners
class Run:
    commands=["rm"]

    @staticmethod
    def run(command,arg1,arg2):
        try:
            MyIO.rm(arg1)
        except:
            from Config import Config
            Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
            return True