"""Requires that Module class is sourced"""

try:
        import NWModule
except ImportError:
        print "Error"

import maya.cmds as cmds
import NWUtilitiesPackage.NWUtilities as util
        

class NWHingeJoints(NWModule.NWModule):
        'Creates a hinge joints for arms and leg type joints' 
        def initialize(self):
            # store variables in container
            util.storeString(self.container, "type", "NWHingeJoints")
        @NWModule.startPrePost
        def start(self,**kwargs):
                'Creates a hinge joint can be used for arms or legs'
                #create container to store all module variables
                
                rootGrp = cmds.group( n = (self.name + "Start_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "StartJoint_GRP"), em = True )
                
                # create starters
                base = util.createStarter((self.name + "Base"), {"shape":"sphere", "size": 0.5})
                middle = util.createStarter((self.name + "Middle"), {})
                end  = util.createStarter((self.name + "End"), {"shape":"sphere", "size": 0.5})
                
                # manage starter joints
                joints = [base[2], middle[2],end[2]]
                cmds.parent(joints[2], joints[1])
                cmds.parent(joints[1], joints[0])
                cmds.parent(joints[0], jointGrp)
                
                # create arrow ctls
                args = {"shape":"arrow", "size":0.5}
                starterArrow = util.createControl( (self.name + "Direction"), args )
                cmds.rotate( 0, 90, 0 , starterArrow[1])
                args = {"shape":"arrow", "size":0.5}
                
                # create axis control
                axisCtl = util.createAxisContols((self.name + "axisCtl"), args )
                
                # create constraints                
                #baseConst = util.constrain(base[0], joints[0],{ "t":1, "name":(self.name + "BaseConst" ) })
                #endConst =util.constrain(end[0], joints[2], { "t":1, "name":(self.name + "EndConst") })
                #middleConst =util.constrain(middle[0], joints[1], { "t":1, "name":(self.name + "MiddleConst")} )
                baseEndConst = util.constrain(end[0], base[0], axisCtl[0], args={ "t":1, "name":(self.name + "BaseEndConst" )} )
                baseEndAimConst = cmds.aimConstraint(base[0], axisCtl[0], n = (self.name + "BaseEndConst" + "_AIM") )
                arrowEndConst = util.constrain(base[0], starterArrow[1], args={ "t":1, "name":(self.name + "ArrowConst")} )
                arrowAimConst = cmds.aimConstraint(end[0], starterArrow[1], n = (self.name + "ArrowConst" + "_AIM") )
                
                util.lockHide(base[0], {"s":1,"v":1, "l":1, "h":1})
                util.lockHide(middle[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                util.lockHide(end[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                
                cmds.parent(end[1], base[0])
                cmds.parent(middle[1], axisCtl[1] )
                cmds.parent(axisCtl[0],base[0] )
                cmds.parent(base[1], rootGrp,)
                cmds.parent(starterArrow[1], rootGrp)
                cmds.parent(jointGrp, rootGrp)
                
                cmds.move(0, 0, 0, base[1])
                cmds.move(0, 0, 2, end[1])
                
                cmds.parent(rootGrp, self.rootGrp)
                
                #store joints and controls
                self.storeStarterJoints( joints )
                self.storeStarterControls( [base[0],middle[0],end[0]] )
                
        @NWModule.buildPrePost
        def build(self,**kwargs):
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
                handleData = util.createIkHandle(self.name, joints, {})
                poleData =  util.createPoleVec(joints, handleData[0], 3)
                
                cmds.parent(handleData[0], setupGrp)
                cmds.parent(poleData, setupGrp)
                
                # Create controls for handle
                baseCtl = util.createControl( (self.name  + "Base"), {} )
                ikCtl = util.createControl( (self.name  + "IK"), {"shape":"locator"} )
                poleCtl = util.createControl( (self.name  + "Pole"), {"shape":"locator"} )
                
                args = {"all" : 1, "mo" : 0}
                util.match(baseCtl[1], joints[0], args)
                util.match(ikCtl[1], joints[2], args)
                util.match(poleCtl[1], poleData[0], args)
                
                cmds.parent(baseCtl[1], controlGrp)
                cmds.parent(ikCtl[1], baseCtl[0])
                cmds.parent(poleCtl[1], baseCtl[0])
                
                middleConst =util.constrain(ikCtl[0], handleData[0], { "all":1, "name":(self.name + "IK")} )
                poleConst =util.constrain(poleCtl[0], poleData[0], { "all":1, "name":(self.name + "Pole")} )
                
                cmds.parent(rootGrp, self.rootGrp)
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
