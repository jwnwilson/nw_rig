import maya.cmds as cmds
import Lib
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
            joints.append( Lib.getFirst(cmds.duplicate(chainJoints[x], po = True, n = (name + str(x + 1) + "_JNT"))) ) 
        
        for x in range( 1, jointNo ):
            cmds.parent(joints[jointNo - x], joints[jointNo - (x + 1)])
        
        return joints
