"""
Module that is parent of all other rig module components
"""
from functools import wraps
import NWUtilitiesPackage.NWUtilities as util
import maya.cmds as cmds


def startPrePost(start):
        @wraps(start)
        def wrapper(*args, **kwds):
            args[0].startPre()
            print ("calling :" + start.__name__ + " " + args[0].name)
            ret = start(*args, **kwds)
            args[0].startPost()
            return ret
        return wrapper
        
def buildPrePost(build):
        @wraps(build)
        def wrapper(*args, **kwds):
	    if args[0].startVar  == False :
               cmds.error(("Start method not run for " + self.name))
            args[0].buildPre()
            print ("calling :" + build.__name__)
            ret = build(*args, **kwds)
            args[0].buildPost()
            return ret
        return wrapper 


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
                self.attributes = {}
                
                # create default hierarchy for module
                # if Module already exists use existing objects
                if util.checkForExistingObject( (self.name + "_CNT"), "container" ):
                    self.container = (self.name + "_CNT")
                else:
                    self.container = cmds.container( n= (self.name + "_CNT"))
                    util.storeString(self.container, "type", "NWModule")
                if util.checkForExistingObject( (self.name + "Root_GRP"), "transform" ):
                    self.rootGrp = (self.name + "Root_GRP")
                else:
                    self.rootGrp = cmds.group( n = (self.name + "Root_GRP"), em = True )
                
                # class specific init
                self.initialize()
                
        def initialize(self):
                pass
        def startPre(self):
                pass
        def buildPre(self):
                pass
        def startPost(self):
                #set start to 1 in container and class
                self.storeVariable("start", "st", "short", 1)
                self.startVar = 1
        def buildPost(self):
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
