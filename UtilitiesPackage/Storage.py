from functools import wraps
import maya.cmds as cmds
import Attribute

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
        Attribute.addStringAttribute(node,attr,data)
    
def storeStringArray(node, attr, data):
    """
        Store string on node
    """
    if dataExists(node, attr):
            cmds.setAttr( (node+"." + attr), type = 'stringArray', *([len(data)] + data) )
    else:
       Attribute.addStringArrayAttribute(node,attr,data)

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
