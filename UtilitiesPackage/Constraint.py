from vector import *
import maya.cmds as cmds
import Attribute
import Constraint
import String
import Transform

# ------------------------
# Constraint functions
# ------------------------
def constrain(*args , **kwargs):
    """
        constrains target, aim Constraint requires more flags
    """
    influenceNo = (len(args) -1)
    sources = args[:-1]
    target = args[influenceNo]
    defaultName = String.removeSuffix(target)
    
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
    """
        Constraints object by a matrix Constraint
    """
    # Check plugin is loaded 
    if cmds.pluginInfo("decomposeMatrix",q= True,l=True) == 0:
        cmds.loadPlugin ("decomposeMatrix")
    functArgs = {"t":1, "r":1, "s":1, "all":0, "mo":0}
    functArgs =  dict(functArgs.items() + args.items())
    mainOff = functArgs["mo"]

    name = String.removeSuffix(child)
    
    matrixDecom = cmds.createNode( 'decomposeMatrix', n= (name + "decomMatrix") )
    offset  = None
    
    # contraint == parent world * inverse child parent
    matrixMulti1 = cmds.createNode( 'multMatrix', n=( name + "matrixMult1") )    
    
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
    # child rotation order -> orient Constraint rotation order
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
        
