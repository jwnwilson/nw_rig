"""
    Module that is parent of all other rig module components
    
"""
from functools import wraps
import maya.cmds as cmds

import UtilitiesPackage as Util

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
               cmds.error(("Blueprint method not run for " + args[0].name))
            args[0].rigPre()
            print ("calling : Rig " + args[0].name)
            ret = rig(*args, **kwds)
            args[0].rigPost()
            return ret
        return wrapper 
        
class ModuleAttribute():
    """
        Class to hold blueprint and rig attribute data
    """
    def __init__(self, name, connection_type, defaultValue, max = None, min = None ):
        self.name = name
        self.type = connection_type
        self.value = defaultValue
        self.defaultValue = defaultValue
        self.max = max
        self.min = min

class Module:
        """
            Base Class for all modules
        """
        #Satic variables
        blueprintAttributes = {}
        rigAttributes = {}
        
        def __init__(self, name):
            # create update variable if module is reloaded get variables from
            # container
            self.name = name
            self.update = 0
            self.blueprintVar = 0
            self.rigVar = 0
            self.connectVar = 0
            self.registeredAttributes= []
            self.inputs = {}
            self.outputs = {}
            self.connections = {}
            self.groups = {}
            
            # create default hierarchy for module
            # if Module already exists use existing objects
            if Util.checkForExistingObject( (self.name + "_CNT"), "container" ):
                self.container = (self.name + "_CNT")
            else:
                self.container = cmds.container( n= (self.name + "_CNT"))
                Util.storeString(self.container, "type", "Module")
            if Util.checkForExistingObject( (self.name + "Root_GRP"), "transform" ):
                self.rootGrp = (self.name + "Root_GRP")
            else:
                self.rootGrp = cmds.group( n = (self.name + "Root_GRP"), em = True )
                self.storeInput(self.rootGrp,"root")
            
            # class specific init
            self.initialize()
            
        @classmethod
        def attributes(cls):
            """
                attributes for each class
            """
            return {"blueprintAttr": cls.blueprintAttributes, "rigAttr" : cls.rigAttributes}
        
        def initialize(self):
            pass
        def blueprintPre(self):
            # create registries
			self.createRegistry("regBlueprintTransform")
			self.createRegistry("regBlueprintShape")
			
			# create Base Groups
			self.groups['blueprint_root'] = cmds.group( n = (self.name + "Blueprint_GRP"), em = True )
			self.groups['blueprint_joint'] = cmds.group( n = (self.name + "BlueprintJoint_GRP"), em = True, p = self.groups['blueprint_root'] )
                    
        def rigPre(self):
            # create registries
			self.createRegistry("regRigTransform")
			self.createRegistry("regRigShape")
			
			# Check for module container
			rootGrp = cmds.group( n = (self.name + "Rig_GRP"), em = True )
			jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True, p= rootGrp)
			setupGrp = cmds.group( n = (self.name + "Setup_GRP"), em = True, p= rootGrp)
			contorlGrp = cmds.group( n = (self.name + "Control_GRP"), em = True, p= rootGrp)
			
			self.groups['rig_root'] = rootGrp
			self.groups['rig_joint'] = jointGrp
			self.groups['rig_setup'] = setupGrp
			self.groups['rig_control'] = contorlGrp
			
			# Turn off jointGrp inherit transform to avoid double trans
			cmds.setAttr( (jointGrp +".inheritsTransform"), 0)
			
			# Get blueprinter joints
			blueprinters  = self.getBlueprinterJoints()
			for joint in blueprinters:
				if cmds.objExists(joint) == False:
					cmds.error(joint + " not found!")
			
			# Duplicate joints
			joints = Util.duplicateChain( self.name , blueprinters)
			cmds.parent(joints[0],jointGrp)
			self.storeRigJoints(joints)
			
			# Hide blueprinters joints
			cmds.setAttr((self.name + "Blueprint_GRP" + ".v"), 0)

        def blueprintPost(self):
            # Store root group as container asset
            cmds.container( self.container, edit=True, f= True, addNode= self.rootGrp, includeNetwork=True, includeHierarchyBelow= True)
            #set blueprint to 1 in container and class
            self.storeVariable("blueprint", "st", "short", 1)
            self.blueprintVar = 1
            
        def rigPost(self):
            # Store root group as container asset
            cmds.container( self.container, edit=True, f= True, addNode= self.rootGrp, includeNetwork=True, includeHierarchyBelow= True)
            #set blueprint to 1 in container and class
            self.storeVariable("rig", "bu", "short", 1)
            # load connections data and connect stuff up!
            self.rigVar = 1
            
        def isRoot(self):
            return False
            
        def blueprintMode(self):
            if self.getVariable("blueprint") == 1:
                return True
            else:
                return False
        def rigMode(self):
            if self.getVariable("rig") == 1:
                return True
            else:
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
                    cmds.error("Container attribute not found for attribute name: %s"% (self.container + "." + attribute))

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
                
        def storeRigJoints(self, joints):
                #should check for blueprinter variable
                self.storeStringArrayVariable("rigJoints", "rj", joints)

        def getRigJoints(self):
                return self.getVariable("rigJoints")

        def storeRigControls(self, controls):
                #should check for blueprinter variable
                self.storeStringArrayVariable("rigControls", "rc", controls)

        def getRigControls(self):
                return self.getVariable("rigControls")
                
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
                    key = Util.getSuffix(attr)
                    if key != "data":
                        # get connected obj
                        objs = Util.getConnectedObjects( (self.container + "." + attr) )
                        # store obj
                        self.inputs[key] = Util.getFirst(objs)
                            
            if outputsAttrs:
                for attr in outputsAttrs:
                    # get attr key
                    key = Util.getSuffix(attr)
                    if key != "data":
                        # get connected obj
                        objs = Util.getConnectedObjects( (self.container + "." + attr) )
                        # store obj
                        self.outputs[key] = Util.getFirst(objs)
        
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
                Util.addAttr(object, connectAttr, "message" )
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
                Util.addAttr(self.container, connectAttr, "message" )
                Util.addAttr(object, connectAttr, "message" )
                cmds.connectAttr((self.container + "." + connectAttr), (object + "." + connectAttr) )
                # Store connection Data
                connectionDataAttr = (connectAttr + "_data")
                connectionData = ["type",type, "attr",attrName  ] 
                Util.addStringArrayAttribute(self.container , connectionDataAttr,connectionData )
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
                Util.addAttr(self.container, connectAttr, "message")
                # Store connection Data
                connectionData = ["type:",type, "attr:",attrName ,"input:",inputPlug ,"output:",outputPlug, "connectionKey:",connectionKey ] 
                Util.addStringArrayAttribute(self.container , connectDataAttr, connectionData )
                self.connections[connectionKey] = {"input":inputPlug,"output":outputPlug, "connectAttr":connectAttr}
                self.registerAttribute( connectDataAttr )
            else:
                cmds.warning( "Connection value :" + (self.container + "." + connectAttr) + " already exists" )
        
        def clearModuleRigData(self):
            """
                Will delete input , output adn connection data
            """
            # Get input attrs
            inputAttrs = cmds.listAttr( self.container, st='input_*')
            # Get output attrs
            outputAttrs = cmds.listAttr( self.container, st='output_*')
            # Get connections attrs
            connectAttrs = cmds.listAttr( self.container, st='connection_*')
            
            if inputAttrs == None:
                inputAttrs = []
            if outputAttrs == None:
                outputAttrs = []
            if connectAttrs == None:
                connectAttrs = []
            
            attrs = (inputAttrs + outputAttrs + connectAttrs)
            # Delete attrs
            for attr in attrs:
                cmds.deleteAttr( self.container, at= attr)
            
        def updateConnectionData(self):
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
                    suffix = Util.getSuffix(attr)
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
                Util.addStringArrayAttribute(self.container,"regAttribute",[attrName])
            else:
                data = cmds.getAttr((self.container + ".regAttribute"))
                data.append(attrName)
                Util.setStringArrayData(self.container,"regAttribute",data)
                self.registeredAttributes.append(attrName)
                
        def getRegisteredAttributes(self):
            """
                Gets list of attributes registered on module
            """
            if cmds.objExists((self.container + ".regAttribute")):
                return cmds.getAttr((self.container + ".regAttribute"))
            else:
                return []
                        
        def createRegistry(self,connection_type):
            """                         
                Will add message attr to container to connect to objects for commands
                to be called on
                
                Stores registry in regAttribute
            """
            if cmds.objExists( (self.container + "." + connection_type) ) == False:
                cmds.addAttr(self.container, ln = connection_type, at= "message")
                self.registerAttribute(connection_type)
                
        def registerObjects(self, objects, connection_type):
            """
                will connect object to container attribute so specific commands can be called on it
                later
            """
            # Cast to type
            if type(objects) != type([]):
            	    objects = [objects]
            	    
            if cmds.objExists( (self.container + "." + connection_type) ):
                for obj in objects:
                    print obj
                    Util.addAttr(obj, connection_type, "message" )
                    cmds.connectAttr((self.container + "." + connection_type), (obj + "." + connection_type) )
            else:
                cmds.error( (self.container + "." + connection_type) + " not found" )
                    
        def getRegisteredObjects(self,connection_type):
            """
                Will return objects connected to registry attribute
            """
            if cmds.objExists( (self.container + "." + connection_type) ):
                return Util.getConnectedObjects( (self.container + "." + connection_type) )
            else:
                cmds.error( (self.container + "." + connection_type) + " not found" )
