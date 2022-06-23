#setDrivenkey_group


import maya.cmds as cmds

selectObject = cmds.ls(sl = True)

for i in selectObject:
    cmds.group(i, n = 'setDrivenkey_' + i. replace('ctl', 'grp'))
