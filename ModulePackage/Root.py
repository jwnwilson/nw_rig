"""Requires that Module class is sourced"""

try:
        import Module
except ImportError:
        print "Error"

import maya.cmds as cmds
# old Utility functions
import UtilitiesPackage
import UtilitiesPackage.Util as Util
exec Util.importUtilities()
# new Utility functions

class Root(Module.Module):
        """
            Creates a root module and heirarchy for other modules to connect to
        """
        def initialize(self):
            # store variables in container
            Util.storeString(self.container, "type", "Root")
        @Module.blueprintPrePost
        def blueprint(self,**kwargs):
             modulesGrp = cmds.group( n = ("modules_GRP"), em = True , p=  self.rootGrp)
             geometryGrp = cmds.group( n = ("geometry_GRP"), em = True , p=  self.rootGrp)
             globalGrp = cmds.group( n = ("global_GRP"), em = True , p=  self.rootGrp)
             
             self.groups = {}
             self.groups["modules"] = modulesGrp
             self.groups["geometry"] = geometryGrp
             self.groups["global"] = globalGrp
             
        @Module.rigPrePost
        def rig(self,**kwargs):
            # check for module container
            pass
        def connect(self,**kwargs):
            # Get Connection data
            
            # Check both objects exists
            
            # connect objects
            pass
        def isRoot(self):
			return True

"""
Test Code
"""
if __name__ == "__main__":
        test = Root("test")
        test.blueprint()
        test.rig()
