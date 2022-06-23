
#all_controler
def generalBody(*args):
    all_Ctl_List = cmds.ls('*:*_ctl')
    cmds.select(all_Ctl_List)

#controler_eyes
def eyes(*args):
    all_eyes_ctl = cmds.ls('*:*eye*ctl')
    cmds.select(all_eyes_ctl)

#controler_not_body
def body_more(*args):
    add_ctl = cmds.ls('*:*antenne*ctl', '*:*cordon*ctl' )
    cmds.select(add_ctl)

#arm_L
def arm_L(*args):
    arm_L = cmds.ls('*:*L*scapula*ctl','*:*L*shoulder*ctl', '*:*L*elbow*ctl', '*:*L*wrist*ctl', '*:*L*Finger*ctl', '*:*L*cup*ctl', '*:*handle*arm*L*ctl' )
    cmds.select(arm_L)

#arm_R
def arm_R(*args):
    arm_R = cmds.ls('*:*R*scapula*ctl','*:*R*shoulder*ctl', '*:*R*elbow*ctl', '*:*R*wrist*ctl', '*:*R*Finger*ctl', '*:*R*cup*ctl', '*:*handle*arm*R*ctl' )
    cmds.select(arm_R)

#leg_L
def pickLeg_L(*args):
    leg_L = cmds.ls('*:*L*leg*ctl','*:*L*knee*ctl', '*:*L*ankle*ctl', '*:*L*Toes*ctl', '*:*L*toes*ctl', '*:*L*Toe*ctl', '*:*L*heel*ctl', '*:*handle*leg*L*ctl' )
    cmds.select(leg_L)

#leg_R
def pickLeg_R(*args):
    leg_R = cmds.ls('*:*R*leg*ctl','*:*R*knee*ctl', '*:*R*ankle*ctl', '*:*R*Toes*ctl', '*:*R*toes*ctl', '*:*R*Toe*ctl', '*:*R*heel*ctl', '*:*handle*leg*R*ctl' )
    cmds.select(leg_L)

#IK/FK
def keyIK_FK(*args):
    cmds.setKeyframe('*:*ctl', at = '.IK_FK')

#switch_IK/FK_armL
def switch_IK_FK_armL(*args):
    x = cmds.getAttr('*:*L*shoulder*ctl.IK_FK')
    if x == 0:
        cmds.setAttr('*:*L*shoulder*ctl.IK_FK', 1)
    if x == 1:
        cmds.setAttr('*:*L*shoulder*ctl.IK_FK', 0)

#switch_IK/FK_armR
def switch_IK_FK_armR(*args):
    x = cmds.getAttr('*:*R*shoulder*ctl.IK_FK')
    if x == 0:
        cmds.setAttr('*:*R*shoulder*ctl.IK_FK', 1)
    if x == 1:
        cmds.setAttr('*:*R*shoulder*ctl.IK_FK', 0)
        
#switch_IK/FK_legR
def switch_IK_FK_legR(*args):
    x = cmds.getAttr('*:*R*leg*ctl.IK_FK')
    if x == 0:
        cmds.setAttr('*:*R*leg*ctl.IK_FK', 1)
    if x == 1:
        cmds.setAttr('*:*R*leg*ctl.IK_FK', 0)        
        
#switch_IK/FK_legL
def switch_IK_FK_legR(*args):
    x = cmds.getAttr('*:*L*leg*ctl.IK_FK')
    if x == 0:
        cmds.setAttr('*:*L*leg*ctl.IK_FK', 1)
    if x == 1:
        cmds.setAttr('*:*L*leg*ctl.IK_FK', 0)  
        
        


cmds.window( width=300 )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='generalBody', command=generalBody)
cmds.button( label='eyes', command=eyes)
cmds.button( label='body_more', command=body_more)
cmds.button( label='arm_L', command=arm_L)
cmds.button( label='arm_R', command=arm_R)
cmds.button( label='Leg_L', command=pickLeg_L)
cmds.button( label='Leg_R', command=pickLeg_R)
cmds.button( label='key_IK_FK', command=keyIK_FK)
cmds.button( label='switch_IK_FK_armL', command=switch_IK_FK_armL)
cmds.button( label='switch_IK_FK_armR', command=switch_IK_FK_armR)
cmds.button( label='switch_IK_FK_legL', command=switch_IK_FK_armL)
cmds.button( label='switch_IK_FK_legR', command=switch_IK_FK_armR)


cmds.showWindow()






























