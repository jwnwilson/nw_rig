"""
    Default window file for NWRig uses UI modules to rig and manage NWRig tool

    Auther Noel: Wilson
    Date: 08/07/2012
"""
import os
import maya.cmds as cmds
from UtilitiesPackage import mayaImport, mayaFromImport
from WindowPackage import RigUI

reload(RigUI)
# doesn't work already called as exec can import file normally
#mayaFromImport("WindowPackage", "RigUI")

# Initialize window
window = RigUI.RigUI({"name":self.name, "windowWidth":500, "windowHeight":500, "title":"Window", "Rig":self})
# Root layout
window.layout({'key':'rootLayout','label':'root'})
# -----------------------------
# File tabs
# -----------------------------
methodTab = window.layout({'key':'methodTab','label':'tabs','type':'tabLayout'},height= 450,width= 550)
# -----------------------------
# File pannel
# -----------------------------
frame1 = window.layout({'key':'File','parent':methodTab,'label':'file','type':'frameLayout'}, height= 100)
window.text({'key':'fileFileText','label':'rig file path:','parent':frame1})
window.textField({'key':'fileFilePath','label':FILE_PATH,'parent':frame1})
fileForm = window.layout({'key':'fileForm','parent':frame1,'type':'formLayout'})
fileText = window.text({'key':'fileText1','label':'file menu','parent':fileForm})
fileNew = window.button({'key':'fileNewButton','label':'New','parent':fileForm,"command":"NWRig.UI.createPromptWindow(\"Close Scene\", \"cmds.file(f= True, new= True)\\nNWRig = NWRigSystem(\\\"nwRig\\\")\")"},width= 100)
fileSave = window.button({'key':'fileSaveButton','label':'Save all data','parent':fileForm, "command":"NWRig.saveAllData()"},width= 100)
fileLoad = window.button({'key':'fileLoadButton','label':'Load all data','parent':fileForm, "command":"NWRig.loadAllData()"},width= 100)
fileLoadRig = window.button({'key':'fileSaveRigButton','label':'Load rig','parent':fileForm, "command":"NWRig.loadRig()"},width= 100)
fileSaveRig  = window.button({'key':'fileLoadRigButton','label':'Save rig','parent':fileForm, "command":"NWRig.saveRig()"},width= 100)

# Edit form layout
attachForm = [  (fileText, "top", 5),
                (fileText, "left", 5)]
attachControl = [   (fileNew, "top", 10 ,fileText ),
                    (fileSaveRig, "top", 10 ,fileNew ),
                    (fileLoadRig, "top", 10 ,fileSaveRig ),
                    (fileSave, "top", 10 ,fileNew ),
                    (fileLoad, "top", 10 ,fileSaveRig ),
                    (fileSave, "left", 150 ,fileSaveRig ),
                    (fileLoad, "left", 150 ,fileLoadRig ),]
attachNone = []
                  
window.editElement("fileForm", af= attachForm, an= attachNone, ac= attachControl )

# -----------------------------
# Blueprint pannel
# -----------------------------
blueprintTab = window.layout({'key':'Blueprint','parent':methodTab,'label':'blueprinter','type':'frameLayout'}, height= 100)
window.text({'key':'blueprintText1','label':'Load blueprinter'})
window.text({'key':'blueprintText2','label':'Module name','parent':blueprintTab},align= "left")
window.textField({'key':'blueprintTextField','label':'defaultName','parent':blueprintTab})
blueprintForm = window.layout({'key':'blueprintForm','parent':blueprintTab,'type':'formLayout'})
blueprintScroll1 = window.layout({'key':'blueprintScroll','type':'scrollLayout','parent':blueprintForm, 'label':'blueprinters'},width= 250, height= 250)
window.loadBlueprintIcons()
blueprintAttributeframe = window.layout({'key':'blueprintAttributeframe','parent':blueprintForm,'label':'blueprintAttributes','type':'frameLayout'},width= 250,height= 250) 
blueprintBlueprintButton = window.button({'key':'blueprintBlueprintButton','parent':blueprintForm, 'label':'create blueprint',"command":"NWRig.UI.createBlueprintModule()"},width= 100)
blueprintSaveNewButton = window.button({'key':'blueprintSaveNewButton','parent':blueprintForm, 'label':'save new blueprint'},width= 100)

# Edit form layout
attachForm = [(blueprintScroll1, "top", 5),
              (blueprintScroll1, "left", 5),
              (blueprintAttributeframe, "top",5),
          (blueprintBlueprintButton, "left",5)]
