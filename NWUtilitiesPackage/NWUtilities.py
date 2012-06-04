"""
This needs to be turned into a meta file that will manage the other utility files

To do:
    -add colours to axis controls
    -axis control:
        -overal group which moved control
        -each subcontrol will be connected to top group in x/y/z
        -each subcontrol has group to counteract it's movement
"""

import maya.cmds as cmds
from vector import *
from functools import wraps

# ------------------------
# lib functions
# ------------------------
def getFirst(array):
    try:
        return array[0]
    except:
        error("Error getting first element of object :" + array )
# ------------------------
# string functions 
# ------------------------
def getPrefixByChar(name, char):
    split = name.split(char)
    return split[0]

def getPrefix(name):
    return getPrefixByChar(name, "_")

def getSuffixByChar(name, char):
    split = name.split(char)
    return split[len(split)-1]

def getSuffix(name):
    return getSuffixByChar(name, "_")   

def removeSuffixByChar(name, char):
    split = name.split(char)
    ret= ""
    if len(split) == 1:
        return split[0]
    for x in range(len(split)-1):
        if x != (len(split)-2):
            ret += (split[x] + "_")
        else:
            ret += (split[x])
    return ret

def removeSuffix(name):
    return removeSuffixByChar(name, "_")

def removePrefixByChar(name,char):
    split = name.split(char)
    ret= ""
    if len(split) == 1:
        return split[0]
    for x in range(1,len(split)):
        if x != (len(split)-1):
            ret += (split[x] + "_")
        else:
            ret += (split[x])
    return ret
    
def removePrefix(name):
    return removePrefixByChar(name,"_")
# ------------------------
# Transform functions
# ------------------------
def match(source, target , args):
    functArgs = {"t":0, "r":0, "s":0, "all":0, "mo":0}
    functArgs =  dict(functArgs.items() + args.items())
    mainOff = functArgs["mo"]
    
    if functArgs["t"] == 1:
        pntConst = cmds.pointConstraint( target, source,  mo = mainOff )
        cmds.delete( pntConst )
    if functArgs["r"] == 1:
        oriConst = cmds.orientConstraint( target, source,  mo = mainOff )
        cmds.delete( oriConst )
    if functArgs["s"] == 1:
        scaConst = cmds.scaleConstraint(  target, source, mo = mainOff )
        cmds.delete( scaConst )
    if functArgs["all"] == 1:
        parConst = cmds.parentConstraint( target, source,  mo = mainOff )
        cmds.delete( parConst )
    
# ------------------------
#attribute functions
# ------------------------
def addStringAttribute(node,attr,data):
    cmds.addAttr(node, longName= attr,shortName= (attr[0]+ attr[len(attr)-1]), dataType="string")
    cmds.setAttr((node+"." + attr), data, type="string")

def addStringArrayAttribute(node,attr,data):
    cmds.addAttr( node, dt = "stringArray", ln = attr, sn = (attr[0]+ attr[len(attr)-1]))
    cmds.setAttr( (node+"." + attr), type = 'stringArray', *([len(data)] + data) )

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
# ------------------------
#starter functions
# ------------------------
def createStarterChain( name, args ):
        'Creates a default starters'
        rootGrp = cmds.group( n = (name + "Starter_GRP"), em = True )
        J = []
        SCtls =[]
        functArgs = {"shape":"sphere", "size":0.5, "chainNo": 4}
        functArgs =  dict(functArgs.items() + args.items())
        
        #create control
        for x in range(functArgs["chainNo"]):
                starter = createStarter( (name + str(x)), functArgs )
                cmds.move(0,0,(x*1),starter[1])
                SCtls.append(starter)
                
        # manage joints
        cmds.parent(SCtls[0][2],rootGrp)
        cmds.parent(SCtls[0][1],rootGrp)
        
        for x in range(1, functArgs["chainNo"]):
                cmds.parent(SCtls[x][2],SCtls[x-1][2])
                cmds.parent(SCtls[x][1],SCtls[x-1][0])
                
        for x in range(len(SCtls)):
            for y in range(len(SCtls[x])):
                J.append(SCtls[x][y])
                
        return J

