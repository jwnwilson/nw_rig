import NWUtilitiesPackage.NWFileUtilities as fileUtil

__all__ = ["NWModule","NWSpineJoints","NWHingeJoints","NWRoot"]

for module in __all__:
	fileUtil.loadModule(__name__ + "." + module)

