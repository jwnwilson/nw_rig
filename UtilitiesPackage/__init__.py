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
	exec "from %s import *" % module

def mayaImport( module ):
	"""
		Trick to import and reload modules to avoid restarting maya
		during debugging
	"""
	exec "import %s " % module
	exec "reload( %s )" % module

def mayaFromImport( modulePath, module ):
	"""
		Trick to import and reload modules to avoid restarting maya
		during debugging
	"""
	exec "from %s import %s" % (modulePath, module)
	exec "reload( %s )" % module

for module in package_contents("UtilitiesPackage"):
	if module != "__init__":
		mayaImportAll( module )

