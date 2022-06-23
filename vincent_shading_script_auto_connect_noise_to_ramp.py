import maya.cmds as cmds

ramp = []
RedshiftMaxonNoise = []

cmds.shadingNode('ramp', asTexture = True)

g = cmds.ls(sl = True)
ramp.append(g)

cmds.shadingNode('RedshiftMaxonNoise', asTexture = True)

u = cmds.ls(sl = True)
RedshiftMaxonNoise.append(u)

cmds.connectAttr(RedshiftMaxonNoise[0][0] + '.outColorR', ramp[0][0] + '.vCoord', f = True)


