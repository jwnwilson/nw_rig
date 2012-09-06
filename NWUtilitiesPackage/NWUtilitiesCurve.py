import maya.cmds as cmds
import NWUtilitiesString as string
import NWUtilitiesControl as control
# ------------------------
# curve functions
# ------------------------
def getCurveCVNumber(curve):
	return ( cmds.getAttr( (curve + ".spans") ) +  cmds.getAttr( (curve + ".degree") ) )

def clusterizeCurve(curve):
	curveNumber = getCurveCVNumber(curve)
	curveName = string.removeSuffix(curve)
	clusterName = (curveName + "Cluster")
	clusterList = []
	for x in range(curveNumber):
		clusterList.append( control.createCluster( ( clusterName + str(x) ), ( curve + ".cv["+ str(x) +"]" ) ) )
	return clusterList
	

	
