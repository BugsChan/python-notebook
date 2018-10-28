from MyIO import MyIO
class Run:
    commands=["mkdir"]

    @staticmethod
    def run(command,arg1,arg2):
        MyIO.mkdir(arg1)