def createStarter( name, args ):
        'Creates a default starters'
        J = []
        functArgs = {"shape":"cube", "size":1, "t":0, "r":0, "s":0}
        functArgs =  dict(functArgs.items() + args.items())
        
        #create control
        if(functArgs["shape"] == "cube"):
                J = cubeCtl( name, functArgs )
        elif(functArgs["shape"] == "sphere"):
                J = sphereCtl( name, functArgs )
        elif(functArgs["shape"] == "arrow"):
                J = arrowCtl( name , functArgs )
        elif(functArgs["shape"] == "locator"):
                J = locatorCtl( name , functArgs )
        else:
                print "Shape not supported...\n"
                return 0
                
        #lock hide unwanted attr
        if functArgs["t"] == 1:
            lockHide(J[0], {"t":1, "h":1, "l":1})
        if functArgs["r"] == 1:
            lockHide(J[0], {"r":1, "h":1, "l":1})
        if functArgs["s"] == 1:
            lockHide(J[0], {"s":1, "h":1, "l":1})
            
        #add starter joint
        jnt = cmds.joint( n = ( name + "_SJNT" ), p= (0, 0, 0 ) )
        matrixConstraint(J[0] , jnt, 0, {})
        J.append(jnt)
        
        #parent to root
        cmds.parent(jnt,J[0])
        #cmds.parent(J[1],rootGrp)
        
        #rename suffix
        newName = J[0].replace("_CTL","_SCTL")
        cmds.rename(J[0],newName)
        J[0] = newName
        
        #create starter variable
        for starter in J:
            storeString(starter, "starter", "")
        return J

#control functions
def createAxisContols(name, args):
        """
            creates a control with sub controls limited to move only in one axis each
        """
        J=[]
        X=[]
        Y=[]
        Z=[]
        functArgs = {"axis":"xyz", "size":1}
        functArgs =  dict(functArgs.items() + args.items())
        child=None
        
        xName = removeSuffix(name) + "X"
        yName = removeSuffix(name) + "Y"
        zName = removeSuffix(name) + "Z"
        
        topGrp = cmds.group(name=(name+"_GRP"),em=True)
        ctlGrp = cmds.group(name=(name+"Ctl_GRP"),em=True)
        
        if "x" in functArgs["axis"]:
            X = arrowCtl( xName, functArgs )
            lockHide(X[0], {"all":1, "h":1, "l":1})
            setColour(X[0], "red")
            cmds.setAttr(( X[0] + ".tx"), lock=False, cb = True , k = True )
            child = getShape(X[0])
            cmds.rotate(0,-90,0, (child+".cv[0:7]"))
        if "y" in functArgs["axis"]:
            Y = arrowCtl( yName, functArgs )
            lockHide(Y[0], {"all":1, "h":1, "l":1})
            setColour(Y[0], "green")
            cmds.setAttr(( Y[0] + ".ty"), lock=False, cb = True , k = True )
            child = getShape(Y[0])
            cmds.rotate(90,0,0, (child+".cv[0:7]"))
        if "z" in functArgs["axis"]:
            Z = arrowCtl( zName, functArgs )
            lockHide(Z[0], {"all":1, "h":1, "l":1})
            setColour(Z[0], "blue")
            cmds.setAttr(( Z[0] + ".tz"), lock=False, cb = True , k = True )
            child = getShape(Z[0])
            cmds.rotate(180,0,0, (child+".cv[0:7]"))
            
        #connect control to group to negate movement
        XNeg = cmds.createNode("multDoubleLinear", n=(name+"X_PMA"))
        cmds.setAttr((XNeg + ".input2"), -1)
        YNeg = cmds.createNode("multDoubleLinear", n=(name+"Y_PMA"))
        cmds.setAttr((YNeg + ".input2"), -1)
        ZNeg = cmds.createNode("multDoubleLinear", n=(name+"Z_PMA"))
        cmds.setAttr((ZNeg + ".input2"), -1)
        
        cmds.connectAttr((X[0]+".tx"),(XNeg+".input1"), f=True)
        cmds.connectAttr((Y[0]+".ty"),(YNeg+".input1"), f=True)
        cmds.connectAttr((Z[0]+".tz"),(ZNeg+".input1"), f=True)
        
        cmds.connectAttr((XNeg+".output"),(X[1]+".tx"), f=True)
        cmds.connectAttr((YNeg+".output"),(Y[1]+".ty"), f=True)
        cmds.connectAttr((ZNeg+".output"),(Z[1]+".tz"), f=True)
        
        #connect control to ctls to top grp
        cmds.connectAttr((X[0]+".tx"),(ctlGrp+".tx"), f=True)
        cmds.connectAttr((Y[0]+".ty"),(ctlGrp+".ty"), f=True)
        cmds.connectAttr((Z[0]+".tz"),(ctlGrp+".tz"), f=True)
        
        cmds.parent(ctlGrp, topGrp)
        
        if "x" in functArgs["axis"]:
            cmds.parent(X[1], ctlGrp)
        if "y" in functArgs["axis"]:
            cmds.parent(Y[1], ctlGrp)
        if "z" in functArgs["axis"]:
            cmds.parent(Z[1], ctlGrp)
            
        J.append(topGrp) 
        J.append(ctlGrp) 
        J = J + X + Y + Z
        return J
