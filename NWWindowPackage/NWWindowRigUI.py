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
		
	def loadSymbolButton(self, module, icon, moduleData):
		""" 
			Load symbolButton
		"""
		rowArgs = {"key": (module + "SymbolRow"),
				"parent": "startScroll",
				'label':(module),
				'type':'rowLayout'}
		buttonArgs = {"key": (module + "SymbolButton"),
						"image": icon, 
						"command": ( "NWRig" + ".UI.updateStartAttributes({\"module\": \"" + module + "\"})"),
				"parent": (module + "SymbolRow") }
		textArgs = {"key": (module + "SymbolText"),
				"parent": (module + "SymbolRow"),
				"label" : moduleData}
		#functArgs =  util.defaultArgs( defaultArgs, args)
		
		#Create start icon
		symbolFrame = self.layout(rowArgs)
		symbolBut = self.symbolButton(buttonArgs)
		symbolText = self.text(textArgs)		
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
			self.loadSymbolButton(args[0],(iconPath + args[1].rstrip()), (" ".join(args[2:])) )
		FILE.close()
		
	def loadModules(self,args,**kwargs):
		""" 
			Load text in list for each module available
		"""
		defaultArgs = {"key": "buildList",
						"parent": "buildScroll"}
		functArgs =	 util.defaultArgs( defaultArgs, args)
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
		functArgs =	 util.defaultArgs( functArgs, {"append": moduleList} )
		
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
		indent = "	 "
		
		moduleList.append(rootContainer)
		
		children = cmds.container( (rootContainer), query= True, nodeList= True )
		if children == None:
			return moduleList
		for child in children:
			decendants = self.recursiveGetModules(child)
			for decendant in decendants:
				decendant = (indent + decendant) 
				moduleList.append(decendant)
		
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
	
	def startModules(self):
		"""
		Run start method for selected module
		"""
		startModule = self.queryElement("startModuleName")
		self.NWRigInstance.startModule(startModule)
		
			
	def updateStartAttributes(self,args):
		"""
			Gets selected module and lists attributes
		"""
		functArgs = util.defaultArgs({}, args )
		# Check startIconScroll element exists
		if self.windowElements.has_key("startAttributeframe"):
			# Load selected objects attributes
				self.loadStartAttributes(args["module"])
		else:
			pass
		
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
				self.loadBuildAttributes(selectedModule.strip())
		else:
			pass
	 
	def loadBuildAttributes(self, module):
		"""
			Will load attributes of module in gui
		"""
		if self.windowElements.has_key("buildAttrTitle") == False:
			self.text({"key":"buildAttrTitle",'label':'build module name','parent':"buildAttributeframe"})
		if self.windowElements.has_key("buildAttrName") == False:
			self.text({"key":"buildAttrName",'label':module,'parent':"buildAttributeframe"})
		else:
			self.editElement("buildAttrName",label= module)
			
	def loadStartAttributes(self, module):
		"""
			Will load attributes of module in gui
		"""
		if self.windowElements.has_key("startModuleName") == False:
			self.text({"key":"startModuleName",'label': module,'parent':"startAttributeframe"})
		else:
			self.editElement("startModuleName",label= module)
			
		self.editElement("startTextField",tx= module)
		
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
	def connectPopupMenus(self, inputkey, outputkey):
		"""
			Builds connect popup menus
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
		moduleList = self.NWRigInstance.getModuleContainers()
		for module in moduleList:
			moduleName = util.removeSuffix(module)
			key = (moduleName + connetionType + "MenuItem")
			kwargs["command"] = ("NWRig.UI.setConnectionModule(\"" + moduleName + "\",\"" + connetionType + "\")")
			# clear popup menu
			if self.elementExists(key):
				self.removeElement(key)
			moduleMenuItem = self.menuItem({'key':key,'label':module,'parent':popupKey}, **kwargs)	
	
	def setConnectionModule(self, module, connectionType):
		"""
			Will create list of connections for selected module
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
		connectInputIconTextScroll = ("connect" + connectionType + "iconTextScroll")
		connectParent = ("connect" + connectionType + "Scroll")
		key = ""
		# Get module 
		module = ""
		if connectionType == "Input":
			module = self.queryElement("connectInputButton")
		else:
			module = self.queryElement("connectOutputButton")
		
		containerName = (module + "_CNT")
		
		# Get module connections
		connectionList = []
		
		# Add create functArgs
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
	
	
	#def buildModule(self,args):
	#	 """
	#		 Get selected module and build them
	#	 """
	#	 functArgs = {"name": "default"}
	#	 functArgs =  dict(functArgs.items() + args.items())
	#	 self.NWRigInstance.buildModule( functArgs )

# just some testing
if __name__ == "__main__":
	test = NWWindowRigUI({})
