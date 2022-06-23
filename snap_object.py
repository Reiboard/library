#snap_object


obj1 = cmds.ls(sl = True)[0] 
obj2 = cmds.ls(sl = True)[1] 

cmds.parentConstraint(obj1, obj2)
cmds.delete(obj2, cn = True)