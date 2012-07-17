"""
    Requires that Module class is sourced
"""

try:
        import NWModule
except ImportError:
        print "Error"

import maya.cmds as cmds
import NWUtilitiesPackage.NWUtilities as util
        

class NWHingeJoints(NWModule.NWModule):
        """
            Creates a hinge joints for arms and leg type joints
        """
        def initialize(self):
                # store variables in container
                util.storeString(self.container, "type", "NWHingeJoints")
        @NWModule.startPrePost
        def start(self,**kwargs):
                'Creates a hinge joint can be used for arms or legs'
                # create registries
                self.createRegistry("regStartTransform")
                self.createRegistry("regStartShape")
                
                # create Base Groups
                rootGrp = cmds.group( n = (self.name + "Start_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "StartJoint_GRP"), em = True, p = rootGrp )
                
                # create starters
                baseData = util.createStarter((self.name + "BaseStarter"), {"shape":"sphere", "size": 0.5})
                middleData = util.createStarter((self.name + "MiddleStarter"), {})
                endData  = util.createStarter((self.name + "EndStarter"), {"shape":"sphere", "size": 0.5})
                
                base = baseData["sctl"]
                middle = middleData["sctl"]
                end = endData["sctl"]
                
                # manage starter joints
                cmds.parent(endData["jnt"], middleData["jnt"])
                cmds.parent(middleData["jnt"], baseData["jnt"])
                cmds.parent(baseData["jnt"], jointGrp)
                
                joints = [baseData["jnt"],middleData["jnt"], endData["jnt"]]
                
                # create arrow ctls
                args = {"shape":"arrow", "size":0.5}
                starterArrowData = util.createStarter( (self.name + "Direction"), args )
                starterArrow = starterArrowData["sctl"]
                cmds.rotate( 0, 90, 0 , starterArrow[1])
                args = {"shape":"arrow", "size":0.5}
                
                # create axis control
                axisCtlData = util.createAxisContols((self.name + "axisCtl"), args )
                axisCtlGrp = axisCtlData["grp"]
                
                # create constraints   
                baseEndConst = util.constrain(end[0], base[0], axisCtlGrp[0], args={ "t":1, "name":(self.name + "BaseEndConst" )} )
                baseEndAimConst = cmds.aimConstraint(base[0], axisCtlGrp[0], n = (self.name + "BaseEndConst" + "_AIM") )
                arrowEndConst = util.constrain(base[0], starterArrow[1], args={ "t":1, "name":(self.name + "ArrowConst")} )
                arrowAimConst = cmds.aimConstraint(end[0], starterArrow[1], n = (self.name + "ArrowConst" + "_AIM") )
                
                util.lockHide(base[0], {"s":1,"v":1, "l":1, "h":1})
                util.lockHide(middle[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                util.lockHide(end[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                
                cmds.parent(end[1], base[0])
                cmds.parent(middle[1], axisCtlGrp[1] )
                cmds.parent(axisCtlGrp[0],base[0] )
                cmds.parent(base[1], rootGrp,)
                cmds.parent(starterArrow[1], rootGrp)
                #cmds.parent(jointGrp, rootGrp)
                
                cmds.move(0, 0, 0, base[1])
                cmds.move(0, 0, 2, end[1])
                
                cmds.parent(rootGrp, self.rootGrp)
                
                # store joints and controls
                self.storeStarterJoints( joints )
                self.storeStarterControls( [base[0],middle[0],end[0]] )
                
                # register Starters
                self.registerObjects((base + middle + end + axisCtlData["xctl"] +
                		      axisCtlData["yctl"] + axisCtlData["zctl"]), 
                	 	      "regStartTransform")
                #self.registerObject(objects, "regStartShape")
                
        @NWModule.buildPrePost
        def build(self,**kwargs):
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
                
                if len(joints) > 3:
                    cmds.error("Too many joints in: " + self.name + "!")
                # Hide starters joints
                cmds.setAttr((self.name + "Start_GRP" + ".v"), 0)
                
                # Create ikHandle
                polePosition = util.getPolePosition(joints, 3)
                handleData = util.createIkHandle(self.name, joints)
                poleData =  util.createPoleVec(joints, handleData["IK"], polePosition)
                
                cmds.parent(handleData["IK"], setupGrp)
                cmds.parent(poleData, setupGrp)
                
                # Create controls for handle
                baseCtl = util.createControl( (self.name  + "Base"), {} )
                ikCtl = util.createControl( (self.name  + "IK"), {"shape":"locator"} )
                poleCtl = util.createControl( (self.name  + "Pole"), {"shape":"locator"} )
                
                args = {"all" : 1, "mo" : 0}
                util.match(baseCtl[1], joints[0], args)
                util.match(ikCtl[1], joints[2], args)
                util.match(poleCtl[1], poleData, args)
                
                util.constrain(baseCtl[0], ikCtl[1], args={ "all":1, "mo":1, "name":(self.name + "IK")} )
                util.constrain(baseCtl[0], poleCtl[1], args={ "all":1, "mo":1, "name":(self.name + "IK")} )
                
                baseConst = util.constrain(baseCtl[0], joints[0], args={ "all":1, "name":(self.name + "Pole")} )
                middleConst =util.constrain(ikCtl[0], handleData["IK"], args={ "all":1, "name":(self.name + "IK")} )
                poleConst = util.constrain(poleCtl[0], poleData, args={ "all":1, "name":(self.name + "Pole")} )
                
                cmds.parent(baseCtl[1], ikCtl[1], poleCtl[1], controlGrp)
                cmds.parent(rootGrp, self.rootGrp)
                
                # register Builds
                self.registerObjects((baseCtl + ikCtl + poleCtl), "regBuildTransform")
                #self.registerObjects(objects, "regBuildShape")
        def connect(self,**kwargs):
                # Get Connection data
                
                # Check both objects exists
                
                # connect objects
                pass

"""
Test Code
"""
if __name__ == "__main__":
        test = NWHingeJoints("test")
        test.start()
        test.build()
