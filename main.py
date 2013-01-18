"""
	Entry point for NWRig
"""
import sys
filePath = "C:/Users/Noel/workspace/Projects/Noel Wilson/Python/NWRig"
if filePath not in sys.path:
	sys.path.append(filePath)
	
import maya.cmds as cmds
import RigSystem.NWRigSystem
reload(RigSystem.NWRigSystem)

	
from UtilitiesPackage.File import mayaImport, mayaFromImport
from RigSystem.NWRigSystem import NWRigSystem
mayaImport( "NWRigSystem" )

global NWRig
NWRig = NWRigSystem("nwRig")
