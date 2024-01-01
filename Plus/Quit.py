from Config import *
from Listeners import Listeners
from MyIO import MyIO
from my_time import MyTime
import json

from tkinter.messagebox import showerror, askquestion

import base64
from Crypto.Cipher import AES

class MyCrypt:
    ENSUREKEY = "FUCK-XI-FORBID-COMMENTS"
    def addTo16(self, value):
        while len(value) % 16 != 0:
            value += bytes('\0', 'utf-8')
        return value

    def encrypt(self, key, value):
        aes = AES.new(self.addTo16(bytes(key, "utf-8")), AES.MODE_ECB)
        value = self.ENSUREKEY + "|" + value
        encryptedValue = aes.encrypt(self.addTo16(bytes(value, "utf-8")))
        return str(base64.encodebytes(encryptedValue), encoding="utf-8")

    def decrypt(self, key, value):
        aes = AES.new(self.addTo16(bytes(key, "utf-8")), AES.MODE_ECB)
        try:
            decodeBytes = base64.decodebytes(bytes(value, "utf-8"))
            decryptedText = str(aes.decrypt(decodeBytes), encoding="utf-8")
            if decryptedText.startswith(self.ENSUREKEY):
                return decryptedText[len(self.ENSUREKEY) + 1:]
            else:
                return False
        except Exception as e:
            return False

class Run:
    commands=[":","：","quit","exit", "save"]

    introduction="""
    save title password
    :w title password
        保存内容
        title: 标题
        password 密码(可以省略)
    :q 退出
    :wq title password
        保存并退出
    :! 强制(用于内容未保存时的强制退出)

    """

    @staticmethod
    def complete(cmd,arg1,arg2,loop=False):
        titlelist=[]
        if cmd=="alltitles":
            return False
        else:
            titles=MyIO.getInstance().alltitles()
            for each in titles:
                if each.find(arg1)==0:
                    titlelist.append(each)
            if loop:
                return list(titles.keys())
            return Listeners.getSame(titlelist)

    @staticmethod
    def next(cmd,arg1,arg2,prev=False):
        titlelist=Run.complete(cmd,arg1,arg2,True)
        if len(titlelist)==0:
            return False
        titlelist.sort(reverse=prev)
        if not arg1:
            return titlelist[0]
        else:
            tmp=False
            for each in titlelist:
                if each==arg1:
                    tmp=True
                elif tmp:
                    return each
            for each in titlelist:
                if each.find(arg1)==0:
                    return each
            return False

    @staticmethod
    def last(cmd,arg1,arg2):
        return Run.next(cmd,arg1,arg2,True)

    @staticmethod
    def run(command,*args):
        if command=="quit" or command=="exit":
            exit()

        if command == "save":
            return Run.run(":", "w", *args)

        if command in ":：" and "w" in args[0]:

            my_io = MyIO()
            wText = Listeners.getInput()
            append = False
            encrypt = False

            if my_io.filePath == Config.getSrc():
                if len(args) < 2:
                    showerror("错误", "请输入标题 (title) !")
                    Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
                    return True
                if len(args) >= 3:
                    encrypt = True
                    wText = MyCrypt().encrypt(args[2], wText)
                else:
                    my_io.write_for_linux(wText)

                if not args[1] in my_io.alltitles():
                    append = True
                    wText = my_io.to_json(args[1], wText, encrypt) + ","
                else:
                    tmp = my_io.readObj()
                    for each in tmp:
                        if each['title'] == args[1]:
                            #改密或删除密码的提醒
                            if (each["encrypt"] ^ encrypt) or ( encrypt and (not MyCrypt().decrypt(args[2], each["text"])) ):
                                if "no" == askquestion("确定", "确定要修改密码吗?"):
                                    return True
                            else:
                                if "no" == askquestion("确定", "确定要存入笔记吗?"):
                                    return True
                            each['time'] = MyTime.toString()
                            each["text"] = wText
                            each["encrypt"] = encrypt
                            break
                    wText = json.dumps(tmp, ensure_ascii=False)
                    wText = wText[1:len(wText) - 1] + ","

            my_io.write(wText, append)
            Listeners.putInput("文件已写入...")

        if "q" in args[0]:
            if "!" in args[0] or "！" in args[0] or "w" in args[0]:  # 强制退出
                exit(0)
            else:
                Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
                return True
