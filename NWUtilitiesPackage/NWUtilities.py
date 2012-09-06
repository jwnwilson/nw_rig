"""
	This needs to be turned into a meta file that will manage the other utility files
"""

import maya.cmds as cmds
from vector import *
from functools import wraps

# import utilities
import NWUtilitiesFile
import NWUtilitiesAttribute
import NWUtilitiesBlueprint
import NWUtilitiesConstraint
import NWUtilitiesControl
import NWUtilitiesCurve
import NWUtilitiesJoint
import NWUtilitiesLib
import NWUtilitiesString
import NWUtilitiesTransform

# Reload all modules
reload(NWUtilitiesFile)
reload(NWUtilitiesAttribute)
reload(NWUtilitiesBlueprint)
reload(NWUtilitiesConstraint)
reload(NWUtilitiesControl)
reload(NWUtilitiesCurve)
reload(NWUtilitiesJoint)
reload(NWUtilitiesLib)
reload(NWUtilitiesString)
reload(NWUtilitiesTransform)

# Import all functions into utilities module for backward compatibility
from NWUtilitiesFile import *
from NWUtilitiesAttribute import *
from NWUtilitiesBlueprint import *
from NWUtilitiesConstraint import *
from NWUtilitiesControl import *
from NWUtilitiesCurve import *
from NWUtilitiesJoint import *
from NWUtilitiesLib import *
from NWUtilitiesString import *
from NWUtilitiesTransform import *

def importUtilitiesShortNames():
	"""
		Will import all utilities into module with short names
	"""
	execString =   ("import NWUtilitiesFile as fileUtil\n"+
					"import NWUtilitiesAttribute as attr\n"+
					"import NWUtilitiesBlueprint as blueprint\n"+
					"import NWUtilitiesConstraint as constraint\n"+
					"import NWUtilitiesControl as control\n"+
					"import NWUtilitiesCurve as curve\n"+
					"import NWUtilitiesJoint as joint\n"+
					"import NWUtilitiesLib as lib\n"+
					"import NWUtilitiesString as string\n"+
					"import NWUtilitiesTransform as transform")
	
	return execString

