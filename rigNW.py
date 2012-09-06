# -*- coding: utf-8 -*-
"""
To do:
- Need inhertance of modules - done
- Need to have multiple instances supported and namespaces for items in containers
- Needs more sub controls for blueprinters
- Blueprinter direction needs to be influenced by other blueprinter controls
- All inputs and outputs refreshed when connection queried can be optimised
- All components must be stored in containers
- Need to store connections -done
- Option to go from rig back to blueprint and via versa
- Require rename option
- Create a defomation menu / skinning menu

- Require a pickle / refresh python module data function so scene data can be reloaded into tool
- Create String array data loader, variable == variable: followed by data
- Create menu
    - New are you sure box
    - Save all
    - Load all
- Blueprint Menu
    - cleaner menu
- Rig Menu
    - Save
        - save control shapes
        - save connections between objects
        - Clean up rig data connection function
        
        
        
"""

MAYA_STANDALONE = 0
DEBUG =0

if MAYA_STANDALONE or DEBUG:
    import maya.standalone
    maya.standalone.initialize()

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaAnim as OpenMayaAnim
import ctypes
import os
import sys
import maya.OpenMaya as OpenMaya
from functools import wraps

PATH_INDICE = 0
ROOT_PATH=[]
PACKAGES ={}

"""
Add python directory to sys.path if necessary depending on operating system
"""
if os.name == 'posix':
    FILE_PATH = "/media/WALKMAN/Python/NWRig/"
elif os.name == 'nt':
    FILE_PATH = "F:/Documents and Settings/Noel Wilson/My Documents/Git/NWRig/"
if FILE_PATH not in sys.path:
    sys.path.append( FILE_PATH )

"""
source utilities first remove duplicate code in __init__
source packages
"""
import NWUtilitiesPackage.NWFileUtilities as fileUtil
import NWUtilitiesPackage.NWUtilities as util
reload(fileUtil)
reload(util)

"""
Dynamic importing of modules
"""
PACKAGES = fileUtil.import_packages( FILE_PATH )
for key in PACKAGES.keys():
    globals()[key] = PACKAGES[key]

class Command:
        def __init__(self,name): 
                self.name = name
                
