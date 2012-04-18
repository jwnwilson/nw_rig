# -*- coding: utf-8 -*-

import maya.cmds as cmds
import NWUtilitiesPackage.NWUtilities as util
import sys

"""
To do:
   - Require a check when adding layout that layout doesn't already exist
   - Require an add to layout function that does check and removes prefixes
   - Move specialised code for rigging tool to a derived class
"""

# temp addition to python path variable
ICON_PATH = "/icons"

class Layout:
    def __init__(self,fullPath,LayoutType):
        self.fullPath = fullPath
        self.buttons=[]
        self.layoutType = LayoutType
        self.images= {}
        self.NWRigInstance = None

class NWWindow:
    """ Creates a class which will create and manage a UI wrapping around maya's
    functionallity
    """
    def __init__(self, args, **kwds):
        """ Creates a window available arguements include:
           "name","windowWidth","windowHeight","title"
        """
        self.NWRigInstance = kwds["NWRig"]
        #default args
        self.windowElements = {"name":"window"}
        self.currentParent= None
        self.windowElements["windowWidth"] = 400
        self.windowElements["windowHeight"] = 400
        self.windowElements["title"] = "NWWindow"
        #overwrite defaults
        self.windowElements =  dict(self.windowElements.items() + kwds.items())
        self.layouts = {}
        self.images= {}
        self.inputs= {}
        self.name = kwds["name"]
        
        args= {"h":self.windowElements["windowWidth"], "w":self.windowElements["windowHeight"], "title":self.windowElements["title"]}
        self.initialise(args)
        
        cmds.showWindow(self.windowElements["window"])
        
    def initialise(self, args):
        # initialise window
        functArgs = {"h":400, "w":400, "title":"WindowNW", "sizeable":True}
        functArgs =  dict(functArgs.items() + args.items())
        name = self.windowElements["name"]
        
        if(cmds.window(name, exists=True)):
            cmds.deleteUI(name)
        
        print self.windowElements
        self.windowElements["window"] = cmds.window(name, width = self.windowElements["windowWidth"], height = self.windowElements["windowHeight"], title = self.windowElements["title"], sizeable=functArgs["sizeable"])  
        self.currentParent = self.windowElements["window"]
    def addToLayout(self, control, layout):
        self.layouts[util.getSuffixByChar(layout, "|")].buttons.append(control)
        
    def refresh(self):
        #refreshes window
        name = self.windowElements["name"]
        if(cmds.window(name, exists=True)):
            cmds.deleteUI(name)
           
        self.windowElements["window"] = cmds.window(name, width = self.windowElements["windowWidth"], height = self.windowElements["windowHeight"], title = self.windowElements["title"], sizeable=False)
        self.currentParent = self.windowElements["window"]
        
        cmds.showWindow(self.windowElements["window"])
    
    def layout(self,args):
        """Creates a layout available arguements include:
           "label","type","columnNo","parent","width","height"
        """
        #adds layout to window
        functArgs = {"label": "layout", "type":"columnLayout","columnNo":3, "parent":self.windowElements["window"], "width": self.windowElements["windowWidth"], "height":self.windowElements["windowHeight"] }
        functArgs =  dict(functArgs.items() + args.items())
        layoutName = None
        layoutType = None
        
        if(functArgs["type"] == "columnLayout"):
            if self.layouts.has_key(functArgs["label"]):
                cmds.error(("layout already exists in: " + self.windowElements["name"]))
            layoutName = cmds.columnLayout(functArgs["label"], p= functArgs["parent"], adjustableColumn=True , height= functArgs["height"], width= functArgs["width"]  )
            layoutType = "column"
        elif(functArgs["type"] == "rowLayout"):
            if self.layouts.has_key(functArgs["label"]):
                cmds.error(("layout already exists in: " + self.windowElements["name"]))
            layoutName = cmds.rowLayout(functArgs["label"], p= functArgs["parent"] ,numberOfColumns= functArgs["columnNo"], height= functArgs["height"], width= functArgs["width"]  )
            layoutType = "row"
        elif(functArgs["type"] == "tabLayout"):
            if self.layouts.has_key(functArgs["label"]):
                cmds.error(("layout already exists in: " + self.windowElements["name"]))
            layoutName = cmds.tabLayout(functArgs["label"], p= functArgs["parent"] )
            layoutType = "tab"
        elif(functArgs["type"] == "frameLayout"):
            if self.layouts.has_key(functArgs["label"]):
                cmds.error(("layout already exists in: " + self.windowElements["name"]))
            layoutName = cmds.frameLayout(functArgs["label"], l= functArgs["label"], p= functArgs["parent"] )
            layoutType = "frame"         
        elif(functArgs["type"] == "formLayout"):
            if self.layouts.has_key(functArgs["label"]):
                cmds.error(("layout already exists in: " + self.windowElements["name"]))
            layoutName = cmds.formLayout(functArgs["label"], l= functArgs["label"], p= functArgs["parent"] )
            layoutType = "form"
        elif(functArgs["type"] == "scrollLayout"):
            if self.layouts.has_key(functArgs["label"]):
                cmds.error(("layout already exists in: " + self.windowElements["name"]))
            layoutName = cmds.scrollLayout(functArgs["label"], p= functArgs["parent"] )
            layoutType = "form"    
        else:
            cmds.error("layout not defined.")
            
        self.layouts[functArgs["label"]] = Layout(layoutName, layoutType)
        self.currentParent = functArgs["label"]
        return layoutName
        
    def button(self,args):
        #adds button to window
        functArgs = {"label": "button", "command":"print \"Button has been pressed\"", "parent":self.currentParent, "layout":self.layouts[self.currentParent].fullPath }
        functArgs =  dict(functArgs.items() + args.items())
        buttonName=None
        if(len(self.layouts) ==0):
            cmds.error("No layouts have been created")
        buttonName= cmds.button(p = functArgs["parent"], l = functArgs["label"], c =functArgs["command"] )
        #self.layouts[util.getSuffixByChar(functArgs["parent"], "|")].buttons.append(buttonName)
        self.addToLayout(buttonName , functArgs["parent"])
        return buttonName
    def symbolButton(self,args):
        #adds button to window
        functArgs = {"label": "button", "command":"print \"Button has been pressed\"", "parent":self.currentParent, "image":"default.png", "layout":self.layouts[self.currentParent].fullPath }
        functArgs =  dict(functArgs.items() + args.items())
        buttonName=None
        if(len(self.layouts) ==0):
            cmds.error("No layouts have been created")
        buttonName= cmds.symbolButton(p = functArgs["parent"], c =functArgs["command"], i = functArgs["image"] )
        #self.layouts[functArgs["parent"]].buttons.append(buttonName)
        self.addToLayout(buttonName , functArgs["parent"])
        self.images[buttonName] = functArgs["image"]
        return buttonName
    def text(self,args):
        #adds text to window
        functArgs = {"label": "label","parent":self.currentParent }
        functArgs =  dict(functArgs.items() + args.items())
        textName=None
        if(len(self.layouts) ==0):
            cmds.error("No layouts have been created")
        textName= cmds.text(p = functArgs["parent"], l = functArgs["label"] )
        return textName
    def textField(self,args):
        #adds text to window
        functArgs = {"label": "label","parent":self.currentParent }
        functArgs =  dict(functArgs.items() + args.items())
        textName=None
        if(len(self.layouts) ==0):
            cmds.error("No layouts have been created")
        if functArgs["label"] in self.inputs.keys():
            textName= cmds.textField(self.inputs[functArgs["label"]], edit= True, p = functArgs["parent"], tx = functArgs["label"] )
        else:
            textName= cmds.textField(p = functArgs["parent"], tx = functArgs["label"] )
            self.inputs[functArgs["label"]] = textName
        return textName
    def iconTextScrollList(self,args):
        functArgs = {"label": "label","parent":self.currentParent, "scrollList": ["default"] }
        functArgs =  dict(functArgs.items() + args.items())
        if functArgs["label"] in self.inputs.keys():
            iconTextName= cmds.iconTextScrollList(self.inputs[functArgs["label"]], e= True, ra= True, p = functArgs["parent"], allowMultiSelection= True, append= functArgs["scrollList"] )
        else:
            iconTextName= cmds.iconTextScrollList(p = functArgs["parent"], allowMultiSelection= True, append= functArgs["scrollList"] )
            self.inputs[functArgs["label"]] = iconTextName
        return iconTextName
    def editLayout(self, label, **kwargs):
        """ asks for the label of a layout to edit (which should match it's name)
            kwargs is a list of args that are passed into an edit function for the layout
            pass arguements as you would for normal python functions e.g.
            editLayout("layout1", l="newLayout", width= 500)
        """
        # check for full path
        labelArray =  label.split('|')
        if len(labelArray) > 1:
            label = labelArray[len(labelArray) - 1 ]
        # edits layout with given args
        if not self.layouts.has_key(label):
            cmds.error(("layout not found in editlayout for label: " + label))
        layoutInst = self.layouts[label]
        command = None
        
        if(layoutInst.layoutType == "column"):
            command = "cmds.columnLayout(\""+ label +"\",e=True"
        elif(layoutInst.layoutType == "row"):
            command = "cmds.rowLayout(\""+ label +"\",e=True"
        elif(layoutInst.layoutType == "tab"):
            command = "cmds.tabLayout(\""+ label +"\",e=True"
        elif(layoutInst.layoutType == "frame"):
            command = "cmds.frameLayout(\""+ label +"\",e=True"
        elif(layoutInst.layoutType == "form"):
            command = "cmds.formLayout(\""+ label +"\",e=True"
        elif(layoutInst.layoutType == "scroll"):
            command = "cmds.scrollLayout(\""+ label +"\",e=True"
        else:
            error(("layoutType not found when editting layout: " + label))
            
        for key in kwargs:
            if type(kwargs[key]) == type( () ):
                command += (", " + key + "= " + str(kwargs[key]))
            else:
                command += (", " + key + "= \"" + kwargs[key]+ "\"")
        command += " )"
        
        exec command
    def queryInput(self, input):
        # Get UI input type
        guiType = cmds.objectTypeUI(self.inputs["buildList"])
        if guiType == "outlineControl":
            name = cmds.iconTextScrollList(self.inputs["buildList"], q = True, si = True)
        elif guiType == "field":
            name = cmds.iconTextScrollList(self.inputs["starterName"], q = True, tx = True)
        # Remove spaces
        name = name[0].encode('utf8')
        name = name.strip()
        return name
    def loadStarters(self, path):
        """ Load icon for each module available
        """
        # get list of modules to load
        windowDir = path
        filePath = (windowDir[0] + "/ui/moduleList.txt")
        iconPath = (windowDir[0] + "/icons/")
        FILE = open(filePath,"rb")
        for line in FILE:
            args = line.split(' ')
            self.loadIcon(args[0],(iconPath + args[1].rstrip()))
        FILE.close()
        
    def loadBuilds(self,args):
        """ Load icon for each module available
        """
        functArgs = {"label": "buildList"}
        functArgs =  dict(functArgs.items() + args.items())
        # Search for containers
        rootContainer = ""
        if cmds.objExists( (self.name + "_CNT")):
            rootContainer = (self.name + "_CNT")
            # recursively find children build root then build it's children under it etc
            self.loadBuildRecursive(rootContainer,functArgs)
        else:
            pass
    def loadBuildRecursive(self,rootContainer,args):
        """Recursively find children build root then build it's children under it"""
        # Build Container
        buildModuleList = []
        buildModuleList.append(rootContainer)
        # Create list of names use indent in name for children
        if cmds.objExists(rootContainer):
            buildModuleList += self.getChildrenRecursive(rootContainer)
            # Pass list to text scroll list
            functArgs = {"scrollList": buildModuleList}
            functArgs =  dict(functArgs.items() + args.items())
            self.iconTextScrollList(functArgs)
        # Build children under rootContainer
    def getChildrenRecursive(self,rootContainer):
        buildModuleList = []
        #buildModuleList.append(rootContainer)
        children = cmds.container(rootContainer, query= True, nodeList= True)
        if children:
            for child in children:
                if cmds.objExists(child):
                    childName = ("   " + child)
                    buildModuleList.append(childName)
                    recuChildren = self.getChildrenRecursive(child)
                    if recuChildren:
                        for recuChild in recuChildren:
                            buildModuleList.append(("   " + recuChild))
        return buildModuleList
    def buildRecursive(self,args):
        """Get selected modules and build them recersively"""
        modules= []
        name = self.queryInput("buildList")
        modules.append(name)
        modules += self.getChildrenRecursive(name)
        for module in modules:
            module = util.removeSuffix(module)
            self.buildModule({"module": "NWRoot", "name": module})            
    def buildModule(self,args):
        """Get selected modules and build them"""
        functArgs = {"name": "default"}
        functArgs =  dict(functArgs.items() + args.items())
        self.NWRigInstance.buildModule( functArgs )
    def loadIcon(self, module, icon):
        """ Load icon
        """
        functArgs = {"image": icon, "command": ("NWRig" + ".startModule( '"+ module + "')")}
        self.symbolButton(functArgs)

# just some testing
if __name__ == "__main__":
    test = NWWindow({})
    test.layout({"label":"root"})
    tabs = test.layout({"type":"tabLayout"})
    #scroll = test.layout({"type":"scrollLayout","parent":tabs, "label":"scroll1"})
    tab1 = test.layout({"parent":tabs,"label":"layout1","type":"frameLayout"})
    test.text({})
    test.button({})
    test.button({})
    test.layout({"parent":tabs,"label":"layout2","type":"frameLayout"})
    test.text({})
    test.button({})
    test.button({})
    test.editLayout("layout2",l="newLayout")
    test.editLayout(tabs,tabLabel= {tab1:"newTabName"})
