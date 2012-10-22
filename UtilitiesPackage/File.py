import os 
import sys
import maya.cmds as cmds

import Lib
import Attribute
import Transform
import Curve

def addSysPaths(paths):
    """
        Adds paths to sys.path global variable if they aren't being used
    """
    for path in paths:
            if path not in sys.path:
                    sys.path.append( path )

# Moving to Utilities file
def importModule(name):
    print ("Importing : " + name )
    try:
        __import__(name)
    except ImportError:
        print ("Error importing :" + name)

def checkRigFolderExists( path ):
    """
        Checkes folder that will old data exists
    """
    if os.path.exists( path ):
        if os.path.exists( (path + "/rigFile") ):
            return True
        else:
            return False
    else:
        return False

def createRigFolders( path ):
    """
        Will create folders for rig
    """
    if os.path.exists( path ) == False:
        os.makedirs( path )
    if os.path.exists( (path + "/rigFile") ) == False:
        os.makedirs( (path + "/rigFile")  )

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
                
        return globals()[module_name]
    except ImportError:
        print ("Error loading :" + module_name)
        
def loadPackage(package_name):
    """
        Will see if package is loaded and import it or reload it 
        respectively
    """
    def loadPackageModules(package_name):
        modules = {}
        modulesNames = []
        modules[package_name] = globals()[package_name] 
        modulesNames =  globals()[package_name].__all__
        for moduleName in modulesNames:
            print ("Loading " + moduleName)
            modules[moduleName] = loadModule(moduleName)
        return modules
        
    modules = {}
    try:
        if globals().has_key(package_name):
                print ("Reloading : " + package_name )
                reload( globals()[package_name] )
                modules = loadPackageModules(package_name)
        else:
                print ("Importing : " + package_name )
                globals()[package_name] = __import__(package_name)    
                modules = loadPackageModules(package_name)
                
        return modules
    except ImportError:
        print ("Error loading :" + package_name)

def import_Libs(dir):
    """ Imports the Libs, returns a list of the Libraries. 
    Pass in dir to scan """
    
    Library_list = {} 
    
    for f in os.listdir(os.path.abspath(dir)):
        module_name, ext = os.path.splitext(f) # Handles no-extension files, etc.
        if ext == '.py': # Important, ignore .pyc/other files.
            print 'importing module: %s' % (module_name)
            loadModule(module_name)
            Library_list[module_name] = globals()[module_name]
 
    return Library_list

def import_packages(dir):
    """ Imports the packages, returns a list of the Libraries. 
    Pass in dir to scan """
    
    Library_list = {} 
    
    directories = os.listdir(os.path.abspath(dir))
    
    # Reorder list so utlities is sourced first
    count = 0
    for d in directories:
        if d == "UtilitiesPackage":
            tempVar = directories[0]
            directories[0] = directories[count]
            directories[count] = tempVar
        count += 1
    
    for d in directories:
        package_name, ext = os.path.splitext( d ) # Handles no-extension files, etc.
        if ext == '' and os.path.isdir( dir+ "/" + package_name): # Important, ignore .pyc/other files.
            if "__init__.py" in os.listdir( os.path.abspath(dir + "/" + package_name + "/") ):
                print 'loading package: %s' % (package_name)
                if (dir  + d + "/") not in sys.path:
                        sys.path.append( dir + d + "/" )
                Library_list = dict(Library_list.items() + (loadPackage(package_name)).items())
 
    return Library_list
    
def saveShapes( filePath, module, objects):
    """
        Will store shape data in file
    """
    #objects = self.getRegisteredObjects(module , regAttr)
    writeData = ""
    
    for object in objects:
        writeLine = (object + " ")
        # Get shape
        shape = Transform.getShape(object)
        # Get CV number
        cvNum = Curve.getCurveCVNumber( shape )
        for x in xrange(cvNum):
            pos = cmds.xform( (object + ".cv["+x+"]"), q= True, ws= True, t=True )
            writeLine += (pos[0] + " " + pos[1] + " " + pos[2] + " ")
        writeData += (writeLine + "\n")
    FILE = open(filePath,"wb")
    blueprintData = FILE.write(writeData)
    FILE.close()
    print ("Saved shape data to : " + filePath)
            