# contains rig system
class RigNW:
        """
            Manages project and loads gui / rigs the rig
        """
        def __init__(self, name, **kwargs):
                classArgs = {"UIFile":"default.py","rerigUI":True}
                #classArgs =  dict(classArgs.items() + kwargs.items())
                classArgs =  util.defaultArgs( classArgs,  kwargs)
                self.Modules = {}
                self.connections = {}
                self.name = name
                self.UIFile =  classArgs["UIFile"]
                if classArgs["rerigUI"]:
                    self.UI = self.initialiseUI()
                
        def initialiseUI(self):
            """ 
                read in UIFile
            """
            windowDir = NWWindowPackage.__path__
            filePath = (windowDir[0] + "/blueprints/" +self.UIFile)
            FILE = open(filePath,"rU")
            command = FILE.read()
            FILE.close()
            exec command
            
            return window
            
        # ------------------------      
        # Load save data
        # ------------------------    
        """def loadBluePrints(self):
            ""
                Loads blueprints for current rig
            ""
            # refresh UI path
            self.UI.getFilePath()
            blueprintFilePath = (str(self.UI.filePath) + "BlueprintData.txt")
            FILE = open(blueprintFilePath,"rU")
            lineArray = FILE.readlines()
            FILE.close()
            
            # Build blueprints
            for line in lineArray:
                moduleName = line.split()[0]
                module = line.split()[1]
                self.blueprintModule(moduleName,module )
            # Load data
            self.loadBlueprintData()"""
        
        def loadBlueprintData(self):
            """
                Loads blueprint data onto blueprinter
            """
            # open file from path in UI
            self.UI.getFilePath()
            for module in self.getModules():
                # Load transforms
                filePath = (str(self.UI.filePath) + module + "BlueprintData.txt")
                self.loadTransforms(filePath)
                # Load attributes
            print ("Blueprint data loaded")
        
        def saveBlueprintData(self):
            """
                Saves blueprint data into file
            """
            # refresh UI path
            self.UI.getFilePath()  
            bluePrintFilePath = (str(self.UI.filePath) + "BlueprintData.txt")
            # Save module data
            self.saveBlueprintModuleData( bluePrintFilePath, self.getModules() )
            # Save detailed info in seperate files
            for module in self.getModules():
                # Save blueprint transforms
                filePath = (str(self.UI.filePath) + module + "BlueprintData.txt")
                self.saveTransforms(filePath, module, "regBlueprintTransform" )
                # Save attribute data
            print ("Blueprint data saved")
            
        def saveRigData(self):
            """
                Saves registered rig Data
            """
            
            self.UI.getFilePath()  
            filePath = (str(self.UI.filePath) + "rigData.txt")
            writeData = ""
            tab = "\t"
            
            # Get container data
            moduleList = self.getModules()
            # for each module
            for module in moduleList:
                # get registered attributes
                writeData += (module + "\n")
                inputData = []
                outputData = []
                connectionsData = []
                regData = []
                registeredAttrs = self.Modules[module].getRegisteredAttributes()
                
                # save container data
                for regAttr in registeredAttrs:
                    writeLine = ""
                    attr = (self.Modules[module].container + "." + regAttr )
                    attrType = cmds.getAttr(attr, type = True)
                    attrData = ""
                    if attrType != "message":
                        attrData = cmds.getAttr(attr)
                    
                    # if attr == message store attribute name and type
                    if attrType == "message":
                        writeLine += ( tab +  attr + " " + attrType ) 
                    # if attr == string store attribute name and data
                    elif attrType == "stringArray":
                        writeLine += ( tab + attr + " " + attrType)
                        for data in attrData:
                            writeLine+= (" " + data)
                    # if attr == etc store attribute name and data
                    else:
                        writeLine += ( tab +  attr + " " + attrType + " " + attrData ) 
                    writeLine += ("\n")
                    
                    if regAttr.startswith("input"):
                        inputData.append(writeLine)
                    elif regAttr.startswith("output"):
                        outputData.append(writeLine)
                    elif regAttr.startswith("connection"):
                        connectionsData.append(writeLine)
                    else:
                        regData.append(writeLine)
                
                # Save transforms
                if "regRigTransform" in registeredAttrs:
                    regTransFilePath = (str(self.UI.filePath) + module + "RigTransData.txt")
                    self.saveTransforms(regTransFilePath, module, "regRigTransform" )
                # Save shapes
                if "regRigShapes" in registeredAttrs:
                    regTransFilePath = (str(self.UI.filePath) + module + "RigShapeData.txt")
                    self.saveShapes(regTransFilePath, module, "regRigShapes" )
                
                writeData += (tab + "Inputs:\n")
                for data in inputData:
                    writeData += (tab + data)
                writeData += (tab + "Outputs:\n")
                for data in outputData:
                    writeData += (tab + data)
                writeData += (tab + "Connections:\n")
                for data in connectionsData:
                    writeData += (tab + data)
                writeData += (tab + "RegisteredAttr:\n")
                for data in regData:
                    writeData += (tab + data)
            
            print ("Saving blueprint data to : " + filePath)
            FILE = open(filePath,"wb")
            blueprintData = FILE.write(writeData)
            FILE.close()
            print ("Blue print data successfully saved!")
            
        def loadRigData(self):
            """
                Load registered rig data
            """
            # open file from path in UI
            self.UI.getFilePath()
            filePath = (str(self.UI.filePath) + "rigData.txt")
            FILE = open(filePath,"rU")
            lineArray = FILE.readlines()
            FILE.close()
            
            fileIndice = 0
            startModuleIndice = 0
            endModuleIndice = 0
            fileSize = len(lineArray)
            
            while fileIndice < fileSize:
                module = lineArray[fileIndice].strip()
                startModuleIndice = fileIndice
                endModuleIndice = self.readRigNextModule(fileIndice, lineArray)
                connections = self.readRigConnectionData(startModuleIndice, endModuleIndice , lineArray)
                registeredAttr = self.readRigRegisteredAttr(startModuleIndice, endModuleIndice , lineArray)
                fileIndice = endModuleIndice
                
                # Load registered Attr data
                for regAttr in registeredAttr:
                    if regAttr.split(".")[1] == "regRigShape":
                        regShapeFilePath = (str(self.UI.filePath) + module + "RigShapeData.txt")
                        self.loadShapes(regShapeFilePath)
                    if regAttr.split(".")[1] == "regRigTransform":
                        regTransFilePath = (str(self.UI.filePath) + module + "RigTransData.txt")
                        self.loadTransforms(regTransFilePath)
                
                # Create connections
                for connection in connections:
                    connectionKey = util.getValueFromDataString(connection, "connectionKey")
                    inputPlug = util.getValueFromDataString(connection, "input")
                    outputPlug = util.getValueFromDataString(connection, "output")
                    type = util.getValueFromDataString(connection, "type")
                    attr = util.getValueFromDataString(connection, "attr")
                    
                    self.Modules[module].storeConnection(connectionKey, inputPlug, outputPlug , type, attrName= "None")
                    self.createConnection(module, connectionKey)
            
            print ("Loaded blueprint data from : " + filePath)
            
        def saveShapes(self, filePath, module, regAttr):
            """
                Will store shape data in file
            """
            objects = self.getRegisteredObjects(module , regAttr)
            writeData = ""
            
            for object in objects:
                # Get shape
                shape = util.getFirst(cmds.listRelatives(object, s= True))
                writeLine = (object + " ")
                # Get CV number
                cvNum = int(cmds.getAttr(shape + ".spans") + cmds.getAttr(shape + ".degree"))
                for x in xrange(cvNum):
                    pos = cmds.xform( (object + ".cv["+x+"]"), q= True, ws= True, t=True )
                    writeLine += (pos[0] + " " + pos[1] + " " + pos[2] + " ")
                writeData += (writeLine + "\n")
            FILE = open(filePath,"wb")
            blueprintData = FILE.write(writeData)
            FILE.close()
            print ("Saved shape data to : " + filePath)
            
        def loadShapes(self, filePath):
            """
                Loads shapes from file
            """
            FILE = open(filePath,"rU")            
                
            for line in FILE:
                shapeDataLine = line.split()
                ShapeObject = shapeDataLines[0]
                shapeDataLines.remove(0)
                index = 0
                for x,y,z in shapeDataLines:
                    cmds.xform( (ShapeObject + ".cv["+index+"]"), ws=True, t= ( x , y , z ) )
                    index+=1
                
            FILE.close()
            print ("Loaded shape data from : " + filePath)
            
        def loadTransforms(self, filePath):
            """
                Loads transforms from file
            """
            FILE = open(filePath,"rU")            
                
            for line in FILE:
                blueprintDataLine = line.split()
                blueprintObject = blueprintDataLine[0]
                translate = [ float( blueprintDataLine[1] ), float( blueprintDataLine[2] ), float( blueprintDataLine[3] ) ]
                rotate = [ float( blueprintDataLine[4] ), float( blueprintDataLine[5] ), float( blueprintDataLine[6] ) ]
                scale = [ float( blueprintDataLine[7] ), float( blueprintDataLine[8] ), float( blueprintDataLine[9] ) ]
                if cmds.objExists(blueprintObject):
                    util.checkSetCompoundAttr( (blueprintObject + ".t"), translate )
                    util.checkSetCompoundAttr( (blueprintObject + ".r"), rotate )
                    util.checkSetCompoundAttr( (blueprintObject + ".s"), scale )
            FILE.close()
            print ("Loaded transfrom data from : " + filePath)
            
        def saveTransforms(self, filePath, module, regAttr):
            """
                Will Store transfrom data in file
            """
            objects = self.getRegisteredObjects( module, regAttr)
            writeData = ""
            
            for object in objects:
                translate = util.getFirst(cmds.getAttr( (object + ".t") ) )
                rotate = util.getFirst( cmds.getAttr( (object + ".r") ) )
                scale = util.getFirst( cmds.getAttr( (object + ".s") ) )
                writeLine = (object + " " + str(translate[0]) + " " + str(translate[1]) + " " + str(translate[2]) + " " +
                                            str(rotate[0]) + " " + str(rotate[1]) + " " + str(rotate[2]) + " " +
                                            str(scale[0]) + " " + str(scale[1]) + " " + str(scale[2]) + "\n")
                writeData += writeLine
            FILE = open(filePath,"wb")
            blueprintData = FILE.write(writeData)
            FILE.close()
            print ("Saved transform data to : " + filePath)
            
        def saveBlueprintModuleData(self, bluePrintFilePath,  modules):
            """
                Saves blueprint module names type and parents
            """
            writeData = ""
            for module in modules:
                writeData += ( module + " " + util.getString(self.Modules[module].container, "type") + "\n" )
                
            FILE = open(bluePrintFilePath,"wb")
            blueprintData = FILE.write(writeData)
            FILE.close()
        
        def readRigConnectionData(self,  startModuleIndice, endModuleIndice, lineArray ):
            """
                Will read array and retrieve connection data
            """
            returnConnectionData= []
            connectionIndiceStart = 0
            connectionIndiceEnd = 1
            for x in xrange( startModuleIndice, endModuleIndice ):
                # remove spaces
                line = lineArray[x].strip()
                if line.startswith("Connections:"):
                    connectionIndiceStart = (x + 1)
                elif line.startswith("RegisteredAttr:"):
                    connectionIndiceEnd = x
            for x in xrange(connectionIndiceStart, connectionIndiceEnd):
                returnConnectionData.append(lineArray[x].strip())
            return returnConnectionData
            
        def readRigRegisteredAttr(self, startModuleIndice, endModuleIndice, lineArray):
            """
                Will read array and retrieve connection data
            """
            returnConnectionData= []
            connectionIndiceStart = 0
            connectionIndiceEnd = 1
            for x in xrange( startModuleIndice, endModuleIndice ):
                # remove spaces
                line = lineArray[x].strip()
                if line.startswith("RegisteredAttr:"):
                    connectionIndiceStart = (x + 1)
                elif line.startswith("\t") == False:
                    connectionIndiceEnd = x
            for x in xrange(connectionIndiceStart, connectionIndiceEnd):
                returnConnectionData.append(lineArray[x].strip())
            return returnConnectionData
            
        def readRigNextModule(self, fileIndice, lineArray):
            """
                Will Find line indice of next module in file
            """
            fileIndice+= 1
            for x in xrange( fileIndice, len(lineArray) ):
                line = lineArray[x]
                if line.startswith("\t") == False:
                    return x
            # return EOF
            return len(lineArray)
                    
        def getRegisteredObjects(self, module, registry):
            """
                finds all registered blueprinter objects from containters
                registry is attribute stored on containers connected to 
                desired objects
            """
            registeredData =[]
            # Get container
            container = self.getContainer(module)
            if cmds.objExists( (container + "." + registry) ):
                registeredData = cmds.listConnections( (container + "." + registry) )
                if registeredData == None:
                    registeredData = []
            else:
                registeredData = []
            return registeredData
        # ------------------------      
        # Module functions
        # ------------------------
        def new(self, **kwards):
            """
                create initial hierarchy for rig
            """
            self.__init__(self.name, rerigUI = False)
            name = self.name
            rootMod = NWRoot.NWRoot(self.name)
            self.Modules["root"] = rootMod
            self.Modules[self.name] = rootMod
            self.Modules["root"].blueprint()
            self.rootGrp = self.Modules["root"].rootGrp
            
        def moduleExists(self, name):
            if cmds.objExists(name + "_CNT"):
                return True
            else:
                return False
        
        def rootExists(self):
            if self.moduleExists(self.name):
                return True
            else:
                return False
                
        def getModules(self):
            moduleKeys = self.Modules.keys()
            # remove root as it will be a duplicate key
            moduleKeys = [ x for x in moduleKeys if not x == "root"]
            
            modules = []
            for key in moduleKeys:
                name  = self.Modules[key].name
                if self.moduleExists(name):
                    modules.append(name)
            return modules
            
        def getContainer(self, module):
            if self.moduleExists(module):
                return (module + "_CNT")
                
        def getRootModuleContainer(self):
            return self.getContainer(self.name)
        
        def checkMethod(self,name, method):
            """
                Check method variable set after completion
            """
            if method == "blueprint" and self.Modules[name].blueprintVar == 0:
                    return True
            if method == "rig" and self.Modules[name].rigVar == 0:
                    return True
            return False
            
        def undoRigMode(self, moduleName):
            """
                Deletes rig and unhides blueprint
            """
            if cmds.objExists( (moduleName + "Blueprint_GRP") ):
                cmds.setAttr((moduleName + "Blueprint_GRP" + ".v"), 1)
                if cmds.objExists( ( moduleName + "Rig_GRP" ) ):
                    cmds.delete( (moduleName + "Rig_GRP") )
                self.Modules[moduleName].storeVariable("blueprint", "st", "short", 1)
                self.Modules[moduleName].blueprintVar = 1
                self.Modules[moduleName].storeVariable("rig", "st", "short", 0)
                self.Modules[moduleName].rigVar = 0
                self.Modules[moduleName].clearModuleRigData()
                
            #else:
            #    cmds.error("Blueprint group not found for : " + moduleName)
            
        """def setRigMode(self, moduleName):
            ""
                Hides rig and unhides blueprint
            ""
            if cmds.objExists( (moduleName + "Rig_GRP") ):
                cmds.setAttr((moduleName + "Blueprint_GRP" + ".v"), 0)
                cmds.setAttr((moduleName + "Rig_GRP" + ".v"), 1)
                self.Modules[moduleName].storeVariable("blueprint", "st", "short", 0)
                self.Modules[moduleName].blueprintVar = 0
                self.Modules[moduleName].storeVariable("rig", "st", "short", 1)
                self.Modules[moduleName].rigVar = 1
            #else:
            #    cmds.error("Rig group not found for : " + moduleName)
        """
        def blueprintMode(self):
            """
                Builds rig blueprints or sets modules back to blueprint mode
            """
            # refresh UI path
            self.UI.getFilePath()
            blueprintFilePath = (str(self.UI.filePath) + "BlueprintData.txt")
            FILE = open(blueprintFilePath,"rU")
            lineArray = FILE.readlines()
            FILE.close()
            
            # Build blueprints
            for line in lineArray:
                moduleName = line.split()[0]
                module = line.split()[1]
                # check modules exist
                if self.moduleExists(moduleName) == False:
                    self.blueprintModule(moduleName,module )
                else:
                    self.undoRigMode(moduleName)
            # Load data
            self.loadBlueprintData()
                
        def rigMode(self):
            """
                Builds rig from blueprints if already built will delete and rebuild
            """
            modules = self.getModules()
            
            for module in modules:
                # Check modules are built
                moduleInstance = self.Modules[module]
                
                if moduleInstance.rigVar == 1 and moduleInstance.isRoot() == False:
                    # if so rebuild but don't reload data
                    self.undoRigMode(module)
                    self.rigModule({"name":module})
                # if not build and load data
                else:
                    self.rigModule({"name":module})
            self.loadRigData()
            
        def blueprintModule(self, name ,module):
            """
                Run blueprint method for module
            """
            # get module name
            #windowElement = self.UI.inputs["blueprintTextField"]
            #name = cmds.textField(windowElement.fullPath, q=True,tx=True)
            
            # Check that root is built
            if self.rootExists() == False:
                self.new()
            
            # Create command
            if self.moduleExists(name) == False:
                command = ("mod = " + str(module) + "." + str(module) + "('"+ name +"')")
                exec command
                
                mod.blueprint()
                self.Modules[mod.name] = mod
                if module != "NWRoot":
                    cmds.parent(mod.rootGrp, self.Modules["root"].groups["modules"])
                    cmds.container( self.Modules["root"].container, edit=True, an= mod.container)
            else:
                if module != "NWRoot":
                    print ("Module \"" + name + "\" already exists!")
                
        def rigModule(self,args):
            """
                Run rig method for module
            """
            # get module name
            defaultArgs = {"name":"default"}
            functArgs =  util.defaultArgs( defaultArgs,  args)
            name = functArgs["name"]
            
            # Check that root is built
            if self.rootExists() == False:
                cmds.error("Root container not found during rig")
            self.refreshModuleList()
            
            # check module exists and rig has not been run
            if self.moduleExists(name) and self.checkMethod(name, "rig"):
                mod = self.Modules[name]
                mod.rig()
            else:
                print ("Module \"" + name + "\" already built!")
                
        def refreshModuleList(self):
            """
                Clears and refreshes module instances
            """
            rootCnt = (self.name + "_CNT")
            rootModule = {}
            # check if module list is empty
            if len(self.Modules) == 0:
                # Find root and find it's children
                if self.rootExists():
                    # populate module list
                    rootModule["root"] = self.reloadModule(rootCnt)
                    childModules = self.getContainerChildren(rootCnt)
                    self.Modules = util.defaultArgs( rootModule,  childModules)
                else:
                    smds.error("Root containter not found for refresh")
        # ------------------------      
        # Container functions
        # ------------------------
        def getModuleContainers(self):
            """
                returns list of all container modules
            """
            rootCnt = ""
            containerList= []
            # Get root container
            if self.rootExists():
                containerList.append( self.getRootModuleContainer() )
                contents= cmds.container(containerList[0], query= True, nodeList= True)
                if contents == None:
                    return containerList
                for item in contents:
                    if cmds.objectType(item) == "container":
                        containerList.append( item )
                return containerList
                
            return containerList
                
        def getContainerChildren(self,cont):
            """
                Finds all children containers of passed container
            """
            containers = {}
            if cmds.objExists(cont):
                # populate module list
                contents = cmds.container(cont, query= True, nodeList= True)
                if contents == None:
                    return containers
                for item in contents:
                    if cmds.objectType(item) == "container":
                        containers[util.removeSuffix(item)] = self.reloadModule(item)
                        # combine and overwrite lists
                        containers = dict(containers.items() + (self.getContainerChildren(item)).items())
                return containers
            else:
                cmds.error("Root containter not found for refresh")
        
        def reloadModule(self,module):
            """
                Gets data from container and rerigs python object
            """
            moduleType = util.getString(module, "type")
            command = ("module = " + str(moduleType) + "." + str(moduleType) + "('"+ util.removeSuffix(module) +"')")
            exec command
            return module
        # ------------------------      
        # input output functions
        # ------------------------
        def updateInputOutput(self):
            """
                iterates through modules updating inputs and puts
            """
            for module in self.Modules.keys():
                self.Modules[module].updateInputOutputs()
                
        
        def getInput(self,module,key):
            """
                Gets input from module
            """
            self.updateInputOutput()
            return self.Modules[module].inputs[key]
        
        def getOutput(self,module,key):
            """
                Gets input from module
            """
            self.updateInputOutput()
            return self.Modules[module].outputs[key]
            
        def updateConnectionData(self):
            """
                iterate through modules update data
            """
            for module in self.Modules:
                module.updateConnectionData()
        
        def createConnection(self, inputModule, connectionKey):
            """
                Connect objects based on connection data
            """
            inputModule = self.Modules[inputModule]
            # Check connection exists
            if not inputModule.connections.has_key(connectionKey):
                cmds.error("Connection data not found")
            inputPlug = inputModule.connections[connectionKey]["input"]
            outputPlug = inputModule.connections[connectionKey]["output"]
            connectionAttr = inputModule.connections[connectionKey]["connectAttr"]
            connectionDataAttr = (connectionAttr + "_data")
            
            inputModule = inputPlug.split(".")[0]
            outputModule = outputPlug.split(".")[0]
            
            inputKey = util.getSuffix( inputPlug.split(".")[1] )
            outputey = util.getSuffix( outputPlug.split(".")[1] )
            
            input = self.getInput(inputModule, inputKey)
            output = self.getOutput(outputModule, outputey)
            
            # Get connection data
            connectionData = cmds.getAttr( (inputModule + "_CNT." + connectionDataAttr) )
            attrName = connectionData[3]
            type = attrName = connectionData[1]
            
            if type == "trans":
                cmds.parentConstraint(output,input, mo= False)
            elif type == "transMo":
                cmds.parentConstraint(output,input, mo= True)
            elif type == "pos":
                cmds.pointConstraint(output,input, mo= False)
            elif type == "posMo":
                cmds.pointConstraint(output,input, mo= True)
            elif type == "rot":
                cmds.orientConstraint(output,input, mo= False)
            elif type == "rotMo":
                cmds.orientConstraint(output,input, mo= True)
            elif type == "scale":
                cmds.scaleConstraint(output,input)
            elif type == "matrix":
                util.matrixConstraint(output, input, 0, {})
            elif type == "matrixMo":
                util.matrixConstraint(output, input, 1, {})
            elif type == "attr":
                cmds.connectAttr(output, input, f= True)
            else:
                cmds.error( ("Connection type not found on connectionAttr: " + connectionAttr) )
            
        def storeConnection(self, connectionKey, inputkey, outputPlug , type, attrName= "none"):
            """
                Store connection between output to input on current module
            """
            
            pass

if __name__ == "__main__":
    print "Blueprinting test:"
    global NWRig
    NWRig = RigNW("nwRig")
