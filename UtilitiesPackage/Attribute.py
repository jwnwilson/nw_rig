from functools import wraps
import maya.cmds as cmds

# ------------------------
# Attribute functions
# ------------------------
def addAttr(object, attrName, attrType, **kwargs):
    if cmds.objExists( (object + "." + attrName) ) == False:
        cmds.addAttr(object, ln= attrName, at= attrType, **kwargs)
    else:
        return False
def addStringAttribute(node,attr,data):
    if cmds.objExists( (node + "." + attr) ) == False:
        cmds.addAttr(node, longName= attr,shortName= (attr[0]+ attr[len(attr)-1]), dataType="string")
        cmds.setAttr((node+"." + attr), data, type="string")
    else:
        return False
def addStringArrayAttribute(node,attr,data):
    if cmds.objExists( (node + "." + attr) ) == False:
        cmds.addAttr( node, dt = "stringArray", ln = attr, sn = (attr[0]+ attr[len(attr)-1]))
        cmds.setAttr( (node+"." + attr), type = 'stringArray', *([len(data)] + data) )
    else:
        return False
def setStringArrayData(node,attr,data):
    if cmds.objExists( (node + "." + attr) ) == True:
        cmds.setAttr( (node+"." + attr), type = 'stringArray', *([len(data)] + data) )
    else:
        return False
def checkSetAttr( attr, value):
    """
        checks attribute is setable will set if so returns bool
    """
    if  cmds.getAttr( attr, se= True):
        cmds.setAttr( attr, value )
        return True
    return False
def checkSetCompoundAttr(attr, compoundValue):
    """
        checks attribute is setable will set if so
    """
    checkSetAttr( (attr + "x"), compoundValue[0])
    checkSetAttr( (attr + "y"), compoundValue[1])
    checkSetAttr( (attr + "z"), compoundValue[2])
    
def getConnectedObjects( attr ):
    """
        gets objects connected to attribute
    """
    if cmds.objExists( attr ):
        objects = cmds.listConnections( attr )
        """for x in range( len(objects) ):
            print objects[x]
            objects[x] = cmds.plugNode(objects[x])"""
        return objects
    else:
        return False

def template(obj):
    cmds.setAttr((obj + ".template"), 1)

def setColour(obj, colour):
    result = None
    try:
        result = {
          'red': 12,
          'blue': 6,
          'yellow': 17,
          'green': 14,
          'orange': 24,
        }[colour]
    except KeyError:
        print ("warning colour not found, default set for " + obj + ".")
        result = 0
        
    if cmds.objExists(obj):
        objShape = cmds.listRelatives(obj, c= True, s= True)
        objAttr = (objShape[0] + ".overrideEnabled")
        if cmds.objExists(objAttr):
            cmds.setAttr( objAttr, 1)
            cmds.setAttr( (objShape[0] +".overrideColor"), result)

def lockHide(obj, args):
    functArgs = {"t":0, "r":0, "s":0, "v":0, "all":0, "l":0, "h":0}
    functArgs =  dict(functArgs.items() + args.items())

    if functArgs["t"] == 1 or functArgs["all"] == 1:
        if functArgs["l"] == 1:
            cmds.setAttr( (obj + ".tx"), l = True )
            cmds.setAttr( (obj + ".ty"), l = True )
            cmds.setAttr( (obj + ".tz"), l = True )
        if functArgs["h"] == 1:
            cmds.setAttr( (obj + ".tx"), cb = False , k = False )
            cmds.setAttr( (obj + ".ty"), cb = False , k = False )
            cmds.setAttr( (obj + ".tz"), cb = False , k = False )
    if functArgs["r"] == 1 or functArgs["all"] == 1:
        if functArgs["l"] == 1:
            cmds.setAttr( (obj + ".rx"), l = True )
            cmds.setAttr( (obj + ".ry"), l = True )
            cmds.setAttr( (obj + ".rz"), l = True )
        if functArgs["h"] == 1:
            cmds.setAttr( (obj + ".rx"), cb = False , k = False )
            cmds.setAttr( (obj + ".ry"), cb = False , k = False )
            cmds.setAttr( (obj + ".rz"), cb = False , k = False )
    if functArgs["s"] == 1 or functArgs["all"] == 1:
        if functArgs["l"] == 1:
            cmds.setAttr( (obj + ".sx"), l = True )
            cmds.setAttr( (obj + ".sy"), l = True )
            cmds.setAttr( (obj + ".sz"), l = True )
        if functArgs["h"] == 1:
            cmds.setAttr( (obj + ".sx"), cb = False , k = False )
            cmds.setAttr( (obj + ".sy"), cb = False , k = False )
            cmds.setAttr( (obj + ".sz"), cb = False , k = False )
    if functArgs["v"] == 1 or functArgs["all"] == 1:
        if functArgs["l"] == 1:
            cmds.setAttr( (obj + ".v"), l = True )
        if functArgs["h"] == 1:
            cmds.setAttr( (obj + ".v"), cb = False , k = False )
# ------------------------
# storage functions
# ------------------------
def dataExistsWrapper(funct):
    """
        simple wrapper to check data exists before accessing it
    """
    @wraps(funct)
    def wrapper(*args, **kwds):
        if dataExists(args[0],args[1]):
            ret = funct(*args, **kwds)
            return ret
        else:
            cmds.error(("Data not found for: " + args[0] + "." + args[1]))
    return wrapper

def dataExists(node, attr):
    """
        Checks if attribute exists
    """
    if cmds.attributeQuery( attr, node= node,exists =True ):
        return True;
    else:
        return False;

def storeString(node, attr, data):
    """
        Store string on node
    """
    if dataExists(node, attr):
        cmds.setAttr((node+"." + attr), data, type="string")
    else:
        addStringAttribute(node,attr,data)
    
def storeStringArray(node, attr, data):
    """
        Store string on node
    """
    if dataExists(node, attr):
            cmds.setAttr( (node+"." + attr), type = 'stringArray', *([len(data)] + data) )
    else:
       addStringArrayAttribute(node,attr,data)

def storeArgs(node, attr, *args):
    pass
    
def storeKwargs(node, attr, **kwargs):
    pass
    
@dataExistsWrapper
def getString(node, attr):
    return cmds.getAttr((node+ "." + attr))
    
@dataExistsWrapper
def getStringArray(node, attr):
    return cmds.getAttr((node+"." + attr))
    
@dataExistsWrapper
def getArgs(node, attr):
    pass
    
@dataExistsWrapper
def getKwargs(node, attr):
    pass
