"""
	This file simply manages other Utility functions, for now will import all functions so 
	one namespace can call all Utility functions. Each Utility can be called from its' own
	namespace as well.
"""

import maya.cmds as cmds
from vector import *
from functools import wraps

"""# import Utilities
import File
import Attribute
import Blueprint
import Constraint
import Control
import Curve
import Joint
import Lib
import String
import Transform
import ModuleUtil

# Reload all modules
reload(File)
reload(Attribute)
reload(Blueprint)
reload(Constraint)
reload(Control)
reload(Curve)
reload(Joint)
reload(Lib)
reload(String)
reload(Transform)
reload(ModuleUtil)

# Import all functions into Util module for backward compatibility
from File import *
from Attribute import *
from Blueprint import *
from Constraint import *
from Control import *
from Curve import *
from Joint import *
from Lib import *
from String import *
from Transform import *
from ModuleUtil import *"""

# Import all utility functions into Util module it will be slow but convient I
# will need to change my project to source only necessary modules in the very near future before
# I regret it, handy for debugging purposes
import UtilitiesPackage

for module in UtilitiesPackage.__all__:
	command = (	"import " + module + "\n" + \
				"reload(" + module + ")\n" + \
				"from " + module + " import *" )
	exec command

def importUtilities():
	"""
		Will import all Utilities into module with short names
	"""
	execString =   ("import File\n"+
					"import Attribute\n"+
					"import Blueprint\n"+
					"import Constraint\n"+
					"import Control\n"+
					"import Curve\n"+
					"import Joint\n"+
					"import Lib\n"+
					"import String\n"+
					"import Transform")
	
	return execString

