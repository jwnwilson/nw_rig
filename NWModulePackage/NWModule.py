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
            print ("calling : Start " + args[0].name)
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
            print ("calling : Build " + args[0].name)
            ret = build(*args, **kwds)
            args[0].buildPost()
            return ret
        return wrapper 


class NWModule:
        """
            Base Class for all modules
        """
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
            self.registeredAttributes= []
            self.inputs = {}
            self.outputs = {}
            
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
                
        def updateInputOutputs(self):
            """
                finds attributes on module with "input_" & "output_" prefix then populates dicts
            """
            
            # Get input attrs
            inputsAttrs = cmds.listAttr( self.container, st='input_*')
            # Get output attrs
            outputsAttrs = cmds.listAttr( self.container, st='output_*')
            
            if inputsAttrs:
                for attr in inputsAttrs:
                        # get attr key
                        key = util.getSuffix(attr)
                        # get connected obj
                        objs = util.getConnectedObjects( attr )
                        # store obj
                        self.inputs[key] = util.getFirst(objs)
                                
            if outputsAttrs:
                for attr in outputsAttrs:
                        # get attr key
                        key = util.getSuffix(attr)
                        # get connected obj
                        objs = util.getConnectedObjects( attr )
                        # store obj
                        self.outputs[key] = util.getFirst(objs)
        
        def storeInput(self,object,key):
            """
                Will store message attribute on container connected to input with key in attr name
            """
            self.createInputOutputAttr(object,key,"input")
        
        def storeOutput(self,object,key):
            """
                Will store message attribute on container connected to output with key in attr name
            """
            self.createInputOutputAttr(object,key,"output")
        
        def createInputOutputAttr(object, key, inputOutput):
            """
                Will store message attribute on container connected to object with key in attr name
            """
            connectAttr = ""
            if inputOutput == "input":
                connectAttr = ("input_" + key)
            elif inputOutput == "output":
                connectAttr = ("output_" + key)
            else:
                cmds.error( "Input or output type not specified" )
                
            if cmds.objExists( (self.container + "." + connectAttr) ) == False:
                cmds.addAttr(self.container, ln = connectAttr, at= "message")
                util.addAttr(object, connectAttr, "message" )
                cmds.connectAttr((self.container + "." + connectAttr), (object + "." + connectAttr) )
                command = ("self." + inputOutput + "s[key] = object")
                exec command
            else:
                cmds.error( "Input / output value :" + (self.container + "." + connectAttr) + " already exists" )

        def createRegistry(self,type):
            """
                Will add message attr to container to connect to objects for commands
                to be called on
                
                Note: Current registry types:
                regStartTransform
                regStartShape
                regBuildTransform
                regBuildShape
            """
            if cmds.objExists( (self.container + "." + type) ) == False:
                cmds.addAttr(self.container, ln = type, at= "message")
                self.registeredAttributes.append(type)
                
        def registerObjects(self, objects, type):
            """
                will connect object to container attribute so specific commands can be called on it
                later
            """
            if cmds.objExists( (self.container + "." + type) ):
                for object in objects:
                    util.addAttr(object, type, "message" )
                    cmds.connectAttr((self.container + "." + type), (object + "." + type) )
            else:
                cmds.error( (self.container + "." + type) + " not found" )
                    
        def getRegisteredObjects(self,type):
            """
                Will return objects connected to registry attribute
            """
            return util.getConnectedObjects( (self.container + "." + type) )
# startFunct()

# buildFunct()

# connectFunct()
