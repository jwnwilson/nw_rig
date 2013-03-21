# -*- coding: utf-8 -*-
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
Add python directory to sys.path if necessary
"""
global FILE_PATH 
FILE_PATH = os.path.dirname(os.path.realpath(__file__)).replace('RigSystem','')
if FILE_PATH not in sys.path:
	sys.path.append( FILE_PATH )
	
	

"""
source file packages
"""
import UtilitiesPackage as Util
import WindowPackage as wp
import ModulePackage as mp

reload(Util)
reload(mp)
reload(wp)

#from ModulePackage import *

class Command:
	def __init__(self,name): 
		self.name = name
				
# Main application object
class NWRigSystem:
	"""
		Manages project and loads gui / rigs the rig
	"""
	def __init__(self, name, **kwargs):
		classArgs = {"UIFile":"defaultBP.py","rerigUI":True}
		classArgs =  Util.defaultArgs( classArgs,  kwargs)
		
		self.Modules = {}
		self.connections = {}
		self.name = name
		self.UIFile =  classArgs["UIFile"]
		self.loadSaveSystem = None
		self.bluePrintSystem = None
		self.buildSystem = None
		self.connectSystem = None
		
		if classArgs["rerigUI"]:
			self.UI = self.initialiseUI()
			
	def initialiseUI(self):
		""" 
			read in UIFile
		"""
		
		windowDir = wp.__path__
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
			Util.createRigFolders(self.UI.getFilePath())
			ret = saveFunction(self,*args, **kwds)
			return ret
		return wrapper
		
	def checkRigFolders(loadFunction):
		"""
			Wrapper for load functions to check for rig folders
		"""
		@wraps(loadFunction)
		def wrapper(self,*args, **kwds):
			if Util.checkRigFolderExists(self.UI.getFilePath()) == False:
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
			self.UI.createPromptWindow("Overwrite old save?",("cmds.file( save = True, type='mayaAscii' )\nprint ( \"NWRig saved to: " + defaultFilePath+ ".ma\")") )
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
				self.UI.createPromptWindow("Discard changes?",("cmds.file(\""+ defaultFilePath + ".ma\", o = True, f = True)\nprint ( \"NWRig loaded from: " + defaultFilePath + ".ma\")") )
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
			Util.loadTransforms(filePath)
			# Load Attributeibutes
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
		Util.saveBlueprintModuleData( bluePrintFilePath, modules )
		# Save detailed info in seperate files
		for module in modules:
			# Save blueprint transforms
			filePath = (str(self.UI.filePath) + module + "BlueprintData.txt")
			Util.saveTransforms(filePath, module, Util.getRegisteredObjects(module,"regBlueprintTransform") )
			# Save Attributeibute data
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
			# get registered Attributeibutes
			writeData += (module + "\n")
			inputData = []
			outputData = []
			connectionsData = []
			regData = []
			registeredAttrs = self.Modules[module].getRegisteredAttributes()
			
			# save container data
			for regAttr in registeredAttrs:
				writeLine = ""
				Attribute = (self.Modules[module].container + "." + regAttr )
				AttributeType = cmds.getAttr(Attribute, type = True)
				AttributeData = ""
				if AttributeType != "message":
					AttributeData = cmds.getAttr(Attribute)
				
				# if Attribute == message store Attributeibute name and type
				if AttributeType == "message":
					writeLine += ( tab +  Attribute + " " + AttributeType ) 
				# if Attribute == string store Attributeibute name and data
				elif AttributeType == "stringArray":
					writeLine += ( tab + Attribute + " " + AttributeType)
					for data in AttributeData:
						writeLine+= (" " + data)
				# if Attribute == etc store Attributeibute name and data
				else:
					writeLine += ( tab +  Attribute + " " + AttributeType + " " + AttributeData ) 
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
				Util.saveTransforms(regTransFilePath, module,  Util.getRegisteredObjects(module,"regRigTransform") )
			# Save shapes
			if "regRigShapes" in registeredAttrs:
				regTransFilePath = (str(self.UI.filePath) + module + "RigShapeData.txt")
				Util.saveShapes(regTransFilePath, module,  Util.getRegisteredObjects(module,"regRigShapes") )
			
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
			endModuleIndice = Util.readRigNextModule(fileIndice, lineArray)
			connections = Util.readRigConnectionData(startModuleIndice, endModuleIndice , lineArray)
			registeredAttr = Util.readRigRegisteredAttr(startModuleIndice, endModuleIndice , lineArray)
			fileIndice = endModuleIndice
			
			# Load registered Attr data
			for regAttr in registeredAttr:
				if regAttr.split(".")[1] == "regRigShape":
					regShapeFilePath = (str(self.UI.filePath) + module + "RigShapeData.txt")
					Util.loadShapes(regShapeFilePath)
				if regAttr.split(".")[1] == "regRigTransform":
					regTransFilePath = (str(self.UI.filePath) + module + "RigTransData.txt")
					Util.loadTransforms(regTransFilePath)
			
			# Create connections
			for connection in connections:
				print connection
				connectionKey = Util.getValueFromDataString(connection, "connectionKey")
				inputPlug = Util.getValueFromDataString(connection, "input")
				outputPlug = Util.getValueFromDataString(connection, "output")
				type = Util.getValueFromDataString(connection, "type")
				Attribute = Util.getValueFromDataString(connection, "attr")
				
				self.Modules[module].storeConnection(connectionKey, inputPlug, outputPlug , type, Attribute)
				self.createConnection(module, connectionKey)
		
		print ("Loaded blueprint data from : " + filePath)
	
	# ------------------------		
	# Module functions
	# ------------------------
	def new(self, blueprint= True, **kwards):
		"""
			create initial hierarchy for rig
		"""
		self.__init__(self.name, rerigUI = False)
		name = self.name
		rootMod = mp.Root(self.name)
		self.Modules["root"] = rootMod
		self.Modules[self.name] = rootMod
		if blueprint:
			self.Modules["root"].blueprint()
			self.rootGrp = self.Modules["root"].rootGrp
	
	def rootExists(self):
		if Util.moduleExists(self.name):
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
			if Util.moduleExists(name):
				modules.append(name)
		return modules
		
			
	def getRootModuleContainer(self):
		return Util.getContainer(self.name)
	
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
		#	 cmds.error("Blueprint group not found for : " + moduleName)
		
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
		
		# Build blueprints from default file is sccene empty
		if self.rootExists():
			modules = self.getModules()
			for module in modules:
				self.undoRigMode(module)
		else:
			for line in lineArray:
				moduleName = line.split()[0]
				module = line.split()[1]
				# check modules exist
				if Util.moduleExists(moduleName) == False:
					self.createModule(moduleName,module )
					self.blueprintModule(moduleName,module )
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
		
	def createModule(self, name, module):
		"""
			Creates module instance
		"""
		# Check that root is built
		if self.rootExists() == False:
			if module == "Root":
				self.new(blueprint= False)
				return
			else:
				self.new()
		
		# Create command
		if Util.moduleExists(name) == False:
			command = ("mod = mp."+ str(module) + "('"+ name +"')")
			exec command
			self.Modules[mod.name] = mod
			
		else:
			if module != "Root":
				print ("Module \"" + name + "\" already exists!")
		
	def blueprintModule(self, name ,module):
		"""
			Run blueprint method for module
		"""	 
		if Util.moduleExists(name):
			if self.checkMethod( name,"blueprint"):
				self.Modules[name].blueprint()
				
				if module != "Root":
					cmds.parent(self.Modules[name].rootGrp, self.Modules["root"].groups["modules"])
					cmds.container( self.Modules["root"].container, edit=True, an= self.Modules[name].container)
			else:
				cmds.error("Blueprint already built for " + name)
		else:
			cmds.error("Module "+name+" not found in rig instance")
			
	def rigModule(self,args):
		"""
			Run rig method for module
		"""
		# get module name
		defaultArgs = {"name":"default"}
		functArgs =	 Util.defaultArgs( defaultArgs,	 args)
		name = functArgs["name"]
		
		# Check that root is built
		if self.rootExists() == False:
			cmds.error("Root container not found during rig")
		self.refreshModuleList()
		
		# check module exists and rig has not been run
		if Util.moduleExists(name) and self.checkMethod(name, "rig"):
			mod = self.Modules[name]
			mod.rig()
		else:
			print ("Module \"" + name + "\" already built!")
			
	def duplicateModule(self, moduleName, newModuleName):
		"""
			duplicated module for now only handles blueprint
		"""
		# duplicate blueprint module
		Util.duplicateBlueprint(moduleName, newModuleName)
		# copy instance
		self.Modules[newModuleName] = copy.deepcopy(self.Modules[moduleName])
		# rename instance data
		self.Modules[newModuleName].name = newModuleName
		self.Modules[newModuleName].rootGrp = (newModuleName + "Root_GRP")
		self.Modules[newModuleName].container = (newModuleName + "_CNT")
		
		joints = self.Modules[newModuleName].getBlueprinterJoints()
		for x in range(len(joints)):
			joints[x] = joints[x].replace(moduleName,newModuleName)
		self.Modules[newModuleName].storeBlueprinterJoints(joints)
		
	def mirrorModule(self, moduleName, newModuleName, axis):
		"""
			Duplciates and mirrors module default x-axis
		"""
		self.duplicateModule(moduleName, newModuleName)
		Util.mirrorBlueprint(newModuleName,axis)
		
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
				self.Modules = Util.defaultArgs( rootModule,  childModules)
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
					containers[Util.removeSuffix(item)] = self.reloadModule(item)
					# combine and overwrite lists
					containers = dict(containers.items() + (self.getContainerChildren(item)).items())
			return containers
		else:
			cmds.error("Root containter not found for refresh")
	
	def reloadModule(self,module):
		"""
			Gets data from container and rerigs python object
		"""
		moduleType = Util.getString(module, "type")
		command = ("module = " + str(moduleType) + "." + str(moduleType) + "('"+ Util.removeSuffix(module) +"')")
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
		
		inputKey = Util.getSuffix( inputPlug.split(".")[1] )
		outputey = Util.getSuffix( outputPlug.split(".")[1] )
		
		input = self.getInput(inputModule, inputKey)
		output = self.getOutput(outputModule, outputey)
		
		# Get connection data
		connectionData = cmds.getAttr( (inputModule + "_CNT." + connectionDataAttr) )
		AttributeName = connectionData[3]
		type = AttributeName = connectionData[1]
		
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
			Util.matrixConstraint(output, input, 0, {})
		elif type == "matrixMo":
			Util.matrixConstraint(output, input, 1, {})
		elif type == "Attribute":
			cmds.connectAttr(output, input, f= True)
		else:
			cmds.error( ("Connection type not found on connectionAttr: " + connectionAttr) )
	
	def storeConnection(self, connectionKey, inputkey, outputPlug , type, AttributeName= "none"):
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
		# Change dict entry in Rig instance
		self.Modules[Util.removeSuffix(newName)] = copy.deepcopy(self.Modules[module])
		self.Modules[Util.removeSuffix(newName)].container = newName
		del self.Modules[module]
	
	def deleteModule(self, module):
		"""
			Deletes module
		"""
		moduleContainer = self.Modules[module].container
		moduleList = cmds.container( (moduleContainer), query= True, nodeList= True )
		
		cmds.delete(moduleList)

if __name__ == "__main__":
	print "Starting test:"
	global NWRig
	NWRig = NWRigSystem("nwRig")
