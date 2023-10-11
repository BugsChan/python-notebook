from Listeners import Listeners
from Plus.Interface import Runcmd

class Run:
	commands=["allcmds"]
	introduction="""
	显示所有命令及所对应的py文件
	"""

	@staticmethod
	def run(cmd,arg1,arg2):
		cmds=Runcmd().cmds
		ans = ""
		if arg1 == "s" or arg1 == "sheet":
			model_gap = "+" + "-" * 15 + "+" + "-" * 15 + "+" + "\n"
			ans = model_gap
			ans += "|{0:^15}|{1:^15}|\n".format("COMMAND", "FILE")
			ans += model_gap
			for each in cmds:
				ans += "|{0:^15}|{1:^15}|\n".format(each, cmds[each] + ".py")
				ans += model_gap
		else:
			ans = "COMMAND\t\tFILE\n"
			for each in cmds:
				ans += each + "\t\t" + cmds[each] + ".py" + "\n"

		Listeners.putInput(ans)
