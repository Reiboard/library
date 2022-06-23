#change_color_curve

import maya.cmds as cmds


colorCurve = cmds.ls('*ctl')
for i in colorCurve:
    cmds.setAttr(i + ".overrideEnabled", 1)
    cmds.setAttr(i + ".overrideColor", 17)