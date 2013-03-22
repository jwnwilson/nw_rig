"""
    Requires that Module class is sourced
"""

try:
        import Module
except ImportError:
        print "Error"
        
import maya.cmds as cmds
import UtilitiesPackage as Util

# new Utility functions
from Module import ModuleAttribute

class SpineJoints(Module.Module):
        """
            Creates a joint chain can be used for spine
        """
        #static variables
        blueprintAttributes = {"Joint number":ModuleAttribute("Joint number", "int", 4)}
        rigAttributes = {"Joint number":ModuleAttribute("Joint number", "int", 4)}
        
        def initialize(self):
            # store variables in container
            Util.storeString(self.container, "type", "SpineJoints")
        @Module.blueprintPrePost
        def blueprint(self,**kwargs):
			"""
				Creates a joint chain can be used for spine
			"""
			# Variables
			rootGrp = self.groups['blueprint_root'] 
			jointGrp = self.groups['blueprint_joint'] 
			
			# get blueprint attributes
			jointNo= int(self.blueprintAttributes["Joint number"].value)
			
			# create blueprinters
			spineChainData = Util.createBlueprinterChain( (self.name + "SpineChainBlueprinter"), {"chainNo": jointNo})
			spineChainJoints = spineChainData["jnt"]
			spineChainSctls = spineChainData["sctl"]
			
			cmds.parent(spineChainJoints[0], jointGrp)
			cmds.parent(spineChainData["root"], rootGrp)
			
			cmds.parent(rootGrp, self.rootGrp)
			
			# store joints and controls
			self.storeBlueprinterJoints( spineChainJoints )
			self.storeBlueprinterControls( spineChainSctls )
			
			# register Blueprinters
			self.registerObjects(Util.createSingleArray(spineChainSctls), "regBlueprintTransform")
			#self.registerObject(objects, "regBlueprintShape")
                
        @Module.rigPrePost
        def rig(self,**kwargs):
			# Variables
			clusterCtls = []
			rootGrp = self.groups['rig_root'] 
			jointGrp = self.groups['rig_joint'] 
			setupGrp = self.groups['rig_setup'] 
			contorlGrp = self.groups['rig_control'] 
			
			# Get rig joints created from blueprint
			joints = self.getRigJoints()
			
			#cmds.ikHandle()
			handleData = Util.createSplineIk(self.name, joints, sol= "ikSplineSolver")
			clusterList = Util.clusterizeCurve( handleData["CRV"] )
			
			cmds.parent(handleData["IK"], setupGrp)
			
			#create controls
			for cluster in clusterList:
				clusterName = Util.removeSuffix( cluster[0] )
				clusterCtl = Util.createControl( clusterName, {"match":cluster[0]}  )
				
				cmds.parent(cluster[1], clusterCtl[0] )
				cmds.parent(clusterCtl[1], controlGrp )
				clusterCtls.append(clusterCtl)
				
			# parent controls
			for x in range(1,  len(clusterCtls) ):
				cmds.parent( clusterCtls[x][1], clusterCtls[x-1][0] )
			cmds.parent(rootGrp, self.rootGrp)
			
			# store outputs
			self.storeOutput(clusterCtls[0][0],"rootControl")
			#self.storeOutput(clusterCtls[3][0],"endControl")
			
			# register Rigs
			for clusterCtl in clusterCtls:
				self.registerObjects(clusterCtl, "regRigTransform")
"""
Test Code
"""
if __name__ == "__main__":
        test = SpineJoints("test")
        test.blueprint()
        test.rig()
                
