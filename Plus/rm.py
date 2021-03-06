from MyIO import MyIO
from Listeners import Listeners
class Run:
    commands=["rm"]

    introduction="""
    rm 文件名
        -删除该文件或文件夹
    rm --bytitle title or rm -t title
        -删除该title
    """

    @staticmethod
    def run(command,arg1,arg2):
        if arg1=='bytitle' or arg1=='t':
            from Plus.rmBytitle import Run
            Run.run(None,arg2,None)
            return False
        try:
            MyIO.rm(arg1)
        except:
            from Config import Config
            Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
            return True