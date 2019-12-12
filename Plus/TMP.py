from Listeners import Listeners
from Config import *

class Run:
	commands=["tmp"]
	introduction="""
    tmp -s
	tmp -save
		存储内容到暂存区
	tmp -r
	tmp -read
	tmp -w
	tmp -write
		读取内容
    """
	src = "tmps/.tmp"
	
	@staticmethod
	def run(cmd, arg1, arg2):
		if arg1 == "r" or arg1 == "read":
			ans = ""
			with open(Run.src, "r", encoding="UTF-8") as file:
				for each in file:
					ans += each
			Listeners.putInput(ans)
		elif arg1 == "s" or arg1 == "save" or arg1 == "w" or arg1 == "write":
			with open(Run.src, "w", encoding="UTF-8") as file:
				file.write(Listeners.getInput())
		else:
			Listeners.getInstance().entry["background"] = Config.getUI()["alert_color"]
			return True
		