from Listeners import Listeners

class Run:
	commands=["clear"]
	introduction="""清除写入面板的所有内容"""

	@staticmethod
	def run(cmd,arg1,arg2):
		Listeners.putInput("")
