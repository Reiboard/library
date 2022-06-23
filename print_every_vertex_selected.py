#print_every_vertex_selected

import maya.cmds as mc

for vertex in mc.ls(sl=1, fl=1):
    print vertex