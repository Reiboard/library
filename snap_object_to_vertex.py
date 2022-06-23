#snap_object_to_vertex


import maya.cmds as cmds

vertex = cmds.ls(sl = True)[0]

slobject = cmds.ls(sl = True)[1]


cmds.xform(slobject,t=cmds.pointPosition( vertex, local=True),ws=True)
