"""
    Default window file for NWRig uses UI modules to build and manage NWRig tool

    Auther Noel: Wilson
    Date: 08/07/2012
"""
import os
# Get OS system
if os.name == 'posix':
    FILE_PATH = "/media/WALKMAN/Python/NWRig/testRig/"
elif os.name == 'nt':
    FILE_PATH = "C:/Documents and Settings/Noel Wilson/My Documents/Python/NWRig/testRig/"

# Initialize window
window = NWWindowRigUI.NWWindowRigUI({"name":self.name, "windowWidth":400, "windowHeight":400, "title":"NWWindow", "NWRig":self})
# Root layout
window.layout({'key':'rootLayout','label':'root'})
# -----------------------------
# Create tabs
# -----------------------------
methodTab = window.layout({'key':'methodTab','label':'tabs','type':'tabLayout'},height= 400,width= 400)
# -----------------------------
# Create pannel
# -----------------------------
frame1 = window.layout({'key':'createFrame','parent':methodTab,'label':'create','type':'frameLayout'}, height= 100)
window.text({'key':'createFileText','label':'rig file path:','parent':frame1})
window.textField({'key':'createFilePath','label':FILE_PATH,'parent':frame1})
window.text({'key':'createText1','label':'create menu'})
window.button({'key':'createNewButton','label':'New'})
window.button({'key':'createSaveButton','label':'Save'})
window.button({'key':'createLoadButton','label':'Load'})
# -----------------------------
# Start pannel
# -----------------------------
startTab = window.layout({'key':'startFrame','parent':methodTab,'label':'starter','type':'frameLayout'}, height= 100)
window.text({'key':'startText1','label':'Load starter'})
window.text({'key':'startText2','label':'Module name','parent':startTab})
window.textField({'key':'startTextField','label':'starterName','parent':startTab})
scroll1 = window.layout({'key':'startScroll','type':'scrollLayout','parent':startTab, 'label':'starters'})
window.loadStartIcons()
startLoadButton = window.button({'key':'startLoadButton','parent':startTab, 'label':'load',"command":"NWRig.loadStartData()"},width= 100)
startSaveButton = window.button({'key':'startSaveButton','parent':startTab, 'label':'save',"command":"NWRig.saveStartData()"},width= 100)
# -----------------------------
# Build pannel
# -----------------------------
buildTab = window.layout({'key':'buildFrame','parent':methodTab,'label':'build','type':'frameLayout'})
window.text({'key':'buildText','label':'build menu'})
buildForm = window.layout({'key':'buildForm','parent':buildTab,'type':'formLayout'})
buildScroll1 = window.layout({'key':'buildScroll','type':'scrollLayout','parent':buildForm, 'label':'buildScroll'},width= 250, height= 150)
buildAttributeframe = window.layout({'key':'buildAttributeframe','parent':buildForm,'label':'buildAttributes','type':'frameLayout'},width= 250,height= 140) 
buildRefreshButton = window.button({'key':'buildRefreshButton','parent':buildForm, 'label':'refresh',"command":"NWRig.UI.loadModules({})"},width= 100)
buildButton = window.button({'key':'buildBuildButton','parent':buildForm, 'label':'build',"command":"NWRig.UI.buildModules({})"},width= 100)
buildLoadButton = window.button({'key':'buildLoadButton','parent':buildForm, 'label':'load'},width= 100)
buildSaveButton = window.button({'key':'buildSaveButton','parent':buildForm, 'label':'save'},width= 100)

# Edit form layout
attachForm = [(buildScroll1, "top", 5),
              (buildScroll1, "left", 5),
              (buildRefreshButton, "left", 5),
              (buildAttributeframe, "top",5)]
attachNone = [(buildScroll1, "right"),
              (buildScroll1, "bottom"),
              (buildRefreshButton, "right"),
              (buildRefreshButton, "bottom"),
              (buildButton, "right"),
              (buildButton, "bottom"),
              (buildAttributeframe, "right"),
              (buildAttributeframe, "bottom"),
              (buildLoadButton, "right"),
              (buildLoadButton, "bottom"),
              (buildSaveButton, "right"),
              (buildSaveButton, "bottom")]
attachControl =  [(buildRefreshButton, "top", 10,buildScroll1 ),
                  (buildButton,"top", 10,buildScroll1),
                  (buildButton,"left", 10,buildRefreshButton),
                  (buildAttributeframe, "left", 10, buildScroll1),
                  (buildLoadButton, "left",50,buildButton),
                  (buildLoadButton, "top",10,buildScroll1),
                  (buildSaveButton, "left",10,buildLoadButton),
                  (buildSaveButton, "top",10,buildScroll1)]
                  
window.editElement("buildForm", af= attachForm, an= attachNone, ac= attachControl )
# -----------------------------
# Connect pannel
# -----------------------------
connectTab = window.layout({'key':'connectFrame','parent':methodTab,'label':'connect','type':'frameLayout'})
connectScroll = window.layout({'key':'connectScroll','type':'scrollLayout','parent':connectTab},width= 250, height= 250)
connectParentButton = window.button({'key':'connectParentButton','parent':connectTab, 'label':'parent'},width= 100)
