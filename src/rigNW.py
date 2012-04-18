# -*- coding: utf-8 -*-

"""
To do:
- Need to have multiple instances supported and namespaces for items in containers
- Lock starter joints only allow manipulation through controls
- Needs more sub controls for starters
- Starter direction needs to be influenced by other starter controls
"""

import maya.standalone
maya.standalone.initialize()

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaAnim as OpenMayaAnim
import ctypes
import os
import sys
import maya.OpenMaya as OpenMaya
from functools import wraps

ROOT_PATH=[]
ROOT_PATH.append("/net/homes/nwilson/Documents/Python/NWRig/")
ROOT_PATH.append("H:/Python/NWRig/src/")
ROOT_PATH.append("C:/Documents and Settings/Noel Wilson/My Documents/python/NWRig/src/")

# source Window

# source Utilities

# source Modules

# temp addition to python path variable
for path in ROOT_PATH:
        sys.path.append( path )

import rigNWUtilities as util
import rigNWWindow as ui
util = reload(util)
ui = reload(ui)

UI_PATH = (ROOT_PATH[1] + ui.ICON_PATH)

#from rigNWUtilities import *

class Command:
        def __init__(self,name): 
                self.name = name
                
def startPrePost(start):
        @wraps(start)
        def wrapper(*args, **kwds):
            print ("calling :" + start.__name__)
            ret = start(*args, **kwds)
            args[0].startComplete()
            return ret
        return wrapper
        
def buildPrePost(build):
        @wraps(build)
        def wrapper(*args, **kwds):
            print ("calling :" + build.__name__)
            ret = build(*args, **kwds)
            args[0].buildComplete()
            return ret
        return wrapper 

#contains rig system
class RigNW:
        def __init__(self, name):
                self.Modules = []
                self.Connections = []
                self.name = name
                self.UI = WindowNW()



if __name__ == "__main__":
    print "test"
    test = HingeJoints("test")
    test.start()
