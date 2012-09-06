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


