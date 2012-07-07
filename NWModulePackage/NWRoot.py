"""Requires that Module class is sourced"""

try:
        import NWModule
except ImportError:
        print "Error"

import maya.cmds as cmds
import NWUtilitiesPackage.NWUtilities as util
        

class NWRoot(NWModule.NWModule):
        """
            Creates a root module and heirarchy for other modules to connect to
        """
        def initialize(self):
            # store variables in container
            util.storeString(self.container, "type", "NWRoot")
        @NWModule.startPrePost
        def start(self,**kwargs):
             modulesGrp = cmds.group( n = ("modules_GRP"), em = True , p=  self.rootGrp)
             geometryGrp = cmds.group( n = ("geometry_GRP"), em = True , p=  self.rootGrp)
             globalGrp = cmds.group( n = ("global_GRP"), em = True , p=  self.rootGrp)
             
             self.groups = {}
             self.groups["modules"] = modulesGrp
             self.groups["geometry"] = geometryGrp
             self.groups["global"] = globalGrp
             
        @NWModule.buildPrePost
        def build(self,**kwargs):
            # check for module container
            pass
        def connect(self,**kwargs):
            # Get Connection data
            
            # Check both objects exists
            
            # connect objects
            pass

"""
Test Code
"""
if __name__ == "__main__":
        test = NWRoot("test")
        test.start()
        test.build()
