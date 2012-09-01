"Requires that Module class is sourced"

class NWHingeJoints(Module):
        'Creates a hinge joints for arms and leg type joints' 
        @blueprintPrePost
        def blueprint(self,**kwargs):
                'Creates a hinge joint can be used for arms or legs'
                #create container to store all module variables
                
                rootGrp = cmds.group( n = (self.name + "Blueprint_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True )
                
                # create blueprinters
                base = util.createBlueprinter((self.name + "base"), {"shape":"sphere", "size": 0.5})
                middle = util.createBlueprinter((self.name + "middle"), {})
                end  = util.createBlueprinter((self.name + "end"), {"shape":"sphere", "size": 0.5})
                
                # manage blueprinter joints
                joints = []
                joints.append(base[2])
                joints.append(middle[2])
                joints.append(end[2])
                cmds.parent(joints[2], joints[1])
                cmds.parent(joints[1], joints[0])
                cmds.parent(joints[0], jointGrp)
                
                # create arrow ctls
                args = {"shape":"arrow", "size":0.5}
                blueprinterArrow = util.createControl( (self.name + "Direction"), args )
                cmds.rotate( 0, 90, 0 , blueprinterArrow[1])
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
                arrowAimConst = cmds.aimConstraint(end[0], blueprinterArrow[1], n = (self.name + "ArrowConst" + "_AIM") )
                arrowEndConst = cmds.pointConstraint(base[0], blueprinterArrow[1], n = (self.name + "ArrowConst" + "_PNT") )
                
                util.lockHide(base[0], {"s":1,"v":1, "l":1, "h":1})
                util.lockHide(middle[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                util.lockHide(end[0], {"r":1,"s":1,"v":1, "l":1, "h":1})
                
                cmds.parent(end[1], base[0])
                cmds.parent(middle[1], axisCtl[1] )
                cmds.parent(axisCtl[0],base[0] )
                cmds.parent(base[1], rootGrp,)
                cmds.parent(blueprinterArrow[1], rootGrp)
                cmds.parent(jointGrp, rootGrp)
                
                cmds.move(0, 0, 0, base[1])
                cmds.move(0, 0, 2, end[1])
                
                #store joints and controls
                self.storeBlueprinterJoints( joints )
                self.storeBlueprinterControls( [base[0],middle[0],end[0]] )
                
        @rigPrePost
        def rig(self,**kwargs):
                # check for module container
                rootGrp = cmds.group( n = (self.name + "Rig_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True, p= rootGrp)
                setupGrp = cmds.group( n = (self.name + "Setup_GRP"), em = True, p= rootGrp)
                
                if cmds.objExists(self.container) == False :
                    cmds.error("Container: " + self.name + " does not exist!")
                #get blueprinter joints
                blueprinters  = self.getBlueprinterJoints()
                
                for joint in blueprinters:
                    if cmds.objExists(joint) == False:
                        cmds.error(joint + " not found!")

                # Duplicate joints
                joints = util.duplicateChain( self.name , blueprinters)
                cmds.parent(joints,jointGrp)
                
                if len(joints) > 3:
                    cmds.error("Too many joints in: " + self.name + "!")
                # Hide blueprinters joints
                cmds.setAttr((self.name + "Blueprint_GRP" + ".v"), 0)
                
                # Create ikHandle
                handleData = util.createIkHandle(joints)
                poleData =   util.createPoleVec(joints, handleData[1])
                
                # Create controls for handle
                
                #self.rigComplete()
        def connect(self,**kwargs):
            # Get Connection data
            
            # Check both objects exists
            
            # connect objects
            pass
