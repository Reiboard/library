#export obj

import maya.cmds as cmds

listObjects = cmds.ls(sl=True) #list des objets selectionnes
print(listObjects)

for i in listObjects:
	cmds.file('D:\\group\\objet\\' + i + '.obj', force=1, options='groups=1;ptgroups=1;materials=1;smoothing=1;normals=1', typ='OBJexport', pr=1, es=1)
	
