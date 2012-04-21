import os 
import sys

def addSysPaths(paths):
    """
        Adds paths to sys.path global variable if they aren't being used
    """
    for path in paths:
            if path not in sys.path:
                    sys.path.append( path )
            #for lib in LIBRARIES:
            #        if ( path + lib) not in sys.path:
            #                sys.path.append( path + lib)

# Moving to utilities file
def importModule(name):
    print ("Importing : " + name )
    try:
        __import__(name)
    except ImportError:
        print ("Error importing :" + name)
        
def loadModule(module_name):
    """
	    Will see if module is loaded and import it or reload it 
	    respectively
    """
    try:
    	if globals().has_key(module_name):
    	    	print ("Reloading : " + module_name )
    	    	reload( globals()[module_name] )
    	else:
    	    	print ("Importing : " + module_name )
    	    	globals()[module_name] = __import__(module_name)
    except ImportError:
        print ("Error loading :" + module_name)

def import_libs(dir):
    """ Imports the libs, returns a list of the libraries. 
    Pass in dir to scan """
    
    library_list = {} 
    
    for f in os.listdir(os.path.abspath(dir)):
        module_name, ext = os.path.splitext(f) # Handles no-extension files, etc.
        if ext == '.py': # Important, ignore .pyc/other files.
            print 'importing module: %s' % (module_name)
            loadModule(module_name)
            #globals()[module_name] = __import__(module_name)
            #reload( globals()[module_name] )
            library_list[module_name] = globals()[module_name]
 
    return library_list

def import_packages(dir):
    """ Imports the packages, returns a list of the libraries. 
    Pass in dir to scan """
    
    library_list = {} 
    
    for d in os.listdir(os.path.abspath(dir)):
        package_name, ext = os.path.splitext( d ) # Handles no-extension files, etc.
        if ext == '' and os.path.isdir( dir+ "/" + package_name): # Important, ignore .pyc/other files.
            if "__init__.py" in os.listdir( os.path.abspath(dir + "/" + package_name + "/") ):
                print 'importing package: %s' % (package_name)
                if (dir  + d + "/") not in sys.path:
                        sys.path.append( dir + d + "/" )
		loadModule(package_name)
                #globals()[package_name] = __import__(package_name)
                #reload( globals()[package_name] )
                library_list[package_name] = globals()[package_name]
 
    return library_list
