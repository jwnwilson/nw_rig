# -*- coding: utf-8 -*-

"""
To do:
- Need inhertance of modules - done
- Need to have multiple instances supported and namespaces for items in containers
- Lock starter joints only allow manipulation through controls
- Needs more sub controls for starters
- Starter direction needs to be influenced by other starter controls
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
    FILE_PATH = "C:/Documents and Settings/Noel Wilson/My Documents/Python/NWRig/"
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
            Manages project and loads gui / builds the rig
        """
        def __init__(self, name, **kwargs):
                classArgs = {"UIFile":"default.py","rebuildUI":True}
                #classArgs =  dict(classArgs.items() + kwargs.items())
                classArgs =  util.defaultArgs( classArgs,  kwargs)
                self.Modules = {}
                self.Connections = []
                self.name = name
                self.UIFile =  classArgs["UIFile"]
                if classArgs["rebuildUI"]:
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
        def loadStartData(self):
            """
                Loads start data onto starters
            """
            # open file from path in UI
            self.UI.getFilePath()
            filePath = (str(self.UI.filePath) + "start.txt")
            FILE = open(filePath,"rU")            
            
            for line in FILE:
                startDataLine = line.split()
                startObject = startDataLine[0]
                translate = [ float( startDataLine[1] ), float( startDataLine[2] ), float( startDataLine[3] ) ]
                rotate = [ float( startDataLine[4] ), float( startDataLine[5] ), float( startDataLine[6] ) ]
                scale = [ float( startDataLine[7] ), float( startDataLine[8] ), float( startDataLine[9] ) ]
                if cmds.objExists(startObject):
                    util.checkSetCompoundAttr( (startObject + ".t"), translate )
                    util.checkSetCompoundAttr( (startObject + ".r"), rotate )
                    util.checkSetCompoundAttr( (startObject + ".s"), scale )
            FILE.close()
            print ("Loaded start data from : " + filePath)
                    
        def saveStartData(self):
            """
                Loads start data onto starters
            """
            objects = self.getRegisteredObjects("regStartTransform")
            self.UI.getFilePath()  
            filePath = (str(self.UI.filePath) + "start.txt")
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
            startData = FILE.write(writeData)
            FILE.close()
            print ("Saving start data to : " + filePath)
            
        def getRegisteredObjects(self, registry):
            """
                finds all registered starter objects from containters
                registry is attribute stored on containers connected to 
                desired objects
            """
            starterTransforms =[]
            # Get all containers
            containers = self.getModuleContainers()
            # iterate through and get staters from attribute connections
            for container in containers:
                if cmds.objExists( (container + "." + registry) ):
                    containerStartTransforms = cmds.listConnections( (container + "." + registry) )
                    starterTransforms += containerStartTransforms
            return starterTransforms
        # ------------------------      
        # Module functions
        # ------------------------
        def new(self, **kwards):
            """
                create initial hierarchy for rig
            """
            self.__init__(self.name, rebuildUI = False)
            name = self.name
            rootMod = NWRoot.NWRoot(self.name)
            self.Modules["root"] = rootMod
            self.Modules[self.name] = rootMod
            self.Modules["root"].start()
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
                
        def getModule(self, name):
            if cmds.objExists(name + "_CNT"):
                return (name + "_CNT")
            else:
                return ""
                
        def getRootModule(self):
            return self.getModule(self.name)
        
        def checkMethod(self,name, method):
            """
                Check method variable set after completion
            """
            if method == "start" and self.Modules[name].startVar == 0:
                    return True
            if method == "build" and self.Modules[name].buildVar == 0:
                    return True
            return False
        def startModule(self,module):
            """
                Run start method for module
            """
            # get module name
            windowElement = self.UI.inputs["startTextField"]
            name = cmds.textField(windowElement.fullPath, q=True,tx=True)
            
            # Check that root is built
            if self.rootExists() == False:
                self.new()
            
            # Create command
            if self.moduleExists(name) == False:
                command = ("mod = " + str(module) + "." + str(module) + "('"+ name +"')")
                exec command
                try:
                    mod.start()
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                self.Modules[mod.name] = mod
                cmds.parent(mod.rootGrp, self.Modules["root"].groups["modules"])
                cmds.container( self.Modules["root"].container, edit=True, an= mod.container)
            else:
                print ("Module \"" + name + "\" already exists!")
                
        def buildModule(self,args):
            """
                Run build method for module
            """
            # get module name
            defaultArgs = {"name":"default"}
            functArgs =  util.defaultArgs( defaultArgs,  args)
            name = functArgs["name"]
            
            # Check that root is built
            if self.rootExists() == False:
                    cmds.error("Root container not found during build")
            self.refreshModuleList()
            
            # check module exists and build has not been run
            if self.moduleExists(name) and self.checkMethod(name, "build"):
                try:
                    mod = self.Modules[name]
                    mod.build()
                except:
                    print "Unexpected error:", sys.exc_info()
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
                containerList.append( self.getRootModule() )
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
                Gets data from container and rebuilds python object
            """
            moduleType = util.getString(module, "type")
            command = ("module = " + str(moduleType) + "." + str(moduleType) + "('"+ util.removeSuffix(module) +"')")
            exec command
            return module
            
if __name__ == "__main__":
    print "Starting test:"
    global NWRig
    NWRig = RigNW("nwRig")
