"Requires that Module class is sourced"

class NWSpineJoints(Module):
        'Creates a joint chain can be used for spine'             
        @blueprintPrePost
        def blueprint(self,**kwargs):
                'Creates a joint chain can be used for spine'
                
                #create module top group
                rootGrp = cmds.group( n = (self.name + "Blueprint_GRP"), em = True )
                jointGrp = cmds.group( n = (self.name + "Joint_GRP"), em = True )
                
                # create blueprinters
                
        @rigPrePost
        def rig(self,**kwargs):
                pass
                # check for module container
                
                #cmds.ikHandle()

                #self.rigComplete()
                
