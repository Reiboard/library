import maya.cmds as mc


g = cmds.ls(sl = True)

vertexList = []

for vertex in mc.ls(sl=1, fl=1):
    u = vertex
    vertexList.append(u)
    
cmds.select(cl = True)

for i in vertexList:
    Position = cmds.xform( i, query=True, translation=True, worldSpace=True )
    print(Position)
    cmds.joint( p=(Position[0], Position[1], Position[2]) )
    listJoint = cmds.ls(sl = True)
    for i in listJoint:
        cmds.group(i, a = True, n = 'parentConstraint_' + i + '_grp')
        cmds.rename(i, i + '_jnt')
        Px = cmds.getAttr( i  + '_jnt.tx')
        Py = cmds.getAttr( i  + '_jnt.ty')
        Pz = cmds.getAttr( i  + '_jnt.tz')
        Rx = cmds.getAttr( i  + '_jnt.rx')
        Ry = cmds.getAttr( i  + '_jnt.ry')
        Rz = cmds.getAttr( i  + '_jnt.rz')
        #print(Px, Py, Pz, Rx, Ry, Rz)
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i + '_ctl') 
        cmds.group(a = True, n = 'orige_' + i + '_grp')
        cmds.move(Px, Py, Pz)
        cmds.rotate(Rx, Ry, Rz)
        cmds.parentConstraint(i + '_ctl', 'parentConstraint_' + i + '_grp')
        cmds.orientConstraint(i + '_ctl', i + '_jnt')    
    cmds.select(cl = True)
    
