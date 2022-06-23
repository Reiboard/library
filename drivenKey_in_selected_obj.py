#drivenKey_in_selected_obj

import maya.cmds as cmds

driver = 'FKNeck_M.rz'

list = cmds.ls(sl=1)

for i in list:
    cmds.setDrivenKeyframe(i+'.t', currentDriver = driver)
    cmds.setDrivenKeyframe(i+'.r', currentDriver = driver)
