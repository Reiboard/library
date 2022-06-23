#snap_lot_of_obj


objGroup = cmds.ls(sl = True)

obj1 = cmds.ls(sl = True)[-1] 


objGroup[:-1]

obj2 = cmds.ls(sl = True)[1] 

for i in objGroup[:-1]:
    cmds.parentConstraint(obj1, i)
    cmds.delete(i, cn = True)
