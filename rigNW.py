# -*- coding: utf-8 -*-

"""
To do:
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
#LIBRARIES = []
PACKAGES ={}

if os.name == 'posix':
        FILE_PATH = "/media/WALKMAN/Python/NWRig/"
elif os.name == 'nt':
        FILE_PATH = "F:\Documents and Settings\Noel Wilson\My Documents\Git\NWRig"
ROOT_PATH.append(FILE_PATH)

def addSysPaths(paths):
    """
        Adds paths to sys.path global variable if they aren't being used
    """
    for path in paths:
            if path not in sys.path:
                    sys.path.append( path )

"""
source utilities first remove duplicate code in __init__
source packages
"""
addSysPaths(ROOT_PATH)
 
import NWUtilitiesPackage.NWFileUtilities as fileUtil
import NWUtilitiesPackage.NWUtilities as util

PACKAGES = fileUtil.import_packages(ROOT_PATH[0])
for key in PACKAGES.keys():
	globals()[key] = PACKAGES[key]

class Command:
        def __init__(self,name): 
                self.name = name
                
# contains rig system
class RigNW:
        def __init__(self, name, **kwargs):
                classArgs = {"UIFile":"default.txt","rebuildUI":True}
                classArgs =  dict(classArgs.items() + kwargs.items())
                self.Modules = {}
                self.Connections = []
                self.name = name
                self.UIFile =  classArgs["UIFile"]
                if classArgs["rebuildUI"]:
                    self.UI = self.initialiseUI()
                
        def initialiseUI(self):
            # window = NWWindowPackage.NWWindow.NWWindow({})
            # read in UIFile
            windowDir = NWWindowPackage.__path__
            filePath = (windowDir[0] + "/blueprints/" +self.UIFile)
            FILE = open(filePath,"rU")
            command = FILE.read()
            FILE.close()
            
            exec command
            
            return window
            
        def new(self, **kwards):
            # create overal hierarchy for rig
            # get name of rig
            self.__init__(self.name, rebuildUI = False)
            name = self.name
            rootMod = NWModulePackage.NWRoot.NWRoot(self.name)
            self.Modules["root"] = rootMod
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
        def checkMethod(self,name, method):
                # Check method variable set after completion
                if method == "start" and self.Modules[name].startVar == 0:
                        return True
                if method == "build" and self.Modules[name].buildVar == 0:
                        return True
                return False
        def startModule(self,module):
            # Check that root is built
            if self.rootExists() == False:
                self.new()
            
            # get module name
            nameAttr = self.UI.inputs["starterName"]
            name = cmds.textField(nameAttr, q=True,tx=True)
            
            # create command
            if not self.moduleExists(name):
                command = ("mod = NWModulePackage." + str(module) + "." + str(module) + "('"+ name +"')")
                exec command
                
                mod.start()
                self.Modules[module] = mod
                cmds.parent(mod.rootGrp, self.Modules["root"].groups["modules"])
                cmds.container( self.Modules["root"].container, edit=True, an= mod.container)
            else:
                print "Module \"" + name + "\" already exists!";
        def buildModule(self,args):
                # Check that root is built
                if self.rootExists() == False:
                        cmds.error("Root container not found during build")
                self.refreshModuleList()
                
                # get module name
                functArgs = {"name":"default"}
                functArgs =  dict(functArgs.items() + args.items())
                name = functArgs["name"]
                
                # check module exists and build has not been run
                if self.moduleExists(name) and self.checkMethod(name, "build"):
                        mod = self.Modules[name]
                        mod.build()
                else:
                        print "Module \"" + name + "\" already built!";
        def refreshModuleList(self):
            # check if module list is empty
            if len(self.Modules) == 0:
                # Find root and find it's children
                if self.rootExists():
                    # populate module list
                    self.Modules = self.getContainerChildren((self.name + "_CNT"))
                    print self.Modules
                else:
                    smds.error("Root containter not found for refresh")
        # Container functions
        def getContainerChildren(self,cont):
            """
                Finds all children containers of passed container
            """
            containers = {}
            if cmds.objExists(cont):
                # populate module list
                contents = cmds.container(cont, query= True, nodeList= True)
                if contents:
                    for item in contents:
                        if cmds.objectType(item) == "container":
                            containers[util.removeSuffix(item)] = self.reloadModule(item)
                            containers = dict(containers.items() + (self.getContainerChildren(item)).items())
                return containers
            else:
                cmds.error("Root containter not found for refresh")
        def reloadModule(self,module):
            """
                Gets data from container and rebuilds python object
            """
            print "Problem here"
            moduleType = util.getString(module, "type")
            command = ("module = NWModulePackage." + str(moduleType) + "." + str(moduleType) + "('"+ util.removeSuffix(module) +"')")
            print command
            exec command
            return module
if __name__ == "__main__":
    #PACKAGES = import_packages(ROOT_PATH[0])
    print "Starting test:"
    global NWRig
    NWRig = RigNW("nwRig")
