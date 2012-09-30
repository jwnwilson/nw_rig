import maya.cmds as cmds
import Attribute
import Constraint
import String
import Transform
import Control

# ------------------------
# Blueprint functions
# ------------------------
def duplicateBlueprint( moduleName, newName):
    """
        Will duplicate module and load all data from source module onto new module
    """
    groupRoot = moduleName + "Root_GRP"
    newGroupRoot = newName + "Root_GRP"
    moduleContainer = moduleName + "_CNT"
    dupContainer = newName + "_CNT"
    # Duplicate container
    duplicated = cmds.duplicate(moduleContainer, name = dupContainer, rc= True)
    duplicated.remove( dupContainer )
    for object in duplicated:
        StringReplace = object.replace(moduleName, newName)
        StringReplace = StringReplace[0:(len(StringReplace)-1)]
        cmds.rename(object, StringReplace)
    # parent module under new container
    parentContainer = cmds.container(moduleContainer, query= True, par= True)
    cmds.container(parentContainer, edit= True, an = dupContainer )    
    # rename Attributeibutes reconnect Attributeibutes
    
def mirrorBlueprint( moduleName, args):
    """
        Will mirror blueprint default is in -x axis
    """
    pass
def createBlueprinterChain( name, args ):
    'Creates a default blueprinters'
    rootGrp = cmds.group( n = (name + "Blueprinter_GRP"), em = True )
    ret = {}
    sctls = []
    joints = []
    functArgs = {"shape":"sphere", "size":0.5, "chainNo": 4}
    functArgs =  dict(functArgs.items() + args.items())
    
    #create Control
    for x in range(functArgs["chainNo"]):
        blueprinter = createBlueprinter( (name + str(x)), functArgs )
        sctls.append(blueprinter["sctl"])
        joints.append(blueprinter["jnt"])
        cmds.move(0,0,(x*1),blueprinter["sctl"][1])
            
    # manage joints
    cmds.parent(joints[0],rootGrp)
    cmds.parent(sctls[0][1],rootGrp)
    
    for x in range(1, functArgs["chainNo"]):
        cmds.parent(sctls[x][1],sctls[x-1][0])
        cmds.parent(joints[x],joints[x-1])
    
    ret["root"] = rootGrp
    ret["sctl"] = sctls
    ret["jnt"] = joints     
    return ret

def createBlueprinter( name, args ):
        'Creates a default blueprinters'
        ret = {}
        sctl = []
        jnt = ""
        functArgs = {"shape":"cube", "size":1, "t":0, "r":0, "s":0}
        functArgs =  dict(functArgs.items() + args.items())
        
        #create Control
        if(functArgs["shape"] == "cube"):
                sctl = Control.cubeCtl( name, functArgs )
        elif(functArgs["shape"] == "sphere"):
                sctl = Control.sphereCtl( name, functArgs )
        elif(functArgs["shape"] == "arrow"):
                sctl = Control.arrowCtl( name , functArgs )
        elif(functArgs["shape"] == "locator"):
                sctl = Control.locatorCtl( name , functArgs )
        else:
                print "Shape not supported...\n"
                return 0
                
        #lock hide unwanted Attribute
        if functArgs["t"] == 1:
            Attribute.lockHide(sctl[0], {"t":1, "h":1, "l":1})
        if functArgs["r"] == 1:
            Attribute.lockHide(sctl[0], {"r":1, "h":1, "l":1})
        if functArgs["s"] == 1:
            Attribute.lockHide(sctl[0], {"s":1, "h":1, "l":1})
            
        #add blueprinter joint
        jnt = cmds.joint( n = ( name + "_SJNT" ), p= (0, 0, 0 ) )
        Constraint.constrain(sctl[0], jnt, args={ "t":1, "mo":0, "name":(name)} )
        #matrixConstraint(sctl[0] , jnt, 0, {})
        #template(jnt)
        
        #parent to root
        cmds.parent(jnt,sctl[0])
        #cmds.parent(ret["sctl"][1],rootGrp)
        
        #rename suffix
        newName = sctl[0].replace("_CTL","_SCTL")
        cmds.rename(sctl[0],newName)
        sctl[0] = newName
        newName = sctl[1].replace("Ctl_GRP","Sctl_GRP")
        cmds.rename(sctl[1],newName)
        sctl[1] = newName
        
        #create blueprinter variable
        """for blueprinter in sctl:
            storeString(blueprinter, "blueprinter", "")
        storeString(jnt, "sjoint", "")"""
        
        ret["sctl"] = sctl
        ret["jnt"] = jnt
        
        return ret

#Control functions
def createAxisContols(name, args):
        """
            creates a Control with sub Controls limited to move only in one axis each
        """
        ret = {}
        X=[]
        Y=[]
        Z=[]
        functArgs = {"axis":"xyz", "size":1}
        functArgs =  dict(functArgs.items() + args.items())
        child=None
        
        xName = String.removeSuffix(name) + "X"
        yName = String.removeSuffix(name) + "Y"
        zName = String.removeSuffix(name) + "Z"
        
        topGrp = cmds.group(name=(name+"_GRP"),em=True)
        ctlGrp = cmds.group(name=(name+"Ctl_GRP"),em=True)
        
        if "x" in functArgs["axis"]:
            X = Control.arrowCtl( xName, functArgs )
            Attribute.lockHide(X[0], {"all":1, "h":1, "l":1})
            Attribute.setColour(X[0], "red")
            cmds.setAttr(( X[0] + ".tx"), lock=False, cb = True , k = True )
            child = Transform.getShape(X[0])
            cmds.rotate(0,-90,0, (child+".cv[0:7]"))
        if "y" in functArgs["axis"]:
            Y = Control.arrowCtl( yName, functArgs )
            Attribute.lockHide(Y[0], {"all":1, "h":1, "l":1})
            Attribute.setColour(Y[0], "green")
            cmds.setAttr(( Y[0] + ".ty"), lock=False, cb = True , k = True )
            child = Transform.getShape(Y[0])
            cmds.rotate(90,0,0, (child+".cv[0:7]"))
        if "z" in functArgs["axis"]:
            Z = Control.arrowCtl( zName, functArgs )
            Attribute.lockHide(Z[0], {"all":1, "h":1, "l":1})
            Attribute.setColour(Z[0], "blue")
            cmds.setAttr(( Z[0] + ".tz"), lock=False, cb = True , k = True )
            child = Transform.getShape(Z[0])
            cmds.rotate(180,0,0, (child+".cv[0:7]"))        
            
        #connect Control to group to negate movement
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
        
        #connect Control to ctls to top grp
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
            
        ret["xctl"] = X
        ret["yctl"] = Y
        ret["zctl"] = Z  
        ret["grp"] = [topGrp, ctlGrp]
        return ret
