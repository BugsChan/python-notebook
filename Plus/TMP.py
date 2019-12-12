from Listeners import Listeners

class Run:
	commands=["tmp"]
	introduction="""
    tmp -s
	tmp -save
		存储内容到暂存区
	tmp -r
	tmp -read
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
			print("text %s", ans)
			Listeners.putInput(ans)
		else:
			with open(Run.src, "w", encoding="UTF-8") as file:
				file.write(Listeners.getInput())
		