# ------------------------
# Control functions
# ------------------------
def createControl( name, args ):
        'Creates a default control'
        J =[]
        functArgs = {"shape":"circle", "size":1}
        functArgs =  dict(functArgs.items() + args.items())
        
        #create control
        if(functArgs["shape"] == "circle"):
                ctl = circleCtl( name, functArgs["size"] )
        elif(functArgs["shape"] == "arrow"):
                ctl = arrowCtl( name, functArgs )
        elif(functArgs["shape"] == "locator"):
                ctl = locatorCtl( name, functArgs )
        else:
                print "Shape not supported...\n"
                return 0
        
        #create control variable
        for c in ctl:
            storeString(c, "control", "")
        return ctl

def shapeCtl( name, shape ):
        'Creates ctl with shape given'
        J=[]
        ctl =(cmds.curve( n =(name + "_CTL"), d= 1, p= shape ) )
        grp = cmds.group( ctl, n = (name + "_GRP"))
        cmds.xform(grp, piv= [0,0,0] )
        J.append(ctl)
        J.append(grp)
        return J

def locatorCtl( name, args ):
        'Creates locator ctl'
        J=[]
        ctl = getFirst(cmds.spaceLocator( n =(name + "_CTL") ) )
        grp = cmds.group( ctl, n = (name + "_GRP"))
        cmds.xform(grp, piv= [0,0,0] )
        J.append(ctl)
        J.append(grp)
        return J
        
def arrowCtl( name, args ):
        'Creates arrow control'
        functArgs = {"size":1}
        functArgs =  dict(functArgs.items() + args.items())
        
        shape= [(0, 1, 0), (0, 1, -2), (0, 2, -2), (0, 0,-4) , (0, -2, -2), (0, -1, -2), (0, -1, 0), (0, 1, 0)]
        cvNo = len(shape)
        ctl= shapeCtl( name, shape )
        crvShape = cmds.listRelatives(ctl[0], c=True, s=True)
        crvShapeCVs = (crvShape[0]+".cv[0:"+ str(cvNo) +"]")
        cmds.scale( functArgs["size"],functArgs["size"],functArgs["size"],crvShapeCVs )
        return ctl
        
def circleCtl( name, radius ):
        'Creates arrow control'
        J=[]
        curve= getFirst(cmds.circle( n = (name+ "_CTL"), c= [0, 0, 0], nr= [0, 1, 0], sw= 360, r= radius, d= 3, ut= 0, tol= 0.01 ,s= 8, ch=1))
        grp = cmds.group( curve, n = (name + "_GRP"))
        J.append(curve)
        J.append(grp)
        return J
        