def loadShapes( filePath):
    """
        Loads shapes from file
    """
    if not os.path.isfile(filePath):
    	 print ("No data found from : " + filePath)
    	 return
    FILE = open(filePath,"rU")            
        
    for line in FILE:
        shapeDataLine = line.split()
        ShapeObject = shapeDataLines[0]
        shapeDataLines.remove(0)
        index = 0
        for x,y,z in shapeDataLines:
            cmds.xform( (ShapeObject + ".cv["+index+"]"), ws=True, t= ( x , y , z ) )
            index+=1
        
    FILE.close()
    print ("Loaded shape data from : " + filePath)
    
def loadTransforms( filePath):
    """
        Loads Transforms from file
    """
    if not os.path.isfile(filePath):
    	 print ("No data found from : " + filePath)
    	 return
    FILE = open(filePath,"rU")            
        
    for line in FILE:
        blueprintDataLine = line.split()
        blueprintObject = blueprintDataLine[0]
        translate = [ float( blueprintDataLine[1] ), float( blueprintDataLine[2] ), float( blueprintDataLine[3] ) ]
        rotate = [ float( blueprintDataLine[4] ), float( blueprintDataLine[5] ), float( blueprintDataLine[6] ) ]
        scale = [ float( blueprintDataLine[7] ), float( blueprintDataLine[8] ), float( blueprintDataLine[9] ) ]
        if cmds.objExists(blueprintObject):
            Attribute.checkSetCompoundAttr( (blueprintObject + ".t"), translate )
            Attribute.checkSetCompoundAttr( (blueprintObject + ".r"), rotate )
            Attribute.checkSetCompoundAttr( (blueprintObject + ".s"), scale )
    FILE.close()
    print ("Loaded transfrom data from : " + filePath)
    
def saveTransforms( filePath, module, objects):
    """
        Will Store transfrom data in file
    """
    #objects = self.getRegisteredObjects( module, regAttr)
    writeData = ""
    
    for object in objects:
        translate = Lib.getFirst(cmds.getAttr( (object + ".t") ) )
        rotate = Lib.getFirst( cmds.getAttr( (object + ".r") ) )
        scale = Lib.getFirst( cmds.getAttr( (object + ".s") ) )
        writeLine = (object + " " + str(translate[0]) + " " + str(translate[1]) + " " + str(translate[2]) + " " +
                                    str(rotate[0]) + " " + str(rotate[1]) + " " + str(rotate[2]) + " " +
                                    str(scale[0]) + " " + str(scale[1]) + " " + str(scale[2]) + "\n")
        writeData += writeLine
    FILE = open(filePath,"wb")
    blueprintData = FILE.write(writeData)
    FILE.close()
    print ("Saved Transform data to : " + filePath)
    
def saveBlueprintModuleData( bluePrintFilePath,  modules):
    """
        Saves blueprint module names type and parents
    """
    writeData = ""
    for module in modules:
        print module
        container = (module + "_CNT")
        writeData += ( module + " " + Attribute.getString(container, "type") + "\n" )
    
    FILE = open(bluePrintFilePath,"wb")
    blueprintData = FILE.write(writeData)
    FILE.close()

def readRigConnectionData(  startModuleIndice, endModuleIndice, lineArray ):
    """
        Will read array and retrieve connection data
    """
    returnConnectionData= []
    connectionIndiceStart = 0
    connectionIndiceEnd = 1
    for x in xrange( startModuleIndice, endModuleIndice ):
        # remove spaces
        line = lineArray[x].strip()
        if line.startswith("Connections:"):
            connectionIndiceStart = (x + 1)
        elif line.startswith("RegisteredAttr:"):
            connectionIndiceEnd = x
    for x in xrange(connectionIndiceStart, connectionIndiceEnd):
        returnConnectionData.append(lineArray[x].strip())
    return returnConnectionData
    
def readRigRegisteredAttr( startModuleIndice, endModuleIndice, lineArray):
    """
        Will read array and retrieve connection data
    """
    returnConnectionData= []
    connectionIndiceStart = 0
    connectionIndiceEnd = 1
    for x in xrange( startModuleIndice, endModuleIndice ):
        # remove spaces
        line = lineArray[x].strip()
        if line.startswith("RegisteredAttr:"):
            connectionIndiceStart = (x + 1)
        elif line.startswith("\t") == False:
            connectionIndiceEnd = x
    for x in xrange(connectionIndiceStart, connectionIndiceEnd):
        returnConnectionData.append(lineArray[x].strip())
    return returnConnectionData
    
def readRigNextModule( fileIndice, lineArray):
    """
        Will Find line indice of next module in file
    """
    fileIndice+= 1
    for x in xrange( fileIndice, len(lineArray) ):
        line = lineArray[x]
        if line.startswith("\t") == False:
            return x
    # return EOF
    return len(lineArray)