attachNone = []
attachControl =  [(blueprintAttributeframe, "left", 5 ,blueprintScroll1 ),
            (blueprintBlueprintButton, "top",10,blueprintScroll1),
			(blueprintSaveNewButton, "left",10,blueprintBlueprintButton),
			(blueprintSaveNewButton, "top",10,blueprintScroll1)]
                  
window.editElement("blueprintForm", af= attachForm, an= attachNone, ac= attachControl )

# -----------------------------
# Rig pannel
# -----------------------------
rigTab = window.layout({'key':'Rig','parent':methodTab,'label':'rig','type':'frameLayout'})
window.text({'key':'rigText','label':'rig menu'})
rigForm = window.layout({'key':'rigForm','parent':rigTab,'type':'formLayout'})
rigScroll1 = window.layout({'key':'rigScroll','type':'scrollLayout','parent':rigForm, 'label':'rigScroll'},width= 250, height= 250)
rigAttributeframe = window.layout({'key':'rigAttributeframe','parent':rigForm,'label':'rigAttributes','type':'frameLayout'},width= 250,height= 250) 
rigRefreshButton = window.button({'key':'rigRefreshButton','parent':rigForm, 'label':'refresh menu',"command":"NWRig.UI.loadModules({})"},width= 100)
rigRenameButton = window.button({'key':'rigRenameButton','parent':rigForm, 'label':'rename module', "command":"NWRig.UI.renameModule()"},width= 100)
rigParentButton = window.button({'key':'rigParentButton','parent':rigForm, 'label':'parent module'},width= 100)
rigDeleteButton = window.button({'key':'rigDeleteButton','parent':rigForm, 'label':'delete module',"command": "NWRig.UI.deleteModule()"},width= 100)
rigButton = window.button({'key':'rigRigButton','parent':rigForm, 'label':'rig Mode',"command":"NWRig.rigMode()"},width= 100)
rigLoadButton = window.button({'key':'rigLoadButton','parent':rigForm, 'label':'load rig data', "command": "NWRig.loadRigData()"},width= 100)
rigSaveButton = window.button({'key':'rigSaveButton','parent':rigForm, 'label':'save rig data', "command": "NWRig.saveRigData()"},width= 100)
rigBlueprintButton = window.button({'key':'rigRigBlueprintButton','parent':rigForm, 'label':'Blueprints mode',"command":"NWRig.blueprintMode()\nNWRig.UI.loadModules({})"},width= 100)
rigBlueprintLoadButton = window.button({'key':'rigBlueprintLoadButton','parent':rigForm, 'label':'load blueprint data', "command": "NWRig.loadBlueprintData()"},width= 100)
rigBlueprintSaveButton = window.button({'key':'rigBlueprintSaveButton','parent':rigForm, 'label':'save blueprint data', "command": "NWRig.saveBlueprintData()"},width= 100)
rigBlueprintMirrorButton = window.button({'key':'rigBlueprintMirrorButton','parent':rigForm, 'label':'mirror blueprint', "command":"NWRig.UI.mirrorBlueprint()\nprint 'NWRig.UI.mirrorBlueprint()'"},width= 100)
rigBlueprintDuplicateButton = window.button({'key':'rigBlueprintDuplicateButton','parent':rigForm, 'label':'duplicate blueprint', "command":"NWRig.UI.duplicateBlueprint()\nprint 'NWRig.UI.duplicateBlueprint()'"},width= 100)

# Edit form layout
attachForm = [(rigScroll1, "top", 5),
              (rigScroll1, "left", 5),
              (rigRefreshButton, "left", 5),
              (rigAttributeframe, "top",5),
              (rigButton,"left", 5 ),
              (rigBlueprintButton,"left", 5 ),
			(rigBlueprintMirrorButton, "left",5)]
