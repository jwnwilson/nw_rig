"""
    Requires that Module class is sourced
"""

try:
        import Module
except ImportError:
        print "Error"

import maya.cmds as cmds
import UtilitiesPackage as Util

from Module import ModuleAttribute

class HingeJoints(Module.Module):
        """
            Creates a hinge joints for arms and leg type joints
        """
        #static variables
        blueprintAttributes = {"Joint number":ModuleAttribute("Joint number", "int", 4)}
        rigAttributes = {"Joint number":ModuleAttribute("Joint number", "int", 4)}
        
        def initialize(self):
                # store variables in container
                Util.storeString(self.container, "type", "HingeJoints")
        @Module.blueprintPrePost
        def blueprint(self,**kwargs):
                'Creates a hinge joint can be used for arms or legs'
                # Variables
        	rootGrp = self.groups['blueprint_root'] 
		jointGrp = self.groups['blueprint_joint'] 
		
                # create blueprinters
                baseData = Util.createBlueprinter((self.name + "BaseBlueprinter"), {"shape":"sphere", "size": 0.5})
                middleData = Util.createBlueprinter((self.name + "MiddleBlueprinter"), {})
                endData  = Util.createBlueprinter((self.name + "EndBlueprinter"), {"shape":"sphere", "size": 0.5})
                
                base = baseData["sctl"]
                middle = middleData["sctl"]
                end = endData["sctl"]
                
                # manage blueprinter joints
                cmds.parent(endData["jnt"], middleData["jnt"])
                cmds.parent(middleData["jnt"], baseData["jnt"])
                cmds.parent(baseData["jnt"], jointGrp)
                
                joints = [baseData["jnt"],middleData["jnt"], endData["jnt"]]
                
                # create arrow ctls
                args = {"shape":"arrow", "size":0.5}
                blueprinterArrowData = Util.createBlueprinter( (self.name + "Direction"), args )
                blueprinterArrow = blueprinterArrowData["sctl"]
                cmds.rotate( 0, 90, 0 , blueprinterArrow[1])
                args = {"shape":"arrow", "size":0.5}
                
                # create axis control
                axisCtlData = Util.createAxisContols((self.name + "axisCtl"), args )
                axisCtlGrp = axisCtlData["grp"]
                
                # create constraints   
                baseEndConst = Util.constrain(end[0], base[0], axisCtlGrp[0], args={ "t":1, "name":(self.name + "BaseEndConst" )} )
                baseEndAimConst = cmds.aimConstraint(base[0], axisCtlGrp[0], n = (self.name + "BaseEndConst" + "_AIM") )
                arrowEndConst = Util.constrain(base[0], blueprinterArrow[1], args={ "t":1, "name":(self.name + "ArrowConst")} )
                arrowAimConst = cmds.aimConstraint(end[0], blueprinterArrow[1], n = (self.name + "ArrowConst" + "_AIM") )
                
                Util.lockHide(base[0], {"s":1,"v":1, "l":1, "h":1})
                Util.lockHide(middle[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                Util.lockHide(end[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                
                cmds.parent(end[1], base[0])
                cmds.parent(middle[1], axisCtlGrp[1] )
                cmds.parent(axisCtlGrp[0],base[0] )
                cmds.parent(base[1], rootGrp,)
                cmds.parent(blueprinterArrow[1], rootGrp)
                #cmds.parent(jointGrp, rootGrp)
                
                cmds.move(0, 0, 0, base[1])
                cmds.move(0, 0, 2, end[1])
                
                cmds.parent(rootGrp, self.rootGrp)
                
                # store joints and controls
                self.storeBlueprinterJoints( joints )
                self.storeBlueprinterControls( [base[0],middle[0],end[0]] )
                
                # register Blueprinters
                self.registerObjects((base + middle + end + axisCtlData["xctl"] +
                		      axisCtlData["yctl"] + axisCtlData["zctl"]), 
                	 	      "regBlueprintTransform")
                #self.registerObject(objects, "regBlueprintShape")
                
        @Module.rigPrePost
        def rig(self,**kwargs):
        	# Variables
        	rootGrp = self.groups['rig_root'] 
		jointGrp = self.groups['rig_joint'] 
		setupGrp = self.groups['rig_setup'] 
		contorlGrp = self.groups['rig_control'] 
		
                # Get rig joints created from blueprint
                joints = self.getRigJoints()
                
                if len(joints) > 3:
                    cmds.error("Too many joints in: " + self.name + "!")
                
                # Create ikHandle
                polePosition = Util.getPolePosition(joints, 3)
                handleData = Util.createIkHandle(self.name, joints)
                poleData =  Util.createPoleVec(joints, handleData["IK"], polePosition)
                
                cmds.parent(handleData["IK"], setupGrp)
                cmds.parent(poleData, setupGrp)
                
                # Create controls for handle
                baseCtl = Util.createControl( (self.name  + "Base"), {} )
                ikCtl = Util.createControl( (self.name  + "IK"), {"shape":"locator"} )
                poleCtl = Util.createControl( (self.name  + "Pole"), {"shape":"locator"} )
                
                args = {"all" : 1, "mo" : 0}
                Util.match(baseCtl[1], joints[0], args)
                Util.match(ikCtl[1], joints[2], args)
                Util.match(poleCtl[1], poleData, args)
                
                Util.constrain(baseCtl[0], ikCtl[1], args={ "all":1, "mo":1, "name":(self.name + "IK")} )
                Util.constrain(baseCtl[0], poleCtl[1], args={ "all":1, "mo":1, "name":(self.name + "IK")} )
                
                baseConst = Util.constrain(baseCtl[0], joints[0], args={ "all":1, "name":(self.name + "Pole")} )
                middleConst =Util.constrain(ikCtl[0], handleData["IK"], args={ "all":1, "name":(self.name + "IK")} )
                poleConst = Util.constrain(poleCtl[0], poleData, args={ "all":1, "name":(self.name + "Pole")} )
                
                cmds.parent(baseCtl[1], ikCtl[1], poleCtl[1], controlGrp)
                cmds.parent(rootGrp, rootGrp)
                
                # register Rigs
                self.registerObjects([baseCtl[0]], "regRigTransform")
                #self.registerObjects(objects, "regRigShape")
                
                # store outputs
		self.storeOutput(baseCtl[0],"rootControl")
			
        def connect(self,**kwargs):
                # Get Connection data
                
                # Check both objects exists
                
                # connect objects
                pass

"""
Test Code
"""
if __name__ == "__main__":
        test = HingeJoints("test")
        test.blueprint()
        test.rig()