def sphereCtl( name, functArgs ):
        J=[]
        ctl = getFirst(cmds.polySphere( n = (name + "_CTL"), r= functArgs["size"], sx= 1, sy= 1, ax= [0, 1, 0], ch= 1))
        grp = cmds.group( ctl, n = (name + "_GRP"))
        J.append(ctl)
        J.append(grp)
        return J

def cubeCtl( name, functArgs ):
        J=[]
        ctl = getFirst(cmds.polyCube( n = (name + "_CTL"), w= functArgs["size"], h= functArgs["size"], d= 1, sx= 1, sy= 1, sz= 1, ax= [0, 1, 0], cuv= 4, ch= 1))
        grp = cmds.group( ctl, n = (name + "_GRP"))
        J.append(ctl)
        J.append(grp)
        return J
# ------------------------
# Ik functions
# ------------------------
def createIkHandle(name, joints, functArgs):
    'Creates Ik handle for three joints'
    args = {"solver":"ikRPsolver"}
    functArgs =  dict(functArgs.items() + args.items())
    
    if len(joints) != 3:
        cmds.error("Incorrect number of joints supplied to IkHandle.")
    
    handleData = cmds.ikHandle( n= (name + "_IKH"), sol= functArgs["solver"], sj= joints[0], ee= joints[2], p= 2, w= 1)
    
    return handleData

def createPoleVec(joints, ikHandle, distance):
    'Creates pole vector for handle for three joints'
    if len(joints) != 3:
        cmds.error("Incorrect number of joints supplied to IkHandle.")
        
    poisiton = getPolePosition(joints, distance)
    
    # Create locator to act as pole vector
    locName = (removeSuffix(ikHandle) + "Pole_LOC")
    poleGrpName = (removeSuffix(ikHandle) + "Pole_GRP")
    poleVecName = (removeSuffix(ikHandle) + "Pole_PVC")
    
    loc = cmds.spaceLocator(n = locName, p= (0,0,0) )
    cmds.xform(loc, ws= True, t= (poisiton[0], poisiton[1], poisiton[2]) )
    locGrp = cmds.group(loc, n= poleGrpName)
    
    cmds.poleVectorConstraint( loc , ikHandle, n= poleVecName, w=.1 )
    
    return locGrp
    
def getPolePosition(joints, distance):
    'Returns best pole vector position'
    if len(joints) != 3:
        cmds.error("Incorrect number of joints supplied to getPolePosition.")
    # get position between joint 1 and 3
    joint1Pos = Vector.initList(cmds.xform(joints[0], q= True,t= True,ws= True))
    joint2Pos = Vector.initList(cmds.xform(joints[1], q= True,t= True,ws= True))
    joint3Pos = Vector.initList(cmds.xform(joints[2], q= True,t= True,ws= True))
    
    joint1to3Pos = (joint3Pos - joint1Pos)
    betweenJoint1and3 = joint1Pos + (joint1to3Pos * 0.5)
    # get vector toward joint 2
    resultVec  = Normalize((joint2Pos - betweenJoint1and3))
    # multiply vector by distance
    resultVec = resultVec * distance
    # return joint 2 position + result
    return (joint2Pos + resultVec)
# ------------------------
# heirarchy functions
# ------------------------
def getShape(obj):
    relatives = cmds.listRelatives(obj,s=True,c=True)
    return relatives[0]
# ------------------------
# curve functions
# ------------------------
def getCvNo(curve):
    degree = cmds.getAttr("curve1.degree")
    spans = cmds.getAttr("curve1.spans")
    return (degree + spans)
# ------------------------
# joint functions
# ------------------------
def createChain(chainNo, ChainName):
        'Creates a chain of joints'
        joints = []     
        for i in range(chainNo):
                joints.append(cmds.joint( n = ( ChainName + str(i) + "_JNT" ), p= (0, 0, (1 * i) ) ))
        return joints
    
