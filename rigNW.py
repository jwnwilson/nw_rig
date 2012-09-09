# -*- coding: utf-8 -*-
"""
To do:
- Need to have multiple instances supported and namespaces for items in containers
    - Save overal rig in file re-import with namespace
- All inputs and outputs refreshed when connection queried can be optimised
- All components must be stored in containers
- Require rename option
- Create a defomation menu / skinning menu

- Require a pickle / refresh python module data function so scene data can be reloaded into tool
- Create String array data loader format - ["key:", "data", "data"]
- Create menu
    - New are you sure box
    - Save rig / all data
    - Load rig / all data             
- Blueprint Menu 
    - Blueprint attributes
    - cleaner menu
    - mirror function
        - select blue print and mirror it
    - Save as blueprint
- Rig Menu - Done
    - Rig module attributes
    - Save
        - save control shapes
        - save connections between objects
        - Clean up rig data connection function
- Connection menu
    - parenting module
    - multiple connection types
- Deformation menu

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
import copy
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
source packages
"""
import NWUtilitiesPackage.NWUtilitiesFile as fileUtil
import NWUtilitiesPackage.NWUtilities as util
reload(fileUtil)
reload(util)

"""
Dynamic importing of modules
"""
PACKAGES = fileUtil.import_packages( FILE_PATH )
for key in PACKAGES.keys():
    globals()[key] = PACKAGES[key]

