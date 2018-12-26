import Plus.cmd as cmd

class Run:
    commands=["restart"]

    @staticmethod
    def run(*args):
        import platform
        myos=platform.platform()
        if "windows" in myos.lower():
            cmd.Run.run("cmd","python","UI.py")
        else:
            cmd.Run.run("cmd","python3","UI.py")
        exit(0)