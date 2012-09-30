# -*- coding: utf-8 -*-

import maya.cmds as cmds
import Window
import sys
import os

import UtilitiesPackage.Util as Util
import String

# Need to import all module data for attribute reading
from Module import Module
from HingeJoints import HingeJoints
from SpineJoints import SpineJoints

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
		functArgs =	 Util.defaultArgs( defaultArgs, args)
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
		functArgs =	 Util.defaultArgs( functArgs, {"append": moduleList} )
		
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
		indent = "	 "
		
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
		#name = cmds.textField(windowElement.fullPath, q=True,tx=True)
		
		# load attributes
		self.rigInstance.createModule(name,blueprintModule )
		self.setAttributesFromUI( name, "blueprint")
		self.rigInstance.blueprintModule(name, blueprintModule)
	
	def setAttributesFromUI(self,name, method):
		"""
			Sets attributes on module
		"""
		# Load every other UI element
		UIAttrArray = eval('self.'+ method + 'AttributeUIElements')
		moduleAttributes = eval('self.rigInstance.Modules[name].'+ method + 'Attributes')
		count = 0
		for key in UIAttrArray.keys()[1::2]:
			value = self.queryInput(key)
			moduleAttributes[count].value = value
			count += 1
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
				self.loadBlueprintAttributes(args["module"])
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
			if selectedModule:
				# Get selected element
				selectedModule = Util.getFirst(selectedModule)
				# Load selected objects attributes
				self.loadRigAttributes(selectedModule.strip())
		else:
			pass
	 
	def loadRigAttributes(self, module):
		"""
			Will load attributes of module in gui
		"""
		# Load module name
		if self.windowElements.has_key("rigAttrTitle") == False:
			self.text({"key":"rigAttrTitle",'label':'rig module name','parent':"rigAttributeframe"})
		if self.windowElements.has_key("rigAttrName") == False:
			self.text({"key":"rigAttrName",'label':module,'parent':"rigAttributeframe"})
		else:
			self.editElement("rigAttrName",label= module)
		
		# Clear rig attr
		for key in self.rigAttributeUIElements.keys():
			self.removeElement(key)
			del self.rigAttributeUIElements[key]
		if self.windowElements.has_key("rigAttributeForm"):
			self.removeElement("rigAttributeForm")
		self.rigAttributeUIElements = {}
		
		# Read module attributes
		rigAttr = self.rigInstance.Modules[String.removeSuffix(module)].rigAttributes
		for attr in rigAttr:
			# save blueprint attr UI element
			self.text({'key':(module + attr.name + 'text'),'label':attr.name,'parent':'rigAttributeframe'})
			self.textField({'key':(module + attr.name),'label':attr.defaultValue,'parent':'rigAttributeframe'})
			# save to printattrbuteUIDict
			key = (module + attr.name + 'text')
			self.rigAttributeUIElements[key] = self.windowElements[key]
			key = (module + attr.name)
			self.rigAttributeUIElements[key] = self.windowElements[key]
			
		# arrange in UI
		self.createOrganisedForm("rigAttributeForm",self.rigAttributeUIElements.keys(),"rigAttributeframe" )
		
	def loadBlueprintAttributes(self, module):
		"""
			Will load attributes of module in gui
		"""
		if self.windowElements.has_key("blueprintModuleName") == False:
			self.text({"key":"blueprintModuleName",'label': module,'parent':"blueprintAttributeframe"})
		else:
			self.editElement("blueprintModuleName",label= module)
			
		# Clear blueprint attr
		for key in self.blueprintAttributeUIElements.keys():
			self.removeElement(key)
			del self.blueprintAttributeUIElements[key]
		if self.windowElements.has_key("blueprintAttributeForm"):
			self.removeElement("blueprintAttributeForm")
		self.blueprintAttributeUIElements = {}
		
		# Read module attributes
		blueprintAttr = eval(module + '.blueprintAttributes')
		for attr in blueprintAttr:
			# save blueprint attr UI element
			textKey = (module + attr.name + 'text').replace(' ', '')
			attrKey = (module + attr.name).replace(' ','')
			self.text({'key':textKey,'label':attr.name,'parent':'blueprintAttributeframe'})
			self.textField({'key':attrKey,'label':attr.defaultValue,'parent':'blueprintAttributeframe'})
			# save to printattrbuteUIDict
			self.blueprintAttributeUIElements[textKey] = self.windowElements[textKey]
			self.blueprintAttributeUIElements[attrKey] = self.windowElements[attrKey]
			
		# arrange in UI
		self.createOrganisedForm("blueprintAttributeForm",self.blueprintAttributeUIElements.keys(),"blueprintAttributeframe" )
		
		self.editElement("blueprintTextField",tx= module)
		
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
			self.editElement( "connectInputButton",	 l= module)
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
		connectionKey = ""
		# get Input
		inputKey = Util.getFirst(self.queryInput(connectInputIconTextScroll))
		# get Output
		outputKey = Util.getFirst(self.queryInput(connectOutputIconTextScroll))
		
		connectionKey = (outputKey + "_" + inputKey)
		
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
			
		selectedModule = Util.getFirst(self.queryInput("rigList"))
		selectedModule = String.removeSuffix(selectedModule.strip())
		self.createValueWindow("Enter new module name", "default","NWRig.duplicateModule(\""+selectedModule+"\", %)")
		self.loadModules({})

# just some testing
if __name__ == "__main__":
	test = RigUI({})
