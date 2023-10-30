from tkinter import *
from Config import Config
from Listeners import *

import ctypes

class ui:
    root=None
    text=None
    entry=None
    def __init__(self):
        self.root=Tk()

        # 适配高分屏
        # 暂时不用，会导致窗口大小变化、汉语输入字体大小变化
        # ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # self.root.tk.call('tk', 'scaling', ScaleFactor/75)

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

        # 滚动条
        if Config.getUI()["scrollbar"]:
            scrollbar = Scrollbar(self.root)
            scrollbar.pack(side="right", fill="y")

        self.text=Text(self.root,textOption)
        self.text.pack(fill="both",expand="yes")
        if Config.getUI()["scrollbar"]:
            scrollbar.config(command=self.text.yview)

        font_conf=Config.getInputConf()["font"]
        font_conf+=" "+Config.getLength(Config.getFontStyle()["size"],True)
        if Config.getFontStyle()["bold"]:
            font_conf+=" bold"
        if Config.getFontStyle()["italic"]:
            font_conf+=" italic"

        self.text.config(font=font_conf)
        self.entry.config(font=font_conf)

        Listeners(self.root, self.text, self.entry)
        self.entry.bind("<Key-Return>", Listeners.entry_Return)
        self.entry.bind("<Key-i>",Listeners.start_insert)
        self.entry.bind("<Key-I>", Listeners.start_insert)
        self.text.bind("<FocusIn>", Listeners.input_focus)
        self.text.bind("<Escape>",Listeners.command_mod)
        self.text.bind("<Key-Return>",Listeners.newLine)
        self.entry.bind("<FocusIn>",Listeners.command_focus)
        self.entry.bind("<Tab>",Listeners.conplement)
        self.entry.bind("<Key-Up>",Listeners.conplement)
        self.entry.bind("<Key-Down>",Listeners.conplement)

        self.root.mainloop()



if __name__=='__main__':
    print(Config.getWidth()
           +"x"+Config.getHeight()
           +"+"+Config.getX()
           +"+"+Config.getY())

    my_ui=ui()
    #my_ui.dumpTest()
