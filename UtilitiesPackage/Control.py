from vector import *
import maya.cmds as cmds
import Lib
import Attribute
import Constraint
import String
import Transform

# ------------------------
# Control functions
# ------------------------
def createCluster( clusterName, objs, **kwargs):
	"""
		Creates cluster on object / objects
	"""
	cluster = (cmds.cluster(objs, name = (clusterName + "_CLS"), **kwargs))[1]
	clusterGrp = cmds.group(cluster, name = (clusterName + "_GRP") )
	
	return [cluster,clusterGrp]

def createControl( name, args ):
        """
            Creates a default control
        """
        functArgs = {"shape":"circle", "size":1, "match":""}
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
        if cmds.objExists(functArgs["match"]):
            Transform.match(ctl[1],functArgs["match"],{"all":1})
        #create control variable
        """for c in ctl:
            storeString(c, "control", "")"""
        return ctl

def shapeCtl( name, shape ):
        """
            Creates ctl with shape given
        """
        J=[]
        ctl =(cmds.curve( n =(name + "_CTL"), d= 1, p= shape ) )
        grp = cmds.group( ctl, n = (name + "Ctl_GRP"))
        cmds.xform(grp, piv= [0,0,0] )
        J.append(ctl)
        J.append(grp)
        return J

def locatorCtl( name, args ):
        'Creates locator ctl'
        J=[]
        ctl = Lib.getFirst(cmds.spaceLocator( n =(name + "_CTL") ) )
        grp = cmds.group( ctl, n = (name + "Ctl_GRP"))
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
        curve= Lib.getFirst(cmds.circle( n = (name+ "_CTL"), c= [0, 0, 0], nr= [0, 1, 0], sw= 360, r= radius, d= 3, ut= 0, tol= 0.01 ,s= 8, ch=1))
        grp = cmds.group( curve, n = (name + "Ctl_GRP"))
        J.append(curve)
        J.append(grp)
        return J
        
def sphereCtl( name, functArgs ):
        J=[]
        ctl = Lib.getFirst(cmds.polySphere( n = (name + "_CTL"), r= functArgs["size"], sx= 1, sy= 1, ax= [0, 1, 0], ch= 1))
        grp = cmds.group( ctl, n = (name + "Ctl_GRP"))
        J.append(ctl)
        J.append(grp)
        return J

def cubeCtl( name, functArgs ):
        J=[]
        ctl = Lib.getFirst(cmds.polyCube( n = (name + "_CTL"), w= functArgs["size"], h= functArgs["size"], d= 1, sx= 1, sy= 1, sz= 1, ax= [0, 1, 0], cuv= 4, ch= 1))
        grp = cmds.group( ctl, n = (name + "Ctl_GRP"))
        J.append(ctl)
        J.append(grp)
        return J
        
# ------------------------
# Ik functions
# ------------------------
def createIkHandle(name, joints, **kwargs):
    """
        Creates Ik handle for three joints
        return values: 
        IK
        EFF
    """
    # Default args
    args = {"sol":"ikRPsolver"}
    functArgs =  Lib.defaultArgs(args, kwargs)
    kwargs = Lib.deleteDictKey(kwargs, "sol")
    ret = {}
    
    if len(joints) != 3:
        cmds.error("Incorrect number of joints supplied to IkHandle.")
    
    handleData = cmds.ikHandle( n= (name + "_IKH"), sol= functArgs["sol"], sj= joints[0], ee= joints[2],**kwargs)
    cmds.setAttr((handleData[0] + ".v"), 0)
    
    ret["IK"] = handleData[0]
    ret["EFF"] = handleData[1]
    return ret
    
def createSplineIk(name, joints, **kwargs):
    """
        Creates spline Ik
        return values: 
        IK
        EFF
        CRV
    """
    # Default args
    args = {"sol":"ikRPsolver"}
    functArgs =  Lib.defaultArgs(args, kwargs)
    kwargs = Lib.deleteDictKey(kwargs, "sol")
    ret = {}
    
    handleData = cmds.ikHandle( n= (name + "_IKH"), sol= functArgs["sol"], sj= joints[0], ee= joints[len(joints)-1],**kwargs)
    cmds.setAttr((handleData[0] + ".v"), 0)
    handleData[2] = cmds.rename(handleData[2],(name+ "IK_CRV") )
    
    ret["IK"] = handleData[0]
    ret["EFF"] = handleData[1]
    ret["CRV"] = handleData[2]
    return ret

def createPoleVec(joints, ikHandle, position):
    """
        Creates pole vector for handle for three joints
    """
    if len(joints) != 3:
        cmds.error("Incorrect number of joints supplied to IkHandle.")
    
    # Create locator to act as pole vector
    locName = (String.removeSuffix(ikHandle) + "Pole_LOC")
    poleGrpName = (String.removeSuffix(ikHandle) + "Pole_GRP")
    poleVecName = (String.removeSuffix(ikHandle) + "Pole_PVC")
    
    loc = Lib.getFirst(cmds.spaceLocator(n = locName, p= (0,0,0) ))
    cmds.xform(loc, ws= True, t= (position[0], position[1], position[2]) )
    locGrp = cmds.group(loc, n= poleGrpName)
    cmds.poleVectorConstraint( loc , ikHandle, n= poleVecName, w=.1 )
    cmds.setAttr((loc + ".v"), 0)
    
    return locGrp
    
def getPolePosition(joints, distance):
    """
        Returns best pole vector position
    """
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
