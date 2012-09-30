import maya.cmds as cmds
import String
import Control

# ------------------------
# curve functions
# ------------------------
def getCurveCVNumber(curve):
	return ( cmds.getAttr( (curve + ".spans") ) +  cmds.getAttr( (curve + ".degree") ) )

def clusterizeCurve(curve):
	curveNumber = getCurveCVNumber(curve)
	curveName = String.removeSuffix(curve)
	clusterName = (curveName + "Cluster")
	clusterList = []
	for x in range(curveNumber):
		clusterList.append( Control.createCluster( ( clusterName + str(x) ), ( curve + ".cv["+ str(x) +"]" ) ) )
	return clusterList
	

	
