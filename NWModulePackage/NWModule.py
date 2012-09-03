"""
    Module that is parent of all other rig module components
    
"""
from functools import wraps
import NWUtilitiesPackage.NWUtilities as util
import maya.cmds as cmds


def blueprintPrePost(blueprint):
        @wraps(blueprint)
        def wrapper(*args, **kwds):
            args[0].blueprintPre()
            print ("calling : Blueprint " + args[0].name)
            ret = blueprint(*args, **kwds)
            args[0].blueprintPost()
            return ret
        return wrapper
        
def rigPrePost(rig):
        @wraps(rig)
        def wrapper(*args, **kwds):
            if args[0].blueprintVar  == False :
               cmds.error(("Blueprint method not run for " + self.name))
            args[0].rigPre()
            print ("calling : Rig " + args[0].name)
            ret = rig(*args, **kwds)
            args[0].rigPost()
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
            self.blueprintVar = 0
            self.rigVar = 0
            self.connectVar = 0
            self.name = name
            self.attributes = {}
            self.registeredAttributes= []
            self.inputs = {}
            self.outputs = {}
            self.connections = {}
            
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
                self.storeInput(self.rootGrp,"root")
            
            # class specific init
            self.initialize()
                
        def initialize(self):
            pass
        def blueprintPre(self):
            pass
                    
        def rigPre(self):
            # Hide blueprint
            if cmds.objExists( (self.name + "Blueprint_GRP") ):
                cmds.setAttr( (self.name + "Blueprint_GRP" + ".v"), 0)
        def blueprintPost(self):
            #set blueprint to 1 in container and class
            self.storeVariable("blueprint", "st", "short", 1)
            self.blueprintVar = 1
        def rigPost(self):
            #set blueprint to 1 in container and class
            self.storeVariable("rig", "bu", "short", 1)
            # load connections data and connect stuff up!
            self.rigVar = 1
            
        def isRoot(self):
            return False
                
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
                    if key != "data":
                        # get connected obj
                        objs = util.getConnectedObjects( (self.container + "." + attr) )
                        # store obj
                        self.inputs[key] = util.getFirst(objs)
                            
            if outputsAttrs:
                for attr in outputsAttrs:
                    # get attr key
                    key = util.getSuffix(attr)
                    if key != "data":
                        # get connected obj
                        objs = util.getConnectedObjects( (self.container + "." + attr) )
                        # store obj
                        self.outputs[key] = util.getFirst(objs)
        
        def storeInput(self,object,key):
            """
                Will store message attribute on container connected to input with key in attr name
            """
            attr = self.createInputOutputAttr(object,key,"input")
            self.registerAttribute( attr )
        
        def storeOutput(self,object,key):
            """
                Will store message attribute on container connected to output with key in attr name
            """
            attr = self.createInputOutputAttr(object,key,"output")
            self.registerAttribute( attr )
        
        def createInputOutputAttr(self, object, key, inputOutput):
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
            
            # Old code only hands transforms
            """if cmds.objExists( (self.container + "." + connectAttr) ) == False:
                cmds.addAttr(self.container, ln = connectAttr, at= "message")
                util.addAttr(object, connectAttr, "message" )
                cmds.connectAttr((self.container + "." + connectAttr), (object + "." + connectAttr) )
                command = ("self." + inputOutput + "s[key] = object")
                exec command
            else:
                cmds.error( "Input / output value :" + (self.container + "." + connectAttr) + " already exists" )"""
            
            type = "trans"
            attrName = ""
            
            # Check if object is attribute
            if len( object.split(".") ) > 1:
                type = "attr"
                object = object.split(".")[0]
                attrName = object.split(".")[1:]
            
            if cmds.objExists( (self.container + "." + connectAttr) ) == False:
                # Mesasage array to link nodes
                util.addAttr(self.container, connectAttr, "message" )
                util.addAttr(object, connectAttr, "message" )
                cmds.connectAttr((self.container + "." + connectAttr), (object + "." + connectAttr) )
                # Store connection Data
                connectionDataAttr = (connectAttr + "_data")
                connectionData = ["type",type, "attr",attrName  ] 
                util.addStringArrayAttribute(self.container , connectionDataAttr,connectionData )
                # Store connection in dict
                command = ("self." + inputOutput + "s[key] = object")
                exec command
            else:
                cmds.error( "Input / output value :" + (self.container + "." + connectAttr) + " already exists" )
            return  connectAttr
            
        def getInput(self, key):
            """
                get input object from key
            """
            self.updateInputOutputs()
            if self.inputs.has_key(key):
                return self.inputs[key]
            else:
                return false
        def getOutput(self, key):
            """
                get input object from key
            """
            self.updateInputOutputs()
            if self.outputs.has_key(key):
                return self.outputs[key]
            else:
                return false
                
        def storeConnection(self, connectionKey, inputPlug, outputPlug , type, attrName= "None"):
            """
                Store connection data between output to input on current module
            """
            
            connectAttr = ("connection_" + connectionKey)
            connectDataAttr = ("connection_" + connectionKey + "_data")
            connectInputAttr = ("connection_" + connectionKey + "_input")
            connectOutputAttr = ("connection_" + connectionKey + "_output")
            
            if cmds.objExists( (self.container + "." + connectAttr) ) == False:
                util.addAttr(self.container, connectAttr, "message")
                # Store connection Data
                connectionData = ["type:",type, "attr:",attrName ,"input:",inputPlug ,"output:",outputPlug, "connectionKey:",connectionKey ] 
                util.addStringArrayAttribute(self.container , connectDataAttr, connectionData )
                self.connections[connectionKey] = {"input":inputPlug,"output":outputPlug, "connectAttr":connectAttr}
                self.registerAttribute( connectDataAttr )
            else:
                cmds.warning( "Connection value :" + (self.container + "." + connectAttr) + " already exists" )
                
        def updateConnectionData():
            """
                Go through module finding connections and updating connections dict
            """
            # Get connections attrs
            connectAttrs = cmds.listAttr( self.container, st='connection_*')
            connectionData = {}
            
            if connectAttrs:
                for attr in connectAttrs:
                    # get attr key
                    key = attr.split("_")[1]
                    suffix = util.getSuffix(attr)
                    if suffix == "data":
                        # get connected obj
                        data = cmds.getAttr( (self.container + "." + attr ) )
                        if data:
                            connectionData = {data[0]:data[1],data[2]:data[3], data[4]:data[5]}
                        else:
                            cmds.error("Connection attribute name incorrect")
                        # store obj
                        self.connections[key] = connectionData
                
        def getConnectionData(self, connectionKey):
            """
                returns connection dict
            """
            self.updateConnectionData()
            if self.connections.has_key(connectionKey):
                return self.connections[connectionKey]
            else:
                return False
                
        def registerAttribute(self, attrName):
            """
                Creates array of attribute names that will store data on module
            """
            if cmds.objExists((self.container + ".regAttribute")) == False:
                util.addStringArrayAttribute(self.container,"regAttribute",[attrName])
            else:
                data = cmds.getAttr((self.container + ".regAttribute"))
                data.append(attrName)
                util.setStringArrayData(self.container,"regAttribute",data)
                self.registeredAttributes.append(attrName)
                
        def getRegisteredAttributes(self):
            """
                Gets list of attributes registered on module
            """
            if cmds.objExists((self.container + ".regAttribute")):
                return cmds.getAttr((self.container + ".regAttribute"))
            else:
                return []
                        
        def createRegistry(self,type):
            """                         
                Will add message attr to container to connect to objects for commands
                to be called on
                
                Stores registry in regAttribute
            """
            if cmds.objExists( (self.container + "." + type) ) == False:
                cmds.addAttr(self.container, ln = type, at= "message")
                self.registerAttribute(type)
                
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
            if cmds.objExists( (self.container + "." + type) ):
                return util.getConnectedObjects( (self.container + "." + type) )
            else:
                cmds.error( (self.container + "." + type) + " not found" )
# blueprintFunct()

# rigFunct()

# connectFunct()
