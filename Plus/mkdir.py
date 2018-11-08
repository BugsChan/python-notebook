from MyIO import MyIO
class Run:
    commands=["mkdir"]
    introduction="""
    mkdir 文件夹名
        -创建一个文件夹
    """

    @staticmethod
    def run(command,arg1,arg2):
        MyIO.mkdir(arg1)