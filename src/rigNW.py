# -*- coding: utf-8 -*-

"""
To do:
- Need to have multiple instances supported and namespaces for items in containers
- Lock blueprinter joints only allow manipulation through controls
- Needs more sub controls for blueprinters
- Blueprinter direction needs to be influenced by other blueprinter controls
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
                
def blueprintPrePost(blueprint):
        @wraps(blueprint)
        def wrapper(*args, **kwds):
            print ("calling :" + blueprint.__name__)
            ret = blueprint(*args, **kwds)
            args[0].blueprintComplete()
            return ret
        return wrapper
        
def rigPrePost(rig):
        @wraps(rig)
        def wrapper(*args, **kwds):
            print ("calling :" + rig.__name__)
            ret = rig(*args, **kwds)
            args[0].rigComplete()
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
    test.blueprint()
