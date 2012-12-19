"""
	Entry point for NWRig
"""

import sys

filePath = "C:/Users/Noel/workspace/Projects/Noel Wilson/Python/NWRig"
if filePath not in sys.path:
	sys.path.append(filePath)
	
from UtilitiesPackage import mayaImport, mayaFromImport

mayaImport( "NWRigSystem" )

global NWRig
NWRig = NWRigSystem.NWRigSystem("nwRig")
