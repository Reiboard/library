#reset_Attr

import maya.cmds as cmds

listSelect = cmds.ls(sl=True)

for obj in listSelect:
    cmds.xform(obj, t =( 0,0,0), ro = (0,0,0))