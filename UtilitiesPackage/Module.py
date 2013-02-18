import maya.cmds as cmds 

def getContainer( module):
	if moduleExists(module):
		return (module + "_CNT")
    
			
def moduleExists( name):
	if cmds.objExists(name + "_CNT"):
		return True
	else:
		return False
		
def getRegisteredObjects( module, registry):
	"""
		finds all registered blueprinter objects from containters
		registry is Attributeibute stored on containers connected to 
		desired objects
	"""
	registeredData =[]
	# Get container
	container = getContainer(module)
	if cmds.objExists( (container + "." + registry) ):
		registeredData = cmds.listConnections( (container + "." + registry) )
		if registeredData == None:
			registeredData = []
	else:
		registeredData = []
	return registeredData
