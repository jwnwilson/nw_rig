import maya.cmds as cmds

# ------------------------
# lib functions
# ------------------------
def deleteDictKey(dic, key):
    if dic.has_key(key):
        del dic[key]
    return dic

def getFirst(array):
    try:
        return array[0]
    except:
        cmds.error("Error getting first element of object :" + str(array) )
        
def defaultArgs(defaultArgs, argsDictionary):
    return dict(defaultArgs.items() + argsDictionary.items())

def checkForKwarg(key, kwargs):
    if key in kwargs:
        return kwargs[key]
    
def checkForExistingObject(objectName, objectType):
    """
        Checks for existing object
    """
    if cmds.objExists( objectName ):
        if cmds.objectType( objectName ) == objectType:
            return True
    return False
def createSingleArray( arrayOfArrays ):
    """
    	Condenses array of arrays in array
    """
    ret = []
    
    for array in arrayOfArrays:
    	    if type(array) == type([]):
    	    	    for element in array:
    	    	    	    ret.append( element )
	    else:
	    	    ret.append(array)
    return ret

# ------------------------
# arg functions
# ------------------------
def checkArgs(argNames, args):
    if len(argNames) != len(args):
        cmds.error("Number of args and arg names do not match.")
    for x in range(argNames):
        if checkArg(argName[x], args[argName[x]]) == 0:
            return 0

    return 1

def checkArg(argName, arg):
    if argName in arg:
        return 1
    else:
        return 0 

def getArg(argName, arg):
    if argName in arg:
        return arg[argName]
    else:
        return 0
