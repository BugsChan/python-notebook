from tkinter import *
from Config import Config
from Listeners import *

class ui:
    root=None
    text=None
    entry=None
    def __init__(self):
        self.root=Tk()

        self.root.title(Config.getTitle())

        self.root.geometry(Config.getWidth()
                           +"x"+Config.getHeight()
                           +"+"+Config.getX()
                           +"+"+Config.getY())

        self.root.resizable(Config.getResizable("x")
                            ,Config.getResizable("y"))

        if Config.fullScreen():
            self.root.attributes("-fullscreen", True)

        if Config.alwaysOnTop():
            self.root.attributes('-topmost', True)

        textOption=Config.getInputConf()
        entryOption=Config.getCommandConf()

        self.entry=Entry(self.root,entryOption)
        self.entry.pack(fill="x",side="bottom")

        self.text=Text(self.root,textOption)
        self.text.pack(fill="both",expand="yes")

        font_conf=Config.getInputConf()["font"]
        font_conf+=" "+Config.getLength(Config.getFontStyle()["size"],True)
        if Config.getFontStyle()["bold"]:
            font_conf+=" bold"
        if Config.getFontStyle()["italic"]:
            font_conf+=" italic"
        print(font_conf)
        self.text.config(font=font_conf)
        self.entry.config(font=font_conf)

        Listeners(self.root, self.text, self.entry)
        self.entry.bind("<Key-Return>", Listeners.entry_Return)
        self.entry.bind("<Key-i>",Listeners.start_insert)
        self.entry.bind("<Key-I>", Listeners.start_insert)
        self.text.bind("<FocusIn>", Listeners.input_focus)
        self.text.bind("<Escape>",Listeners.command_mod)
        self.entry.bind("<FocusIn>",Listeners.command_focus)

        self.root.mainloop()



if __name__=='__main__':
    print(Config.getWidth()
           +"x"+Config.getHeight()
           +"+"+Config.getX()
           +"+"+Config.getY())

    my_ui=ui()
    #my_ui.dumpTest()


