# -*- coding: utf-8 -*-

import maya.cmds as cmds
from NWWindow import *
import sys
import os

"""
To do:
   - Rewrite entire module store full path to every entity by a key
   - Every entity requires a key and a parent
   - Store list of all inputs
   - Use **kwargs correctly
"""

# temp addition to python path variable
ICON_PATH = "/icons"

class NWWindowRigUI(NWWindow):
    """ Creates a class which will create and manage a UI wrapping around maya's
    functionallity
    """
    def initialise(self,args, **kwds):
        """
            NWWindowRigUI initalise function
        """
        self.NWRigInstance = None
        self.NWRigInstance = util.checkForKwarg("NWRig",args)
        self.filePath = ""
        
    def loadSymbolButton(self, module, icon, function):
        """ 
            Load symbolButton
        """
        defaultArgs = {"key": (module + "SymbolButton"),
                        "image": icon, 
                        "command": ( "NWRig" + "."+ function + "( '"+ module + "')") }
        #functArgs =  util.defaultArgs( defaultArgs, args)
        
        symbolBut = self.symbolButton(defaultArgs)
        
        return symbolBut
    
    def loadStartIcons(self):
        """ 
            Load icon for each module available
        """
        # get list of modules to load
        currentPath = os.path.dirname(__file__)
        filePath = (currentPath + "/ui/moduleList.txt")
        iconPath = (currentPath + "/icons/")
        FILE = open(filePath,"rb")
        for line in FILE:
            args = line.split(' ')
            self.loadSymbolButton(args[0],(iconPath + args[1].rstrip()), "startModule" )
        FILE.close()
        
    def loadModules(self,args,**kwargs):
        """ 
            Load text in list for each module available
        """
        defaultArgs = {"key": "buildList",
                        "parent": "buildScroll"}
        functArgs =  util.defaultArgs( defaultArgs, args)
        selectCommand = ("NWRig" + ".UI.updateBuildAttributes({})")
        rootContainer = ""
        iconTextScroll = ""
        moduleList = []
        
        # Overwrite select command
        kwargs["sc"] = selectCommand
        
        if self.NWRigInstance.rootExists():
            self.NWRigInstance.refreshModuleList()
            rootContainer = self.NWRigInstance.Modules["root"].name
        else:
            if self.elementExists(functArgs["key"]):
                return self.windowElements[functArgs["key"].fullPath]

        # Create list of modules in scene indent children
        moduleList = self.recursiveGetModules( (rootContainer + "_CNT") )
        
        # Add module list to funct args
        functArgs =  util.defaultArgs( functArgs, {"append": moduleList} )
        
        if self.elementExists(functArgs["key"]):
            combinedArgs = util.defaultArgs( functArgs, kwargs)
            combinedArgs.pop("key")
            iconTextScroll = self.editElement(functArgs["key"], ra= True)
            iconTextScroll = self.editElement(functArgs["key"], **combinedArgs)
        else:
            iconTextScroll = self.iconTextScrollList(functArgs, **kwargs)
        
        self.inputs[functArgs["key"]] = self.windowElements[functArgs["key"]]
        return iconTextScroll
        
    def recursiveGetModules(self,rootContainer):
        """
            Recursively find modules from root container
        """
        moduleList = []
        indent = "   "
        
        moduleList.append(rootContainer)
        
        children = cmds.container( (rootContainer), query= True, nodeList= True )
        if children == None:
            return moduleList
        for child in children:
            decendants = self.recursiveGetModules(child)
            for decendant in decendants:
                decendant = (indent + decendant) 
                moduleList.append(decendant)
        """for child in children:
            if cmds.objExists( child ):
                allChildren = (self.recursiveGetModules( child ))[1:]
                moduleList.append( indent + child )
                for grandChild in allChildren
                    moduleList.append( (indent*2) + grandChild )"""
        
        return moduleList
        
    def buildModules(self,args):
        """
            Get selected modules and build them recersively
        """
        moduleList= []
        
        selectedModule = util.getFirst(self.queryInput("buildList"))
        selectedModule = selectedModule.strip()
        moduleList = self.recursiveGetModules(selectedModule)
        
        for module in moduleList:
            moduleName = util.removeSuffix(module)
            moduleName = moduleName.strip()
            self.NWRigInstance.buildModule({"name": moduleName})
        
    def updateBuildAttributes(self,args):
        """
            Gets selected module and lists attributes
        """
        functArgs = util.defaultArgs({}, args )
        # Check buildIconScroll element exists
        if self.inputs.has_key("buildList"):
            selectedModule = self.queryInput("buildList")
            if selectedModule:
                # Get selected element
                selectedModule = util.getFirst(selectedModule)
                # Load selected objects attributes
                self.loadAttributes(selectedModule.strip())
        else:
            pass
     
    def loadAttributes(self, module):
        """
            Will load attributes of module in gui
        """
        if self.windowElements.has_key("buildAttrTitle") == False:
            self.text({"key":"buildAttrTitle",'label':'build module name','parent':"buildAttributeframe"})
        if self.windowElements.has_key("buildAttrName") == False:
            self.text({"key":"buildAttrName",'label':module,'parent':"buildAttributeframe"})
        else:
            self.editElement("buildAttrName",label= module)
        
    def getFilePath(self):
        """
            will get file path from text field
        """
        textFieldInput = ""
        if self.windowElements.has_key("createFilePath"):
            textFieldInput = self.queryInput("createFilePath")
            self.filePath = textFieldInput
        else:
            cmds.error("Create file path text field not found")
    
    #def buildModule(self,args):
    #    """
    #        Get selected module and build them
    #    """
    #    functArgs = {"name": "default"}
    #    functArgs =  dict(functArgs.items() + args.items())
    #    self.NWRigInstance.buildModule( functArgs )

# just some testing
if __name__ == "__main__":
    test = NWWindowRigUI({})
