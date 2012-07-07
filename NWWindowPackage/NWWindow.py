# -*- coding: utf-8 -*-

import maya.cmds as cmds
import NWUtilitiesPackage.NWUtilities as util
import sys

"""
To do:
   - Rewrite entire module store full path to every entity by a key
   - Every entity requires a key and a parent
   - Store list of all inputs
   - Use **kwargs correctly
"""

# temp addition to python path variable
ICON_PATH = "/icons"

class Element:
    def __init__(self, key , fullPath , parent , type , **kwargs):
        """
            Class to hold each data for each window element
        """
        # Each key must be unique
        self.key = key
        # Full path to GUI element
        self.fullPath = fullPath
        # PArent of element
        self.parent = parent
        # type must equal name of function used create element for edit to work
        self.type = type
        self.initialize(**kwargs)

    def initialize(self):
        pass

class Layout(Element):
    def initialize(self,**kwargs):
        #self.layoutType = util.checkForKwarg("layoutType",kwargs)
        self.button = util.checkForKwarg("button",kwargs)
        self.image = util.checkForKwarg("image",kwargs)
        self.NWRigInstance = util.checkForKwarg("rigInstance",kwargs)

class NWWindow:
    """ 
        Generic window GUI building class
    """
    def __init__(self, args, **kwds):
        """ Creates a window available arguements include:
           "name","windowWidth","windowHeight","title"
        """
        self.name = "window"
        self.name = util.checkForKwarg("name",kwds)
        #default args
        self.windowParamters = { "name":"window", "windowWidth":400, "windowHeight":400, "title":"NWWindow", "window":""}
        #overwrite defaults
        self.windowParamters =   util.defaultArgs( self.windowParamters , args)
        #stores each element of the window by a unique key
        self.windowElements ={}
        #store key of last used parent element
        self.currentParent= None
        # possibly obsolete
        self.layouts = {}
        # possibly obsolete
        self.images= {}
        # additional list for queryable inputs
        self.inputs= {}
        
        #args= {"h":self.windowParamters["windowWidth"], "w":self.windowParamters["windowHeight"], "title":self.windowParamters["title"]}
        self.initialiseWindow(**kwds)
        
        cmds.showWindow(self.windowParamters["window"])
        
        # For derived classes
        self.initialise(args, **kwds)
        
    def initialise(self,args, **kwds):
        """
            Dummy class to overwritten via inhertance
        """
        pass
        
    def initialiseWindow(self, **kwds):
        """
            Initialise window
        """
        functArgs =  util.defaultArgs( {"windowHeight":400, "windowWidth":400, "title":"WindowNW", "sizeable":True} , self.windowParamters)
        name = self.windowParamters["name"]
        
        if(cmds.window(name, exists=True)):
            cmds.deleteUI(name)
            
        print kwds
        
        self.windowParamters["window"] = cmds.window(name, width = functArgs["windowWidth"], height = functArgs["windowHeight"], title = functArgs["title"], sizeable = functArgs["sizeable"],**kwds)  
        self.currentParent = self.windowParamters["window"]
    
    #def addToLayout(self, control, layout):
    #    self.layouts[util.getSuffixByChar(layout, "|")].buttons.append(control)
        
    def refresh(self):
        """
            Refreshes window
        """
        name = self.windowParamters["name"]
        if(cmds.window(name, exists=True)):
            cmds.deleteUI(name)
           
        self.windowParamters["window"] = cmds.window(name, width = self.windowParamters["windowWidth"], height = self.windowParamters["windowHeight"], title = self.windowParamters["title"], sizeable=False)
        self.currentParent = self.windowParamters["window"]
        
        cmds.showWindow(self.windowParamters["window"])
        
    def saveElement(self,*args):
        """
            Stores window element data in a dict for easy modification
        """
        # check if element exists
        if self.elementExists(args[0]) == False:
            self.windowElements[args[0]] = Element(*args)
            return self.windowElements[args[0]]
        else:
            error("Non unique key given for window element")
            
    def removeElement(self,*args):
        """
            remove element from UI
        """
        # Hide element?
        pass
    
    def saveInput(self,*args):
        """
            Stores window input data in a dict for easy modification
        """
        self.inputs[args[0]] = self.saveElement(*args)
        
    def elementExists(self,element):
        """
            checks if element exists
        """
        if self.windowElements.has_key(element):
            return True
        else:
            return False
            
    def inputExists(self, input):
        """
            checks if input exists errors if it does
        """
        if self.inputs.has_key(input):
            return False
        else:
            error( "Input :" + input + " already exists" )
            return True
            
    def layout(self,args,**kwargs):
        """
            Creates a layout available arguements include:
           "key","type","columnNo","parent","width","height"
        """
        #adds layout to window
        defaultArgs = {"key": "layout",
                        "label":"label",
                        "type":"columnLayout",
                        "columnNo":3, 
                        "parent":self.windowParamters["window"], 
                        "width": self.windowParamters["windowWidth"], 
                        "height":self.windowParamters["windowHeight"] }
        functArgs =  util.defaultArgs( defaultArgs, args)
        layoutName = None
        
        # check if element already exists
        if self.elementExists(functArgs["key"]):
            cmds.error( "Element :" + element + " already exists")
        
        if(functArgs["type"] == "columnLayout"):
            layoutName = cmds.columnLayout(functArgs["key"], p= functArgs["parent"], adjustableColumn=True , height= functArgs["height"], width= functArgs["width"], **kwargs  )
        elif(functArgs["type"] == "rowLayout"):
            layoutName = cmds.rowLayout(functArgs["key"], p= functArgs["parent"] ,numberOfColumns= functArgs["columnNo"], height= functArgs["height"], width= functArgs["width"], **kwargs  )
        elif(functArgs["type"] == "tabLayout"):
            layoutName = cmds.tabLayout(functArgs["key"], p= functArgs["parent"], **kwargs )
        elif(functArgs["type"] == "frameLayout"):
            layoutName = cmds.frameLayout(functArgs["key"], l= functArgs["label"], p= functArgs["parent"],**kwargs )
        elif(functArgs["type"] == "formLayout"):
            layoutName = cmds.formLayout(functArgs["key"], p= functArgs["parent"],**kwargs )
        elif(functArgs["type"] == "scrollLayout"):
            layoutName = cmds.scrollLayout(functArgs["key"], p= functArgs["parent"], **kwargs )
        else:
            error("Layout not defined.")
            
        self.saveElement(functArgs["key"],layoutName,functArgs["parent"],functArgs["type"] )
        self.currentParent = functArgs["key"]
        return layoutName
        
    def button(self,args,**kwargs):
        """
            Adds button to window
        """
        defaultArgs = {"key": "button", 
                        "label": "button",
                        "type":"button",
                        "command":"print \"Button has been pressed\"", 
                        "parent":self.currentParent }
        functArgs =  util.defaultArgs( defaultArgs, args)
        buttonName=None
        
        # check if element already exists
        if self.elementExists(functArgs["key"]):
            cmds.error( "Element :" + element + " already exists")
        # Check parent exists for button
        if(functArgs["parent"] == None):
            cmds.error("No parent found for button")
        
        buttonName = cmds.button(p = functArgs["parent"], l = functArgs["label"], c =functArgs["command"],**kwargs )
        self.saveElement(functArgs["key"],buttonName, functArgs["parent"],functArgs["type"])
        
        return buttonName
    
    def symbolButton(self,args,**kwargs):
        """
            Adds symbol button to window
        """
        defaultArgs = {"key": "button", 
                        "label": "symbolButton",
                        "type":"symbolButton",
                        "command":"print \"Button has been pressed\"", 
                        "parent":self.currentParent, 
                        "image":"default.png" }
        functArgs =  util.defaultArgs( defaultArgs, args)
        buttonName=None
        
        # check if element already exists
        if self.elementExists(functArgs["key"]):
            cmds.error( "Element :" + element + " already exists")
        # Check parent exists for button
        if(functArgs["parent"] == None):
            cmds.error("No parent found for button")
        
        buttonName= cmds.symbolButton(p = functArgs["parent"], c =functArgs["command"], i = functArgs["image"],**kwargs )
        self.saveElement(functArgs["key"],buttonName, functArgs["parent"],functArgs["type"])
        
        return buttonName
    
    def text(self,args,**kwargs):
        """
            Adds text to window
        """
        defaultArgs = {"key": "text",
                        "label":"text",
                        "type":"text",
                        "parent":self.currentParent }
        functArgs =  util.defaultArgs( defaultArgs, args)
        textName=None
        
        # check if element already exists
        if self.elementExists(functArgs["key"]):
            cmds.error( "Element :" + element + " already exists")
        # Check parent exists for button
        if(functArgs["parent"] == None):
            cmds.error("No parent found for text")
            
        textName= cmds.text(p = functArgs["parent"], l = functArgs["label"], **kwargs )
        self.saveElement(functArgs["key"], textName, functArgs["parent"],functArgs["type"])
        
        return textName
    
    def textField(self,args,**kwargs ):
        """
            Adds text field to window
        """
        defaultArgs = {"key": "key",
                        "label":"textField",
                        "type":"textField",
                        "parent":self.currentParent }
        functArgs =  util.defaultArgs( defaultArgs, args)
        textName= None
        
        # check if element already exists
        if self.elementExists(functArgs["key"]):
            cmds.error( "Element :" + element + " already exists")
        # Check parent exists for button
        if(functArgs["parent"] == None):
            cmds.error("No parent found for text field")
        
        # Moving to edit input function
        #if functArgs["key"] in self.inputs.keys():
        #   textName= cmds.textField(self.inputs[functArgs["key"]], edit= True, p = functArgs["parent"], tx = functArgs["label"] )
        
        textName= cmds.textField(p = functArgs["parent"], tx = functArgs["label"], **kwargs  )
        self.saveInput(functArgs["key"], textName, functArgs["parent"],functArgs["type"])
        
        return textName
    def iconTextScrollList(self,args, **kwargs):
        """
            Adds icon text scroll list to window
        """
        defaultArgs = {"key": "key",
                        "label":"textScrollList",
                        "type":"iconTextScrollList",
                        "parent":self.currentParent, 
                        "append": ["default"] }
        functArgs =  util.defaultArgs( defaultArgs, args)
        
        # check if element already exists
        if self.elementExists(functArgs["key"]):
            cmds.error( "Element :" + element + " already exists")
        # Check parent exists for button
        if(functArgs["parent"] == None):
            cmds.error("No parent found for text field")
        
        # Moving to edit input function
        #if functArgs["key"] in self.inputs.keys():
        #    iconTextName= cmds.iconTextScrollList(self.inputs[functArgs["key"]], e= True, ra= True, p = functArgs["parent"], allowMultiSelection= True, append= functArgs["scrollList"] ,**kwargs)
        
        iconTextName= cmds.iconTextScrollList(p = functArgs["parent"], allowMultiSelection= True, append= functArgs["append"],**kwargs )
        self.saveInput(functArgs["key"], iconTextName, functArgs["parent"],functArgs["type"])
        
        return iconTextName
    def editElement(self, key, **kwargs):
        """ 
            Asks for the key of an element to edit
            kwargs is a list of args that are passed into an edit function
            E.g. editLayout("layout1", l="newLayout", width= 500)
        """
        # check for full path
        if self.elementExists( key ) == False:
            cmds.error( "Element :" + element + " not found to edit")
        
        element = self.windowElements[key]
        command = None
        
        if element.type != None or element.type != "":
            command = "ret = cmds."+ element.type +"(\""+ element.fullPath + "\",e=True"
        else:
            error(("layoutType not found when editting layout: " + label))
            
        for key in kwargs:
            if type(kwargs[key]) == type( [] ):
                command += (", " + key + "= " + str(kwargs[key]))
            elif type(kwargs[key]) == type( True ):
                command += (", " + key + "= " + str(kwargs[key]))
            else:
                command += (", " + key + "= \"" + str(kwargs[key])+ "\"")
            
        command += " )"
        exec command
        
        return ret
        
    def queryInput(self, inputKey, **kwargs ):
        """
            Get UI input type
        """
        returnVal = ""
        # Check input exists
        self.inputExists(inputKey)
        
        inputElement = self.inputs[inputKey]
        
        #error("This function requires testing for different UI types")
        
        guiType = cmds.objectTypeUI(inputElement.fullPath)
        if guiType == "outlineControl":
            returnVal = cmds.iconTextScrollList(inputElement.fullPath, q = True, si = True, **kwargs)
        elif guiType == "field":
            returnVal = cmds.textField(inputElement.fullPath, q = True, tx = True, **kwargs)
        
        return returnVal
        
    def buildWindowFromFile(self,file):
        """ 
            read in UIFile
        """
        # path to file
        currentDir = __path__
        filePath = (currentDir + "/blueprints/" + file)
        
        FILE = open(filePath,"rU")
        command = FILE.read()
        FILE.close()
        exec command
    
# just some testing
if __name__ == "__main__":
    test = NWWindow({})