# import utilities with new short names
exec NWUtilitiesPackage.NWUtilities.importUtilitiesShortNames()

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
        def checkAndCreateRigFolders(saveFunction):
            """
                Wrapper for save functions to check and create rig folders if necessary
            """
            @wraps(saveFunction)
            def wrapper(self,*args, **kwds):
                fileUtil.createRigFolders(self.UI.getFilePath())
                ret = saveFunction(self,*args, **kwds)
                return ret
            return wrapper
            
        def checkRigFolders(loadFunction):
            """
                Wrapper for load functions to check for rig folders
            """
            @wraps(loadFunction)
            def wrapper(self,*args, **kwds):
                if fileUtil.checkRigFolderExists(self.UI.getFilePath()) == False:
                    cmds.error("Unable to find folders for rig to load from.")
                ret = loadFunction(self,*args, **kwds)
                return ret
            return wrapper
            
        @checkAndCreateRigFolders
        def saveRig(self):
            """
                Will save current rig if built in file
            """
            # Check all modules are in rig mode
            modules = self.Modules.keys()
            for module in modules:
                if self.Modules[module].rigMode() != 1:
                    cmds.error("Cannot save rig as not all modules are in rig mode")
            # If file exists prompt warning
            defaultFilePath = ( self.UI.getFilePath() + "rigFile/" + self.name )
            deatultFolderPath = ( self.UI.getFilePath() + "rigFile/" )
            
            # If folder doesn't exist create
            if os.path.exists( deatultFolderPath ) == False :
                os.makedirs( deatultFolderPath )
            
            cmds.file( rename= defaultFilePath )
            if os.path.exists( (defaultFilePath + ".ma") ):
                # prompt and save / exit
                self.UI.createPromptWindow("Overwrite old save?",("cmds.file( save = True, type='mayaAscii' )\nprint ( \"Rig saved to: " + defaultFilePath+ ".ma\")") )
            else:
                # Save file
                cmds.file( save = True, type='mayaAscii' )
                print ( "Rig saved to: " + defaultFilePath + ".ma")
                
        @checkRigFolders
        def loadRig(self):
            """
                Will load current rig from file
            """
            # If file exists prompt warning
            # Load file
            defaultFilePath = ( self.UI.getFilePath() + "/rigFile/" + self.name)
            
            if os.path.exists( (defaultFilePath + ".ma") ):
                if cmds.file( q=True, modified=True):
                    # prompt and save / exit
                    self.UI.createPromptWindow("Discard changes?",("cmds.file(\""+ defaultFilePath + ".ma\", o = True, f = True)\nprint ( \"Rig loaded from: " + defaultFilePath + ".ma\")") )
                else:
                    cmds.file( (defaultFilePath + ".ma") , o = True)
                    print ( "Rig loaded from: " + defaultFilePath + ".ma")
            else:
                cmds.error("Rig file not found.")
            
        @checkAndCreateRigFolders
        def saveAllData(self):
            """
                Saves all blueprint and rig data
            """
            self.saveBlueprintData()
            self.saveRigData()
            
        @checkRigFolders
        def loadAllData(self):
            """
                Load all blueprint and rig data
            """
            self.loadBlueprintData()
            self.loadRigData()
            
        @checkRigFolders
        def loadBlueprintData(self, modules = None):
            """
                Loads blueprint data onto blueprinter
            """
            if modules == None:
                modules = self.getModules()
            
            # open file from path in UI
            self.UI.getFilePath()
            for module in modules:
                # Load transforms
                filePath = (str(self.UI.filePath) + module + "BlueprintData.txt")
                util.loadTransforms(filePath)
                # Load attributes
            print ("Blueprint data loaded")
            
        @checkAndCreateRigFolders
        def saveBlueprintData(self, modules = None ):
            """
                Saves blueprint data into file
            """
            if modules == None:
                modules = self.getModules()
            
            # refresh UI path
            self.UI.getFilePath()  
            bluePrintFilePath = (str(self.UI.filePath) + "BlueprintData.txt")
            # Save module data
            util.saveBlueprintModuleData( bluePrintFilePath, modules )
            # Save detailed info in seperate files
            for module in modules:
                # Save blueprint transforms
                filePath = (str(self.UI.filePath) + module + "BlueprintData.txt")
                util.saveTransforms(filePath, module, self.getRegisteredObjects(module,"regBlueprintTransform") )
                # Save attribute data
            print ("Blueprint data saved")
            
        @checkAndCreateRigFolders
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
                    util.saveTransforms(regTransFilePath, module,  self.getRegisteredObjects(module,"regRigTransform") )
                # Save shapes
                if "regRigShapes" in registeredAttrs:
                    regTransFilePath = (str(self.UI.filePath) + module + "RigShapeData.txt")
                    util.saveShapes(regTransFilePath, module,  self.getRegisteredObjects(module,"regRigShapes") )
                
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
            
        @checkRigFolders
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
                endModuleIndice = util.readRigNextModule(fileIndice, lineArray)
                connections = util.readRigConnectionData(startModuleIndice, endModuleIndice , lineArray)
                registeredAttr = util.readRigRegisteredAttr(startModuleIndice, endModuleIndice , lineArray)
                fileIndice = endModuleIndice
                
                # Load registered Attr data
                for regAttr in registeredAttr:
                    if regAttr.split(".")[1] == "regRigShape":
                        regShapeFilePath = (str(self.UI.filePath) + module + "RigShapeData.txt")
                        util.loadShapes(regShapeFilePath)
                    if regAttr.split(".")[1] == "regRigTransform":
                        regTransFilePath = (str(self.UI.filePath) + module + "RigTransData.txt")
                        util.loadTransforms(regTransFilePath)
                
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
            #self.loadBlueprintData()
                
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
            #self.loadRigData()
            
        def blueprintModule(self, name ,module):
            """
                Run blueprint method for module
            """            
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
        
        def renameModule(self, module, name):
            """
                Renames module
            """
            # Rename container and all module components
            moduleContainer = self.Modules[module].container
            moduleList = cmds.container( (moduleContainer), query= True, nodeList= True )
            # Rename module instance and dictionary keys
            for obj in moduleList:
                if cmds.objExists(obj):
                    newName = obj.replace(module, name )
                    cmds.rename(obj, newName)
            newName = moduleContainer.replace(module, name )
            cmds.rename(moduleContainer, newName) 
            # Change dict entry in NWRig instance
            self.Modules[string.removeSuffix(newName)] = copy.deepcopy(self.Modules[module])
            self.Modules[string.removeSuffix(newName)].container = newName
            del self.Modules[module]
        
        def deleteModule(self, module):
            """
                Deletes module
            """
            moduleContainer = self.Modules[module].container
            moduleList = cmds.container( (moduleContainer), query= True, nodeList= True )
            
            cmds.delete(moduleList)

if __name__ == "__main__":
    print "Blueprinting test:"
    global NWRig
    NWRig = RigNW("nwRig")
