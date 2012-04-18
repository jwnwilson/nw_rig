"Requires that Module class is sourced"

class NWSpineJoints(Module):
        'Creates a joint chain can be used for spine'             
        @startPrePost
        def start(self,**kwargs):
                'Creates a joint chain can be used for spine'
                
                #create module top group
                rootGrp = cmds.group( n = (self.name + "Start_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True )
                
                # create starters
                
        @buildPrePost
        def build(self,**kwargs):
                pass
                # check for module container
                
                #cmds.ikHandle()

                #self.buildComplete()
                
