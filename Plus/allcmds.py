from Listeners import Listeners
from Plus.Interface import Runcmd

class Run:
	commands=["allcmds"]
	
	@staticmethod
	def run(cmd,arg1,arg2):
		cmds=str(Runcmd().cmds)
		cmds=cmds.replace("{","").replace("}",".py").replace(",",".py\n")
		cmds=cmds.replace("'","")
		cmds="command file\n"+cmds
		Listeners.putInput(cmds)
