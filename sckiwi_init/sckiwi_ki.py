import seiscomp3.Kernel, sys, os, subprocess
# The path to the Source_Analysis file
file_path = '/home/alireza/seiscomp3/sckiwi/Source_Analysis'


Main_Sc = file_path.split ('/')[-1]

class Module (seiscomp3.Kernel.Module):
	def __init__ (self, env):
		seiscomp3.Kernel.Module.__init__(self, env, env.moduleName (__file__))	
		
	def _run (self):	
		if os.path.exists(file_path):
			params = {}
			params = self.env.lockFile (self.name)
			params += " " + "bash %s" % file_path
			self.env.start (self.name, "run_with_lock", params, True)		
		else:
			message = 'The main script < %s > is missing. check SEISCOMP_HOME/sckiwi directory' % (Main_Sc)
			print (message)	
	
