"Requires that Module class is sourced"

try:
        import NWModule
except ImportError:
        print "Error"

class NWSpineJoints(NWModule.NWModule):
        """
            Creates a joint chain can be used for spine
        """
        def initialize(self):
            # store variables in container
            util.storeString(self.container, "type", "NWSpineJoints")
        @NWModule.startPrePost
        def start(self,**kwargs):
                'Creates a joint chain can be used for spine'
                
                #create module top group
                rootGrp = cmds.group( n = (self.name + "Start_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True )
                
                # create starters
                
        @NWModule.buildPrePost
        def build(self,**kwargs):
                pass
                # check for module container
                
                #cmds.ikHandle()

                #self.buildComplete()
                
