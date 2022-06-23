#snap_orige_to_joint_and_rename


obj1 = cmds.ls(sl = True)[0] 
obj2 = cmds.ls(sl = True)[1] 

cmds.parentConstraint(obj1, obj2)
cmds.delete(obj2, cn = True)
cmds.rename(obj2, 'orige_' + obj1. replace("_jnt", "_grp"))

listSelected = cmds.ls(sl = True)
slectedObj1 = cmds.ls(sl = True)[0] 
slectedObj2 = cmds.ls(sl = True)[1] 
cmds.select(cl = True)
cmds.select(slectedObj2)



nameGroupe = cmds.ls(sl = True)[0]
listOfChild = cmds.listRelatives(nameGroupe, ad=True, type="transform")
list = cmds.select(listOfChild)
childSelected = cmds.ls(sl = True)



for z in childSelected:
    cmds.rename(z , slectedObj1. replace("_jnt", "_ctl"))




slObject = cmds.ls(sl = True)

cmds.parent(slObject[0]. replace('ctl', '') + 'jnt', slObject[0])