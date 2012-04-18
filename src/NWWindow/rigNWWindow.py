# -*- coding: utf-8 -*-

import maya.cmds as cmds
import sys

# temp addition to python path variable
ICON_PATH = "/icons"

class Layout:
    def __init__(self,fullPath,LayoutType):
        self.fullPath = fullPath
        self.buttons=[]
        self.layoutType = LayoutType
        self.images= {}

class WindowNW:
    """ Creates a class which will create and manage a UI wrapping around maya's
    functionallity
    """
    def __init__(self, args):
        """ Creates a window available arguements include:
           "name","windowWidth","windowHeight","title"
        """
        #default args
        self.windowElements = {"name":"window"}
        self.currentParent= None
        self.windowElements["windowWidth"] = 400
        self.windowElements["windowHeight"] = 400
        self.windowElements["title"] = "windowNW"
        #overwrite defaults
        self.windowElements =  dict(self.windowElements.items() + args.items())
        self.layouts = {}
        
        args= {"h":self.windowElements["windowWidth"], "w":self.windowElements["windowHeight"], "title":self.windowElements["title"]}
        self.initialise(args)
        
        cmds.showWindow(self.windowElements["window"])
        
    def initialise(self, args):
        # initialise window
        functArgs = {"h":400, "w":400, "title":"WindowNW"}
        functArgs =  dict(functArgs.items() + args.items())
        name = self.windowElements["name"]
        
        if(cmds.window(name, exists=True)):
            cmds.deleteUI(name)
           
        self.windowElements["window"] = cmds.window(name, width = self.windowElements["windowWidth"], height = self.windowElements["windowHeight"], title = name, sizeable=False)  
        self.currentParent = self.windowElements["window"]
        
    def refresh(self):
        #refreshes window
        name = self.windowElements["name"]
        if(cmds.window(name, exists=True)):
            cmds.deleteUI(name)
           
        self.windowElements["window"] = cmds.window(name, width = self.windowElements["windowWidth"], height = self.windowElements["windowHeight"], title = name, sizeable=False)
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
        self.layouts[functArgs["parent"]].buttons.append(buttonName)
        return buttonName
    def symbolButton(self,args):
        #adds button to window
        functArgs = {"label": "button", "command":"print \"Button has been pressed\"", "parent":self.currentParent, "image":"default.png", "layout":self.layouts[self.currentParent].fullPath }
        functArgs =  dict(functArgs.items() + args.items())
        buttonName=None
        if(len(self.layouts) ==0):
            cmds.error("No layouts have been created")
        buttonName= cmds.button(p = functArgs["parent"], l = functArgs["label"], c =functArgs["command"], i = functArgs["image"] )
        self.layouts[functArgs["parent"]].buttons.append(buttonName)
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
        
    def editLayout(self, label, **kwargs):
        """ asks for the label of a layout to edit (which should match it's name)
            kwargs is a list of args that are passed into an edit function for the layout
            pass arguements as you would for normal python functions e.g.
            editLayout("layout1", l="newLayout", width= 500)
        """
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
            command += (", " + key + "= \"" + kwargs[key]+ "\"")
        command += " )"
        
        exec command

# just some testing
if __name__ == "__main__":
    test = WindowNW({})
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