attachNone = []
attachControl =  [  (rigAttributeframe, "left", 10, rigScroll1),
                    (rigRefreshButton, "top", 10,rigScroll1 ),
                    (rigRenameButton, "left", 10, rigRefreshButton),
                    (rigRenameButton, "top", 10, rigScroll1),
                    (rigDeleteButton, "left", 10, rigRenameButton),
                    (rigDeleteButton, "top", 10, rigScroll1),
                    (rigBlueprintButton,"top", 50,rigRefreshButton),
                    (rigButton,"top", 10 , rigBlueprintButton ),
                    (rigLoadButton, "left",150,rigButton),
                    (rigLoadButton, "top",10,rigBlueprintButton),
                    (rigSaveButton, "left",10,rigLoadButton),
                    (rigSaveButton, "top",10,rigBlueprintButton),
                    (rigBlueprintLoadButton, "left",150,rigBlueprintButton),
                    (rigBlueprintLoadButton, "top",50,rigRefreshButton),
                    (rigBlueprintSaveButton, "left",10,rigBlueprintLoadButton),
                    (rigBlueprintSaveButton, "top",50,rigRefreshButton),
					(rigParentButton, "left", 10, rigDeleteButton),
					(rigParentButton, "top", 10, rigScroll1),
					(rigBlueprintMirrorButton, "top",10,rigRefreshButton),
            		(rigBlueprintDuplicateButton, "left",10,rigBlueprintMirrorButton),
            		(rigBlueprintDuplicateButton, "top",10,rigRefreshButton),]
                  
window.editElement("rigForm", af= attachForm, an= attachNone, ac= attachControl )
# -----------------------------
# Connect pannel
# -----------------------------
connectTab = window.layout({'key':'Connections','parent':methodTab,'label':'connect','type':'frameLayout'})
window.text({'key':'connectText','label':'connect menu','parent':connectTab})
connectForm = window.layout({'key':'connectForm','parent':connectTab,'type':'formLayout','parent':connectTab})
connectOutputText = window.text({'key':'connectOutputText','label':'output','parent':connectForm})
connectInputText = window.text({'key':'connectInputText','label':'input','parent':connectForm})
connectOutputButton = window.button({'key':'connectOutputButton','label':'Output Module','parent':connectForm, "command":"NWRig.UI.loadConnections(\"Output\")"},width= 100)
connectInputButton = window.button({'key':'connectInputButton','label':'Input Module','parent':connectForm, "command":"NWRig.UI.loadConnections(\"Input\")"},width= 100)
window.connectPopupMenus(connectInputButton, connectOutputButton)
connectInputScroll = window.layout({'key':'connectInputScroll','type':'scrollLayout','parent':connectForm},width= 250, height= 250)
connectOutputScroll = window.layout({'key':'connectOutputScroll','type':'scrollLayout','parent':connectForm},width= 250, height= 250)

#connectParentButton = window.button({'key':'connectParentButton','parent':connectForm, 'label':'parent'},width= 100)
connectConnectButton = window.button({'key':'connectConnectButton','parent':connectForm, 'label':'connect', "command": "NWRig.UI.connectOutputToInput()"},width= 100)
connectOptionMenu = window.optionMenu({'key':'connectConnectOptionMenu','parent':connectForm, 'label':'Maintain offset'},width= 200)
connectMaintainOffset = window.menuItem({'key':'connectMaintainOffset','parent':connectOptionMenu, 'label':'Maintain offset'})
connectNoMaintainOffset = window.menuItem({'key':'connectNoMaintainOffset','parent':connectOptionMenu, 'label':'No maintain offset'})

# Edit form layout
attachForm = [(connectOutputText, "top", 5),
              (connectOutputText, "left", 5),
              (connectOutputButton, "left", 5),
              (connectInputText, "left",5),
              (connectOutputScroll, "top",5),
              (connectInputText, "top", 5),
              (connectConnectButton,"left", 5)]
attachNone = [(connectOutputText, "right"),
              (connectOutputText, "bottom"),
              (connectOutputButton, "right"),
              (connectOutputButton, "bottom"),
              (connectOutputScroll, "right"),
              (connectOutputScroll, "bottom")]
attachControl =  [(connectOutputButton, "top", 10,connectOutputText ),
                  (connectOutputScroll,"top", 10,connectOutputButton),
                  (connectInputText,"left", 150,connectOutputButton),
                  (connectInputButton,"top", 10,connectInputText),
                  (connectInputButton,"left", 150,connectOutputButton),
                  (connectInputScroll,"top", 10,connectInputButton),
                  (connectInputScroll,"left", 10,connectOutputScroll),
                  #(connectParentButton,"top", 10,connectOutputScroll),
                  #(connectParentButton,"left", 10,connectConnectButton),
                  (connectConnectButton,"top", 10,connectInputScroll),
		  (connectOptionMenu,"left", 10,connectConnectButton),
                  (connectOptionMenu,"top", 10,connectInputScroll),]
                  
window.editElement("connectForm", af= attachForm, an= attachNone, ac= attachControl )
# -----------------------------
# Deformation pannel
# -----------------------------
deformTab = window.layout({'key':'Deformation','parent':methodTab,'label':'Deformation','type':'frameLayout'})
