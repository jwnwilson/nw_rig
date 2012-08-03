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
                spineChainData = util.createStarterChain( (self.name + "SpineChainStarter"), {"chainNo": 5})
                spineChainJoints = spineChainData["jnt"]
                spineChainSctls = spineChainData["sctl"]
                print spineChainSctls
                cmds.parent(spineChainJoints[0], jointGrp)
                cmds.parent(spineChainSctls[0][1], rootGrp)
                
                cmds.parent(rootGrp, self.rootGrp)
                
                # store joints and controls
                self.storeStarterJoints( spineChainJoints )
                self.storeStarterControls( spineChainSctls )
                
                # register Starters
                self.registerObjects(util.createSingleArray(spineChainSctls), "regStartTransform")
                #self.registerObject(objects, "regStartShape")
                
        @NWModule.buildPrePost
        def build(self,**kwargs):
        	# Variables
        	clusterCtls = []
        	
                # create registries
                self.createRegistry("regBuildTransform")
                self.createRegistry("regBuildShape")
                
                # Check for module container
                rootGrp = cmds.group( n = (self.name + "Build_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True, p= rootGrp)
                setupGrp = cmds.group( n = (self.name + "Setup_GRP"), em = True, p= rootGrp)
                controlGrp = cmds.group( n = (self.name + "Control_GRP"), em = True, p= rootGrp)
                
                # Get starter joints
                starters  = self.getStarterJoints()
                for joint in starters:
                    if cmds.objExists(joint) == False:
                        cmds.error(joint + " not found!")
                
                # Duplicate joints
                joints = util.duplicateChain( self.name , starters)
                cmds.parent(joints[0],jointGrp)
                
                # Hide starters joints
                cmds.setAttr((self.name + "Start_GRP" + ".v"), 0)
                
                #cmds.ikHandle()
                handleData = util.createSplineIk(self.name, joints, sol= "ikSplineSolver")
                clusterList = util.clusterizeCurve( handleData["CRV"] )
                
                cmds.parent(handleData["IK"], setupGrp)
                
                #create controls
                for cluster in clusterList:
                    clusterName = util.removeSuffix( cluster[0] )
                    clusterCtl = util.createControl( clusterName, {"match":cluster[0]}  )
                    
                    cmds.parent(cluster[1], clusterCtl[0] )
                    cmds.parent(clusterCtl[1], controlGrp )
                    clusterCtls.append(clusterCtl)
                    
                # parent controls
                for x in range(1,  len(clusterCtls) ):
                    cmds.parent( clusterCtls[x][1], clusterCtls[x-1][0] )
                cmds.parent(rootGrp, self.rootGrp)
                
                # register Builds
                #self.registerObjects((baseCtl + ikCtl + poleCtl), "regBuildTransform")
"""
Test Code
"""
if __name__ == "__main__":
        test = NWSpineJoints("test")
        test.start()
        test.build()
                
