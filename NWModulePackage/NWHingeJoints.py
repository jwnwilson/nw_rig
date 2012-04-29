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
                joints = []
                joints.append(base[2])
                joints.append(middle[2])
                joints.append(end[2])
                cmds.parent(joints[2], joints[1])
                cmds.parent(joints[1], joints[0])
                cmds.parent(joints[0], jointGrp)
                
                # create arrow ctls
                args = {"shape":"arrow", "size":0.5}
                starterArrow = util.createControl( (self.name + "Direction"), args )
                cmds.rotate( 0, 90, 0 , starterArrow[1])
                args = {"all" : 1, "mo" : 0}
                cmds.cycleCheck( e= 0)
                util.match(joints[0], base[0], args)
                util.match(joints[1], middle[0], args)
                util.match(joints[2], end[0], args)
                cmds.cycleCheck( e= 1)
                args = {"shape":"arrow", "size":0.5}
                axisCtl = util.createAxisContols((self.name + "axisCtl"), args )

                # create constraints                
                baseConst = cmds.pointConstraint(base[0], joints[0], n = (self.name + "BaseConst" + "_PNT") ) 
                endConst =cmds.pointConstraint(end[0], joints[2], n = (self.name + "EndConst" + "_PNT") )
                middleConst =cmds.pointConstraint(middle[0], joints[1], n = (self.name + "MiddleConst" + "_PNT") )
                baseEndConst = cmds.pointConstraint(end[0], base[0], axisCtl[0], n = (self.name + "BaseEndConst" + "_PNT") )
                baseEndAimConst = cmds.aimConstraint(base[0], axisCtl[0], n = (self.name + "BaseEndConst" + "_AIM") )
                arrowAimConst = cmds.aimConstraint(end[0], starterArrow[1], n = (self.name + "ArrowConst" + "_AIM") )
                arrowEndConst = cmds.pointConstraint(base[0], starterArrow[1], n = (self.name + "ArrowConst" + "_PNT") )
                
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
                print handleData
                poleData =  util.createPoleVec(joints, handleData[0], 3)
                
                cmds.parent(handleData, setupGrp)
                cmds.parent(poleData, setupGrp)
                
                # Create controls for handle
                
                #self.buildComplete()
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
