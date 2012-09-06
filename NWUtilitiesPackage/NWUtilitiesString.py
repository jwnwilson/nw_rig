import maya.cmds as cmds

# ------------------------
# string functions 
# ------------------------
def getValueFromDataString(string, key):
	"""
		will read array data is organised in the format
		key:, data, key:, data, key:
	"""
	array = string.split(" ")
	index = 0;
	for obj in array:
		if obj == (key +":"):
			return array[index +1]
		index +=1
	cmds.error("Key: " + key + " not found in data array.")
	
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