def duplicateChain(name , chainJoints):
        'Duplicates a chain of joints'
        i = 1
        joints = []
        jointNo = len(chainJoints)
        
        for x in range( jointNo ):
            joints.append( getFirst(cmds.duplicate(chainJoints[x], po = True, n = (name + str(x + 1) + "_JNT"))) ) 
        
        for x in range( 1, jointNo ):
            cmds.parent(joints[jointNo - x], joints[jointNo - (x + 1)])
        
        return joints
# ------------------------
# attribute functions
# ------------------------
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
# ------------------------
# constraint functions
# ------------------------
def constrain(*args , **kwargs):
    """
        constrains target, aim constraint requires more flags
    """
    influenceNo = (len(args) -1)
    sources = args[:-1]
    target = args[influenceNo]
    defaultName = removeSuffix(target)
    
    functArgs = {"t":0, "r":0, "s":0, "all":0, "aim":0, "mo":0, "name": defaultName}
    functArgs =  dict(functArgs.items() + kwargs["args"].items())
    mainOff = functArgs["mo"]
    
    if functArgs["t"] == 1:
        constrain = cmds.pointConstraint( args, n = (functArgs["name"] + "_PNT"),  mo = mainOff )
    if functArgs["r"] == 1:
        constrain = cmds.orientConstraint( args, n = (functArgs["name"]+ "_ORC"),  mo = mainOff )
    if functArgs["s"] == 1:
        constrain = cmds.scaleConstraint(  args, n = (functArgs["name"]+ "_SCT"), mo = mainOff )
    if functArgs["all"] == 1:
        constrain = cmds.parentConstraint( args, n = (functArgs["name"]+ "_PCT"),  mo = mainOff )
    if functArgs["aim"] == 1:
        constrain = cmds.aimConstraint( args, n = (functArgs["name"]+ "_AIM"),  mo = mainOff )
    return constrain

