# Initialize window
window = NWWindowRigUI.NWWindowRigUI({"name":self.name, "windowWidth":400, "windowHeight":400, "title":"NWWindow", "NWRig":self})
# Root layout
window.layout({'key':'rootLayout','label':'root'})
# Create tabs
methodTab = window.layout({'key':'methodTab','label':'tabs','type':'tabLayout'})
# Create pannel
frame1 = window.layout({'key':'createFrame','parent':methodTab,'label':'create','type':'frameLayout'})
window.text({'key':'createText1','label':'create menu'})
window.button({'key':'createNewButton','label':'New'})
window.button({'key':'createSaveButton','label':'Save'})
window.button({'key':'createLoadButton','label':'Load'})
# Start pannel
startTab = window.layout({'key':'startFrame','parent':methodTab,'label':'starter','type':'frameLayout'})
window.text({'key':'startText1','label':'Load starter'})
scroll1 = window.layout({'key':'startScroll','type':'scrollLayout','parent':startTab, 'label':'starters'})
window.loadStartIcons()
window.text({'key':'startText2','label':'Module name','parent':startTab})
window.textField({'key':'startTextField','label':'starterName','parent':startTab})
# Build pannel
buildTab = window.layout({'key':'buildFrame','parent':methodTab,'label':'build','type':'frameLayout'})
window.text({'key':'buildText','label':'build menu'})
buildScroll1 = window.layout({'key':'buildScroll','type':'scrollLayout','parent':buildTab, 'label':'buildScroll'})
#buildIconScrollList = window.loadBuilds({'parent':buildScroll1})
#buildAttributes = window.loadBuildAttributes({'parent':buildScroll1})
window.button({'key':'buildRefreshButton','parent':buildTab, 'label':'refresh',"command":"NWRig.UI.loadModules({})"})
window.button({'key':'buildBuildButton','parent':buildTab, 'label':'build',"command":"NWRig.UI.buildModules({})"})
#connectTab = window.layout({'parent':createTab,'label':'connect','type':'frameLayout'})