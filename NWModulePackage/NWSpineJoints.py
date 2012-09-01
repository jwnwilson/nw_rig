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
        @NWModule.blueprintPrePost
        def blueprint(self,**kwargs):
                """
                    Creates a joint chain can be used for spine
                """
                
                # create registries
                self.createRegistry("regBlueprintTransform")
                self.createRegistry("regBlueprintShape")
                
                #create module top group
                rootGrp = cmds.group( n = (self.name + "Blueprint_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "BlueprintJoint_GRP"), em = True, p = rootGrp )
                
                # create blueprinters
                spineChainData = util.createBlueprinterChain( (self.name + "SpineChainBlueprinter"), {"chainNo": 5})
                spineChainJoints = spineChainData["jnt"]
                spineChainSctls = spineChainData["sctl"]
                print spineChainSctls
                cmds.parent(spineChainJoints[0], jointGrp)
                cmds.parent(spineChainSctls[0][1], rootGrp)
                
                cmds.parent(rootGrp, self.rootGrp)
                
                # store joints and controls
                self.storeBlueprinterJoints( spineChainJoints )
                self.storeBlueprinterControls( spineChainSctls )
                
                # register Blueprinters
                self.registerObjects(util.createSingleArray(spineChainSctls), "regBlueprintTransform")
                #self.registerObject(objects, "regBlueprintShape")
                
        @NWModule.rigPrePost
        def rig(self,**kwargs):
        	# Variables
        	clusterCtls = []
        	
                # create registries
                self.createRegistry("regRigTransform")
                self.createRegistry("regRigShape")
                
                # Check for module container
                rootGrp = cmds.group( n = (self.name + "Rig_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True, p= rootGrp)
                setupGrp = cmds.group( n = (self.name + "Setup_GRP"), em = True, p= rootGrp)
                controlGrp = cmds.group( n = (self.name + "Control_GRP"), em = True, p= rootGrp)
                
                # Get blueprinter joints
                blueprinters  = self.getBlueprinterJoints()
                for joint in blueprinters:
                    if cmds.objExists(joint) == False:
                        cmds.error(joint + " not found!")
                
                # Duplicate joints
                joints = util.duplicateChain( self.name , blueprinters)
                cmds.parent(joints[0],jointGrp)
                
                # Hide blueprinters joints
                cmds.setAttr((self.name + "Blueprint_GRP" + ".v"), 0)
                
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
                
                # store outputs
                self.storeOutput(clusterCtls[3][0],"endControl")
                
                # register Rigs
                #self.registerObjects((baseCtl + ikCtl + poleCtl), "regRigTransform")
"""
Test Code
"""
if __name__ == "__main__":
        test = NWSpineJoints("test")
        test.blueprint()
        test.rig()
                
