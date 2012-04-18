
class NWModule:
        def __init__(self, name):
                self.name = name
                # create update variable if module is reloaded get variables from
                # container
                self.update = 0
                self.startVar = 0
                self.buildVar = 0
                self.connectVar = 0
                self.name = name
                self.container = cmds.container( n= name)
                
                # create default hierarchy for module
                
        def startComplete(self):
                #set start to 1 in container and class
                self.storeVariable("start", "st", "short", 1)
                self.startVar = 1

        def buildComplete(self):
                #set start to 1 in container and class
                self.storeVariable("build", "bu", "short", 1)
                self.buildVar = 1
                
        @startPrePost        
        def start(self):
            pass
        @buildPrePost   
        def build(self):
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

        def storeStarterJoints(self, joints):
                #should check for starter variable
                self.storeStringArrayVariable("starterJoints", "sj", joints)

        def getStarterJoints(self):
                return self.getVariable("starterJoints")

        def storeStarterControls(self, controls):
                #should check for starter variable
                self.storeStringArrayVariable("starterControls", "sc", controls)

        def getStarterControls(self):
                return self.getVariable("starterControls")

# startFunct()

# buildFunct()

# connectFunct()
