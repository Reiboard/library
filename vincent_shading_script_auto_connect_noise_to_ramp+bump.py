import maya.cmds as cmds

ramp = []
RedshiftMaxonNoise = []
bump = []

cmds.shadingNode('ramp', asTexture = True)

g = cmds.ls(sl = True)
ramp.append(g)

cmds.shadingNode('RedshiftMaxonNoise', asTexture = True)

u = cmds.ls(sl = True)
RedshiftMaxonNoise.append(u)

cmds.shadingNode('RedshiftBumpMap', asTexture = True)

z = cmds.ls(sl = True)
bump.append(z)


cmds.connectAttr(ramp[0][0] + '.outColor', bump[0][0] + '.input', f = True)

cmds.connectAttr(RedshiftMaxonNoise[0][0] + '.outColorR', ramp[0][0] + '.vCoord', f = True)




