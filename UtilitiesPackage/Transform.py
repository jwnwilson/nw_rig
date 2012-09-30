import maya.cmds as cmds

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
# heirarchy functions
# ------------------------
def getShape(obj):
    relatives = cmds.listRelatives(obj,s=True,c=True)
    return relatives[0]
