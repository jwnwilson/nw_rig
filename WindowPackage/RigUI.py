# -*- coding: utf-8 -*-

import maya.cmds as cmds
import Window
import sys
import os

import UtilitiesPackage as Util
import UtilitiesPackage.String as String

# Need to import all module data for attribute reading
from ModulePackage.Module import Module
from ModulePackage.HingeJoints import HingeJoints
from ModulePackage.SpineJoints import SpineJoints

# Reload dependancies
reload(Window)

"""
To do:
   - Rewrite entire module store full path to every entity by a key
   - Every entity requires a key and a parent
   - Store list of all inputs
   - Remove attribute duplicate code
"""

# temp addition to python path variable
ICON_PATH = "/icons"
    
class RigUI(Window.Window):
    """ 
    Files a class which will file and manage a UI wrapping around maya's
    functionallity
    """
    def initialise(self,args, **kwds):
        """
            RigUI initalise function
        """
        self.rigInstance = None
        self.rigInstance = Util.checkForKwarg("Rig",args)
        self.filePath = ""
        self.blueprintAttributeUIElements = {}
        self.rigAttributeUIElements = {}
    
    def loadSymbolButton(self, module, icon, moduleData):
        """ 
            Load symbolButton
        """
        rowArgs = {"key": (module + "SymbolRow"),
                "parent": "blueprintScroll",
                'label':(module),
                'type':'rowLayout'}
        buttonArgs = {"key": (module + "SymbolButton"),
                        "image": icon, 
                        "command": ( "NWRig" + ".UI.updateBlueprintAttributes({\"module\": \"" + module + "\"})"),
                        "parent": (module + "SymbolRow") }
        textArgs = {"key": (module + "SymbolText"),
                "parent": (module + "SymbolRow"),
                "label" : moduleData}
        #functArgs =  Util.defaultArgs( defaultArgs, args)
        
        #File blueprint icon
        symbolFrame = self.layout(rowArgs)
        symbolBut = self.symbolButton(buttonArgs)
        symbolText = self.text(textArgs)        
        return symbolBut
    
    def loadBlueprintIcons(self):
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
            self.loadSymbolButton(args[0],(iconPath + args[1].rstrip()), (" ".join(args[2:])) )
        FILE.close()
        
    def loadModules(self,args,**kwargs):
        """ 
            Load text in list for each module available
        """
        defaultArgs = {"key": "rigList",
                        "parent": "rigScroll"}
        functArgs =  Util.defaultArgs( defaultArgs, args)
        selectCommand = ("NWRig" + ".UI.updateRigAttributes({})")
        rootContainer = ""
        iconTextScroll = ""
        moduleList = []
        
        # Overwrite select command
        kwargs["sc"] = selectCommand
        
        if self.rigInstance.rootExists():
            self.rigInstance.refreshModuleList()
            rootContainer = self.rigInstance.Modules["root"].name
        else:
            if self.elementExists(functArgs["key"]):
                return self.windowElements[functArgs["key"].fullPath]
            else:
                cmds.warning("No modules found in scene")
                return None

        # File list of modules in scene indent children
        moduleList = self.recursiveGetModules( (rootContainer + "_CNT") )
        
        # Add module list to funct args
        functArgs =  Util.defaultArgs( functArgs, {"append": moduleList} )
        
        if self.elementExists(functArgs["key"]):
            combinedArgs = Util.defaultArgs( functArgs, kwargs)
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
        cmds.select( children )
        children = cmds.ls(sl= True, type = "container")
        if children == None:
            return moduleList
        for child in children:
            decendants = self.recursiveGetModules(child)
            for decendant in decendants:
                decendant = (indent + decendant) 
                moduleList.append(decendant)
        
        return moduleList
        
    def rigModules(self,args):
        """
            Get selected modules and rig them recersively
        """
        moduleList= []
        
        if self.elementExists("rigList") == False:
            cmds.warning("No modules found in scene")
            return None
        
        selectedModule = Util.getFirst(self.queryInput("rigList"))
        selectedModule = selectedModule.strip()
        moduleList = self.recursiveGetModules(selectedModule)
        
        for module in moduleList:
            moduleName = Util.removeSuffix(module)
            moduleName = moduleName.strip()
            self.rigInstance.rigModule({"name": moduleName})
        # Load rig data
        self.rigInstance.loadRigData()
    
    def createBlueprintModule(self):
        """
        Run blueprint method for selected module
        """
        if self.elementExists("blueprintModuleName") == False:
            cmds.warning("Blueprinter module not selected.")
            return None
        blueprintModule = self.queryElement("blueprintModuleName")
        name = self.queryInput("blueprintTextField")
        
        # load attributes
        self.rigInstance.createModule(name,blueprintModule )
        self.setAttributesFromUI( name, "blueprint")                     
        self.rigInstance.blueprintModule(name, blueprintModule)
    
    def setAttributesFromUI(self,name, method):
        """
            Sets attributes on module
        """
        # Load every other UI element
        exec('UIAttrArray = self.'+ method + 'AttributeUIElements')
        exec('moduleAttributes = self.rigInstance.Modules[name].'+ method + 'Attributes')
        
        for key,moduleKey in zip(UIAttrArray.keys()[1::2],moduleAttributes.keys()):
            value = self.queryInput(key)
            moduleAttributes[moduleKey].value = value
            
    def renameModule(self):
        """
            Will rename current module
        """
        if self.elementExists("rigList") == False:
            cmds.warning("No modules found in scene")
            return None
        
        selectedModule = Util.getFirst(self.queryInput("rigList"))
        selectedModule = String.removeSuffix(selectedModule.strip())
        self.createValueWindow("Enter new module name", "default","NWRig.renameModule(\""+selectedModule+"\", %)")
        self.loadModules({})
        
    def deleteModule(self):
        """
            Deletes module
        """
        if self.elementExists("rigList") == False:
            cmds.warning("No modules found in scene")
            return None
        
        selectedModule = Util.getFirst(self.queryInput("rigList"))
        selectedModule = String.removeSuffix(selectedModule.strip())
        self.rigInstance.deleteModule(selectedModule)
        self.loadModules({})
        
    def updateBlueprintAttributes(self,args):
        """
            Gets selected module and lists attributes
        """
        functArgs = Util.defaultArgs({}, args )
        # Check blueprintIconScroll element exists
        if self.windowElements.has_key("blueprintAttributeframe"):
            # Load selected objects attributes
            self.loadAttributes('blueprint',args["module"])
            self.editElement("blueprintTextField",tx = args["module"])
        else:
            pass
        
    def updateRigAttributes(self,args):
        """
            Gets selected module and lists attributes
        """
        functArgs = Util.defaultArgs({}, args )
        # Check rigIconScroll element exists
        if self.inputs.has_key("rigList"):
            selectedModule = self.queryInput("rigList")
            print "selectedModule"
            print selectedModule
            if selectedModule:
                # Get selected element
                selectedModule = Util.getFirst(selectedModule)
                # Load selected objects attributes
                self.loadAttributes('rig',selectedModule.strip())
        else:
            pass
        
    def loadAttributes(self,type, module):
        """
            Will load attributes of module in gui
        """
        if type == "blueprint":
            moduleKey = "blueprintModuleName"
            frameKey = "blueprintAttributeframe"
            formKey = "blueprintAttributeForm"
            attributeVariable  = '.blueprintAttributes'
            attrElements = self.blueprintAttributeUIElements
            attributes = eval(module + attributeVariable)
        elif type == "rig":
            moduleKey = "rigModuleName"
            frameKey = "rigAttributeframe"
            formKey = "rigAttributeForm"
            attributeVariable  = '.rigAttributes'
            attrElements = self.rigAttributeUIElements
            attributes = self.rigInstance.Modules[String.removeSuffix(module)].rigAttributes
        else:
            cmds.error("type undefined for load attributes functions")
        
        if self.windowElements.has_key(moduleKey) == False:
            self.text({"key":moduleKey,'label': module,'parent':frameKey})
        else:
            self.editElement(moduleKey,label= module)
        
        # Clear attr
        for key in attrElements.keys():
            self.removeElement(key)
            del attrElements[key]
            if self.inputs.has_key(key):
                del self.inputs[key]
        if self.windowElements.has_key(formKey):
            self.removeElement(formKey)
        attrElements.clear()
        
        # Read module attributes
        for key in attributes.keys():
            attr = attributes[key]
            # save blueprint attr UI element
            textKey = (module + attr.name + 'text').replace(' ', '')
            attrKey = (module + attr.name).replace(' ','')
            self.text({'key':textKey,'label':attr.name,'parent':frameKey})
            self.textField({'key':attrKey,'label':attr.defaultValue,'parent':frameKey})
            # save to blueprintAttrbuteUIDict
            attrElements[textKey] = self.windowElements[textKey]
            attrElements[attrKey] = self.windowElements[attrKey]
            self.inputs[attrKey] = self.windowElements[attrKey]
        
        # arrange in UI
        self.createOrganisedForm(formKey,attrElements.keys(),frameKey )
        
    def queryAttribute(self, module, attr):
        """
            will get attribute data from UI
        """
        attrKey = (module + attr).replace(' ','')
        return self.queryInput(attrKey)
        
    def getAllAttributes(self, type, module):
        """
            returns all attributes in dict
        """
        if type == "blueprint":
            attributes = self.rigInstance.Modules[module].blueprintAttributes
        elif type == "blueprint":
            attributes = self.rigInstance.Modules[module].rigAttributes
        else:
            cmds.error("type undefined for get all attributes functions")
            
        ret = {}
        for attr in attributes:
            ret[attr] = self.queryAttribute(module,attr)
        return ret
        
    def getFilePath(self):
        """
            will get file path from text field
        """
        textFieldInput = ""
        if self.windowElements.has_key("fileFilePath"):
            textFieldInput = self.queryInput("fileFilePath")
            self.filePath = textFieldInput
            return self.filePath
        else:
            cmds.error("File file path text field not found")
    
    def connectPopupMenus(self, inputkey, outputkey):
        """
            Rigs connect popup menus
        """
        connectOutputPopup = self.popupMenu({'key':'connectOutputPopup','parent':outputkey} )
        connectInputPopup = self.popupMenu({'key':'connectInputPopup','parent':inputkey} )
        
        cmds.popupMenu(connectOutputPopup, e= True, pmc = ("NWRig.UI.populateConnectPopupMenu( \"" + connectOutputPopup + "\", \"Output\")") )
        cmds.popupMenu(connectInputPopup, e= True, pmc = ("NWRig.UI.populateConnectPopupMenu( \"" + connectInputPopup + "\", \"Input\")") )
    
    def populateConnectPopupMenu(self, popupKey, connetionType = "Input"):
        """
            Finds modules in scene and lists them in popup menu
        """
        kwargs = {}
        # get module list
        moduleList = self.rigInstance.getModuleContainers()
        for module in moduleList:
            moduleName = Util.removeSuffix(module)
            key = (moduleName + connetionType + "MenuItem")
            kwargs["command"] = ("NWRig.UI.setConnectionModule(\"" + moduleName + "\",\"" + connetionType + "\")")
            # clear popup menu
            if self.elementExists(key):
                self.removeElement(key)
            moduleMenuItem = self.menuItem({'key':key,'label':module,'parent':popupKey}, **kwargs)  
    
    def setConnectionModule(self, module, connectionType):
        """
            Will file list of connections for selected module
        """
        # Change name of button to module
        if connectionType == "Input":
            self.editElement( "connectInputButton",  l= module)
        else:
            self.editElement( "connectOutputButton",  l= module)
    
    def loadConnections(self, connectionType):
        """
            Loads connections of selected module 
        """
        # Input scroll list key 
        connectionList = []
        connectInputIconTextScroll = ("connect" + connectionType + "IconTextScroll")
        connectParent = ("connect" + connectionType + "Scroll")
        key = ""
        # Get module 
        module = ""
                
        # Get module connections
        self.rigInstance.updateInputOutput()
        
        if connectionType == "Input":
            module = self.queryElement("connectInputButton")
            command = ("connectionList = self.rigInstance.Modules[\""+module+"\"].inputs.keys()")
            exec command
        elif connectionType == "Output":
            module = self.queryElement("connectOutputButton")
            command = ("connectionList = self.rigInstance.Modules[\""+module+"\"].outputs.keys()")
            exec command
        else:
            cmds.error("connection type not defined")
        
        containerName = (module + "_CNT")
        
        # Add file functArgs
        functArgs = {"key": connectInputIconTextScroll, "append": connectionList,
                     "parent": connectParent}
        
        if self.elementExists(functArgs["key"]):
            key = functArgs.pop("key")
            iconTextScroll = self.editElement(key, ra= True)
            iconTextScroll = self.editElement(key, **functArgs)
        else:
            iconTextScroll = self.iconTextScrollList(functArgs)
            key = functArgs.pop("key")
        
        self.inputs[key] = self.windowElements[key]
        return iconTextScroll
    
    def connectOutputToInput(self):
        """
            Gets input and outputs from GUI and will connect them
        """
        type = "trans"
        connectInputIconTextScroll = "connectInputIconTextScroll"
        connectOutputIconTextScroll = "connectOutputIconTextScroll"
        connectOption = "connectConnectOptionMenu"
        connectionKey = ""
        # get Input
        inputKey = Util.getFirst(self.queryInput(connectInputIconTextScroll))
        # get Output
        outputKey = Util.getFirst(self.queryInput(connectOutputIconTextScroll))
        # get maintain offset
        connectionOption = self.queryInput(connectOption)
        
        connectionKey = (outputKey + "_" + inputKey)
        if connectionOption == 'Maintain offset':
        	type = "transMo"
        else:
        	type = "trans"
        
        # get Modules
        inputModule = self.queryElement("connectInputButton")
        outputModule = self.queryElement("connectOutputButton")
        
        # get input / output objects
        inputObj = self.rigInstance.getInput(inputModule, inputKey)
        outputObj = self.rigInstance.getOutput(outputModule, outputKey)
        
        inputPlug = (inputModule + "." + inputKey)
        outputPlug = (outputModule + "." + outputKey)
        
        # perform connection based on type
        self.rigInstance.Modules[inputModule].storeConnection(connectionKey, inputPlug, outputPlug , type)
        self.rigInstance.createConnection( inputModule , connectionKey )
    
    def duplicateBlueprint(self):
        """
            duplciates blueprint
        """
        if self.elementExists("rigList") == False:
            cmds.warning("No modules found in scene")
            return None
            
        selectedModule =self.queryInput("rigList")
        if not selectedModule:
            cmds.error("Select module to duplicate in rig menu.")
        selectedModule = Util.getFirst(selectedModule)
        selectedModule = String.removeSuffix(selectedModule.strip())
        self.createValueWindow("Enter new module name", "default","NWRig.duplicateModule(\""+selectedModule+"\", %)")
        self.loadModules({})
        
    def mirrorBlueprint(self):
        """
            duplciates blueprint
        """
        if self.elementExists("rigList") == False:
            cmds.warning("No modules found in scene")
            return None
            
        selectedModule =self.queryInput("rigList")
        if not selectedModule:
            cmds.error("Select module to duplicate in rig menu.")
        selectedModule = Util.getFirst(selectedModule)
        selectedModule = String.removeSuffix(selectedModule.strip())
        self.createValueWindow("Enter new module name", "default","NWRig.mirrorModule(\""+selectedModule+"\", %, 'x')")
        self.loadModules({})

# just some testing
if __name__ == "__main__":
    test = RigUI({})
