
class NWModule:
        def __init__(self, name):
                self.name = name
                # create update variable if module is reloaded get variables from
                # container
                self.update = 0
                self.blueprintVar = 0
                self.rigVar = 0
                self.connectVar = 0
                self.name = name
                self.container = cmds.container( n= name)
                
                # create default hierarchy for module
                
        def blueprintComplete(self):
                #set blueprint to 1 in container and class
                self.storeVariable("blueprint", "st", "short", 1)
                self.blueprintVar = 1

        def rigComplete(self):
                #set blueprint to 1 in container and class
                self.storeVariable("rig", "bu", "short", 1)
                self.rigVar = 1
                
        @blueprintPrePost        
        def blueprint(self):
            pass
        @rigPrePost   
        def rig(self):
            pass
                
        def storeVariable(self, attribute, shortAttr, varType, variable):
                #if container exists store variable
                if cmds.attributeQuery(attribute, n= self.container, exists = True ):
                        cmds.setAttr( (self.container + "." + attribute), variable)
                else:
                        cmds.addAttr(self.container, at = varType, ln = attribute, sn= shortAttr)
                        cmds.setAttr( (self.container + "." + attribute), variable)                

        def storeStringArrayVariable(self, attribute, shortAttr, variable):
                #if container exists store variable
                if cmds.attributeQuery(attribute, n= self.container, exists = True ):
                        cmds.setAttr( (self.container + "." + attribute), type = 'stringArray', *([len(variable)] + variable) )
                else:
                        cmds.addAttr(self.container, dt = "stringArray", ln = attribute, sn = shortAttr)
                        cmds.setAttr( (self.container + "." + attribute), type = 'stringArray', *([len(variable)] + variable) )

        def getVariable(self, attribute):
                #if container exists store variable
                if cmds.attributeQuery(attribute, n= self.container, exists = True ):
                        return cmds.getAttr( (self.container + "." + attribute) )
                else:
                        cmds.error("Container attribute not found.")

        def storeBlueprinterJoints(self, joints):
                #should check for blueprinter variable
                self.storeStringArrayVariable("blueprinterJoints", "sj", joints)

        def getBlueprinterJoints(self):
                return self.getVariable("blueprinterJoints")

        def storeBlueprinterControls(self, controls):
                #should check for blueprinter variable
                self.storeStringArrayVariable("blueprinterControls", "sc", controls)

        def getBlueprinterControls(self):
                return self.getVariable("blueprinterControls")

# blueprintFunct()

# rigFunct()

# connectFunct()
