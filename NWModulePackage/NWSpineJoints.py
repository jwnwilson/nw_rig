"""
    Requires that Module class is sourced
"""

try:
        import NWModule
except ImportError:
        print "Error"
        
import maya.cmds as cmds
import NWUtilitiesPackage.NWUtilities as util

class NWSpineJoints(NWModule.NWModule):
        """
            Creates a joint chain can be used for spine
        """
        def initialize(self):
            # store variables in container
            util.storeString(self.container, "type", "NWSpineJoints")
        @NWModule.startPrePost
        def start(self,**kwargs):
                """
                    Creates a joint chain can be used for spine
                """
                
                # create registries
                self.createRegistry("regStartTransform")
                self.createRegistry("regStartShape")
                
                #create module top group
                rootGrp = cmds.group( n = (self.name + "Start_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "StartJoint_GRP"), em = True, p = rootGrp )
                
                # create starters
                spineChain = util.createStarterChain( (self.name + "SpineChainStarter"), {"chainNo": 5})
                print spineChain
                cmds.parent(spineChain[0], jointGrp)
                
                 # store joints and controls
                #self.storeStarterJoints( joints )
                #self.storeStarterControls( [base[0],middle[0],end[0]] )
                
                # register Starters
                self.registerObjects((spineChain), "regStartTransform")
                #self.registerObject(objects, "regStartShape")
                
        @NWModule.buildPrePost
        def build(self,**kwargs):
                pass
                # check for module container
                
                #cmds.ikHandle()

                #self.buildComplete()
                
