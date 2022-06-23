#rename_groupe


import maya.cmds as cmds



nameGroupe = cmds.ls(sl = True)[0]
listOfChild = cmds.listRelatives(nameGroupe, ad=True, type="transform")
list = cmds.select(listOfChild)
childSelected = cmds.ls(sl = True)


for z in childSelected:
    cmds.rename(z , nameGroupe+"_01")
    
cmds.rename(nameGroupe, nameGroupe + '_grp')
    
########################################################################################
'''
cmds.select(nameGroupe)
cmds.select(list)
'''

listObjects = cmds.ls(sl=True)

for i in listObjects:
	try:
		currentShape = cmds.listRelatives(i)
		currentType = cmds.objectType(currentShape)
		print(currentType)
	
	except:
		currentType = cmds.objectType(i)	
	
	if currentType == "mesh":
		if not i.endswith("_msh"):
			cmds.rename(i , i + "_msh")
		

	if currentType == "nurbsCurve":
		if not i.endswith("crv"):
			cmds.rename(i , i + "_crv")	

	if currentType == "joint":
		if not i.endswith("jnt"):
			cmds.rename(i , i + "_jnt")	
	
	if currentType == "transform":
		if not i.endswith("_grp"):
			cmds.rename(i , i + "_grp")
			

