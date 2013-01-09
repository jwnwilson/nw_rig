import os 
import sys
import maya.cmds as cmds
import imp

import Lib
import Attribute
import Transform
import Curve

MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

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
        
def package_contents(package_name):
    """
        Returns names of all modules in package
    """
    file, pathname, description = imp.find_module(package_name)
    if file:
        raise ImportError('Not a package: %r', package_name)
    # Use a set because some may be both source and compiled.
    return set([os.path.splitext(module)[0]
        for module in os.listdir(pathname)
        if module.endswith(MODULE_EXTENSIONS)])

    
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

