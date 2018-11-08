from Listeners import Listeners
from Plus.Interface import Runcmd

class Run:
	commands=["allcmds"]
	introduction="""
	显示所有命令及所对应的py文件
	"""

	@staticmethod
	def run(cmd,arg1,arg2):
		cmds=str(Runcmd().cmds)
		cmds=cmds.replace("{","").replace("}",".py").replace(",",".py\n")
		cmds=cmds.replace("'","")
		cmds="command file\n"+cmds
		Listeners.putInput(cmds)