def matrixConstraint(parent , child, mainOff, args):
    # Check plugin is loaded 
    if cmds.pluginInfo("decomposeMatrix",q= True,l=True) == 0:
        cmds.loadPlugin ("decomposeMatrix")
    functArgs = {"t":1, "r":1, "s":1, "all":0, "mo":0}
    functArgs =  dict(functArgs.items() + args.items())
    mainOff = functArgs["mo"]

    name = removeSuffix(child)
    
    matrixDecom = cmds.createNode( 'decomposeMatrix', n= (name + "decomMatrix") )
    offset  = None
    
    # contraint == parent world * inverse child parent
    matrixMulti1 = cmds.createNode( 'multMatrix', n=( name + "matrixMult1") )    
    
    # offset!!! == original child world position
    
    # don't forget to freeze pivots if they are offset shit gets real
    cmds.xform( child, cp = True )
    
    offsetMat = cmds.createNode( "fourByFourMatrix", n= (name + "offsetMat" ) ) 
    matrixMulti2 = cmds.createNode( 'multMatrix', n= (name +  "matrixMult2") )

    if mainOff == 1:
        #parentCon = cmds.parentConstraint(child ,offset )
        #cmds.delete(parentCon)
        m = cmds.xform( child, q=True, ws=True, m=True  )
        cmds.setAttr( (offsetMat +".i00"), m[0])
        cmds.setAttr( (offsetMat +".i01"), m[1])
        cmds.setAttr( (offsetMat +".i02"), m[2])
        cmds.setAttr( (offsetMat +".i03"), m[3])
        cmds.setAttr( (offsetMat +".i10"), m[4])
        cmds.setAttr( (offsetMat +".i11"), m[5])
        cmds.setAttr( (offsetMat +".i12"), m[6])
        cmds.setAttr( (offsetMat +".i13"), m[7])
        cmds.setAttr( (offsetMat +".i20"), m[8])
        cmds.setAttr( (offsetMat +".i21"), m[9])
        cmds.setAttr( (offsetMat +".i22"), m[10])
        cmds.setAttr( (offsetMat +".i23"), m[11])
        cmds.setAttr( (offsetMat +".i30"), m[12])
        cmds.setAttr( (offsetMat +".i31"), m[13])
        cmds.setAttr( (offsetMat +".i32"), m[14])
        cmds.setAttr( (offsetMat +".i33"), m[15])
    
    # offset == child original world matrix * inverse parent matrix
    cmds.connectAttr( (offsetMat +  ".output"), (matrixMulti2 + ".matrixIn[0]"), f= True ) 
    cmds.connectAttr( (parent + ".worldInverseMatrix"), (matrixMulti2 + ".matrixIn[1]"), f= True )
        
    m = cmds.getAttr( (matrixMulti2 + ".matrixSum") )
        
    cmds.setAttr( (offsetMat +".i00"), m[0])
    cmds.setAttr( (offsetMat +".i01"), m[1])
    cmds.setAttr( (offsetMat +".i02"), m[2])
    cmds.setAttr( (offsetMat +".i03"), m[3])
    cmds.setAttr( (offsetMat +".i10"), m[4])
    cmds.setAttr( (offsetMat +".i11"), m[5])
    cmds.setAttr( (offsetMat +".i12"), m[6])
    cmds.setAttr( (offsetMat +".i13"), m[7])
    cmds.setAttr( (offsetMat +".i20"), m[8])
    cmds.setAttr( (offsetMat +".i21"), m[9])
    cmds.setAttr( (offsetMat +".i22"), m[10])
    cmds.setAttr( (offsetMat +".i23"), m[11])
    cmds.setAttr( (offsetMat +".i30"), m[12])
    cmds.setAttr( (offsetMat +".i31"), m[13])
    cmds.setAttr( (offsetMat +".i32"), m[14])
    cmds.setAttr( (offsetMat +".i33"), m[15])
    
    # Order of matrixs is VERY important if offset is applied last the child will not rotate around
    # the parent's origin as it's the parent pivot will not be multiplied properly
    cmds.connectAttr( (offsetMat + ".output"), (matrixMulti1 + ".matrixIn[0]"), f= True )
    cmds.connectAttr( (parent + ".worldMatrix"), (matrixMulti1 + ".matrixIn[1]"), f= True )
    cmds.connectAttr( (child + ".parentInverseMatrix"), (matrixMulti1 + ".matrixIn[2]"), f= True )
    
    # make child rotate around parent instead of copy it's rotation
    orc = cmds.createNode( "orientConstraint", n= (removeSuffix(child) + "Const_ORC"), p= child  )
    
    #final connect
    cmds.connectAttr( (matrixMulti1 + ".matrixSum") , (matrixDecom + ".inputMatrix") , f= True )
    
    # output rotation -> orient target[0] target rotation
    cmds.connectAttr( ( matrixDecom +".or") , ( orc + ".tg[0].tr") , f= True )
    # child rotation order -> orient constraint rotation order
    cmds.connectAttr( ( child +".ro") , ( orc + ".cro") , f= True )
    
    # orient target[0] target rptation order == 0
    cmds.setAttr( ( orc +".tg[0].tro"), 0 )   
    
    # A orient const can be used to preserve clean join rotations if desired
    #cmds.connectAttr( ( orc + ".cr" ) , ( child + ".r" ) , f= True )
    if functArgs["r"] == 1 or functArgs["all"]:
        cmds.connectAttr( ( matrixDecom + ".outputRotate") , (child  + ".rotate"), f= True )
    if functArgs["t"] == 1 or functArgs["all"]:
        cmds.connectAttr( (matrixDecom + ".outputTranslate") , (child  + ".translate"), f= True)
    if functArgs["s"] == 1 or functArgs["all"]:
        cmds.connectAttr( ( matrixDecom + ".outputScale") , (child  + ".scale"), f= True )
    if functArgs["r"] == 1 or functArgs["all"]:
        cmds.connectAttr( ( matrixDecom + ".outputShear") , (child  + ".shear"), f= True )
        
