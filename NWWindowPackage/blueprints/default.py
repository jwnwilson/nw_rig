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
    FILE_PATH = "F:/Documents and Settings/Noel Wilson/My Documents/Git/NWRig/testRig/"

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
window.button({'key':'createNewButton','label':'New',"command":"cmds.file(f= True, new= True)"})
window.button({'key':'createSaveButton','label':'Save'})
window.button({'key':'createLoadButton','label':'Load'})
# -----------------------------
# Start pannel
# -----------------------------
startTab = window.layout({'key':'startFrame','parent':methodTab,'label':'starter','type':'frameLayout'}, height= 100)
window.text({'key':'startText1','label':'Load starter'})
window.text({'key':'startText2','label':'Module name','parent':startTab},align= "left")
window.textField({'key':'startTextField','label':'starterName','parent':startTab})
startForm = window.layout({'key':'startForm','parent':startTab,'type':'formLayout'})
startScroll1 = window.layout({'key':'startScroll','type':'scrollLayout','parent':startForm, 'label':'starters'},width= 250, height= 150)
window.loadStartIcons()
startAttributeframe = window.layout({'key':'startAttributeframe','parent':startForm,'label':'startAttributes','type':'frameLayout'},width= 250,height= 150) 
startLoadButton = window.button({'key':'startLoadButton','parent':startForm, 'label':'load',"command":"NWRig.loadStartData()"},width= 100)
startSaveButton = window.button({'key':'startSaveButton','parent':startForm, 'label':'save',"command":"NWRig.saveStartData()"},width= 100)
startStartButton = window.button({'key':'startStartButton','parent':startForm, 'label':'start',"command":"NWRig.UI.startModules()"},width= 100)

# Edit form layout
attachForm = [(startScroll1, "top", 5),
              (startScroll1, "left", 5),
              (startAttributeframe, "top",5),
	      (startStartButton, "left",5)]
attachNone = [(startScroll1, "right"),
              (startScroll1, "bottom"),
              (startAttributeframe, "right"),
              (startAttributeframe, "bottom"),
	      (startLoadButton, "right"),
              (startLoadButton, "bottom"),
	      (startSaveButton, "right"),
              (startSaveButton, "bottom")]
attachControl =  [(startAttributeframe, "left", 5 ,startScroll1 ),
		  (startStartButton, "top",10,startScroll1),
		  (startLoadButton, "left",100,startStartButton),
                  (startLoadButton, "top",10,startScroll1),
		  (startSaveButton, "left",10,startLoadButton),
		  (startSaveButton, "top",10,startScroll1)]
                  
window.editElement("startForm", af= attachForm, an= attachNone, ac= attachControl )

# -----------------------------
# Build pannel
# -----------------------------
buildTab = window.layout({'key':'buildFrame','parent':methodTab,'label':'build','type':'frameLayout'})
window.text({'key':'buildText','label':'build menu'})
buildForm = window.layout({'key':'buildForm','parent':buildTab,'type':'formLayout'})
buildScroll1 = window.layout({'key':'buildScroll','type':'scrollLayout','parent':buildForm, 'label':'buildScroll'},width= 250, height= 150)
buildAttributeframe = window.layout({'key':'buildAttributeframe','parent':buildForm,'label':'buildAttributes','type':'frameLayout'},width= 250,height= 150) 
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
window.text({'key':'connectText','label':'connect menu','parent':connectTab})
connectForm = window.layout({'key':'connectForm','parent':connectTab,'type':'formLayout','parent':connectTab})
connectOutputText = window.text({'key':'connectOutputText','label':'output','parent':connectForm})
connectInputText = window.text({'key':'connectInputText','label':'input','parent':connectForm})
connectOutputButton = window.button({'key':'connectOutputButton','label':'Output Module','parent':connectForm, "command":"NWRig.UI.loadConnections(\"Output\")"},width= 100)
connectInputButton = window.button({'key':'connectInputButton','label':'Input Module','parent':connectForm, "command":"NWRig.UI.loadConnections(\"Input\")"},width= 100)
window.connectPopupMenus(connectInputButton, connectOutputButton)
connectInputScroll = window.layout({'key':'connectInputScroll','type':'scrollLayout','parent':connectForm},width= 250, height= 250)
connectOutputScroll = window.layout({'key':'connectOutputScroll','type':'scrollLayout','parent':connectForm},width= 250, height= 250)

connectParentButton = window.button({'key':'connectParentButton','parent':connectForm, 'label':'parent'},width= 100)
connectConnectButton = window.button({'key':'connectConnectButton','parent':connectForm, 'label':'connect'},width= 100)

# Edit form layout
attachForm = [(connectInputText, "top", 5),
              (connectInputText, "left", 5),
              (connectInputButton, "left", 5),
              (connectOutputText, "left",5),
              (connectInputScroll, "top",5),
              (connectOutputText, "top", 5),
              (connectConnectButton,"left", 5)]
attachNone = [(connectInputText, "right"),
              (connectInputText, "bottom"),
              (connectInputButton, "right"),
              (connectInputButton, "bottom"),
              (connectInputScroll, "right"),
              (connectInputScroll, "bottom")]
attachControl =  [(connectInputButton, "top", 10,connectInputText ),
                  (connectInputScroll,"top", 10,connectInputButton),
                  (connectOutputText,"left", 150,connectInputButton),
                  (connectOutputButton,"top", 10,connectOutputText),
                  (connectOutputButton,"left", 150,connectInputButton),
                  (connectOutputScroll,"top", 10,connectOutputButton),
                  (connectOutputScroll,"left", 10,connectInputScroll),
                  (connectParentButton,"top", 10,connectInputScroll),
                  (connectParentButton,"left", 10,connectConnectButton),
                  (connectConnectButton,"top", 10,connectOutputScroll)]
                  
window.editElement("connectForm", af= attachForm, an= attachNone, ac= attachControl )
