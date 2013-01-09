__all__ = [
		"File",
		"Attribute",
		"Blueprint",
		"Constraint",
		"Control",
		"Curve",
		"File",
		"Joint",
		"Lib",
		"ModuleUtil",
		"String",
		"Transform"
]

from UtilitiesPackage.File import package_contents

def mayaImportAll( module ):
	return "from %s import *" % module

def mayaImport( module ):
	"""
	return string to import module and reload it
	"""
	return ("import %s " % module + "\n" + "reload( %s )" % module)

def mayaFromImport( modulePath, module ):
	"""
	return string to import module and reload it
	"""
	return ("from %s import %s" % (modulePath, module) + "\n" + "reload( %s )" % module) 

for module in package_contents("UtilitiesPackage"):
	if module != "__init__":
		exec mayaImport( module )
		exec mayaImportAll( module )

