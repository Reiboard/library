jointSelected = cmds.ls(sl = True)

jointBase = []
for i in jointSelected:
    jointBase.append(i)
#position_joint_start
joint1 = cmds.select(jointBase[0])
joint1P = cmds.xform(joint1,q=1,ws=1,rp=1)
joint1Px = joint1P[0]
joint1Py = joint1P[1]
joint1Pz = joint1P[2]
joint2 = cmds.select(jointBase[1])
joint2P = cmds.xform(joint2,q=1,ws=1,rp=1)
joint2Px = joint2P[0]
joint2Py = joint2P[1]
joint2Pz = joint2P[2]
joint3 = cmds.select(jointBase[2])
joint3P = cmds.xform(joint3,q=1,ws=1,rp=1)
joint3Px = joint3P[0]
joint3Py = joint3P[1]
joint3Pz = joint3P[2]

#nameBase
nameBase = []
for i in jointBase:
    u = i.replace('_jnt', '')
    nameBase.append(u)

#create_IK_FK_chain
for i in jointBase:
    cmds.select(i)
    position = cmds.xform(i,q=1,ws=1,rp=1)
    px = position[0]
    py = position[1]
    pz = position[2]
    cmds.select(cl = True)
    cmds.joint( p=(px, py, pz), n = 'IK_' + i )
    cmds.select(cl = True)
    cmds.joint( p=(px, py, pz), n = 'FK_' + i )

#constrainte_orient
IK_FK = ['IK_', 'FK_']

for i in IK_FK:
    cmds.parent(i + jointBase[1], i + jointBase[0])
    cmds.parent(i + jointBase[2], i + jointBase[1])
    for z in jointBase:
        cmds.orientConstraint(i+z, z)


#create_IK_handle+circle
cmds.ikHandle( sj='IK_'+ jointBase[0] , ee='IK_'+ jointBase[2], ap = True, w=.5, n= 'IK_handle')
positionHandle = cmds.xform('IK_handle',q=1,ws=1,rp=1)
handlePx = position[0]
handlePy = position[1]
handlePz = position[2]
cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = 'IK_handle_controler_ctl' ) 
cmds.group('IK_handle_controler_ctl', a = True, n = 'orige_IK_handle_controler_grp')
cmds.move(handlePx, handlePy, handlePz, 'orige_IK_handle_controler_grp')
cmds.parent('IK_handle', 'IK_handle_controler_ctl')


#controler_FK_and_contraint
listFK = cmds.ls('FK_*_jnt')
for i in listFK:
    cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i.replace('jnt', 'ctl') )
    g = cmds.ls(sl = True)
    for z in g:
        cmds.group(z, a = True, n = 'orige_' + z.replace('ctl', 'grp'))


listOrigeFK = cmds.ls('orige_FK*_grp')
cmds.move(joint1Px, joint1Py, joint1Pz, listOrigeFK[0])
cmds.move(joint2Px, joint2Py, joint2Pz, listOrigeFK[1])
cmds.move(joint3Px, joint3Py, joint3Pz, listOrigeFK[2])

#constraint_joint_FK
for i in nameBase:
    cmds.parentConstraint('FK_' + i + '_ctl', 'FK_' + i + '_jnt')

listCircleFK = cmds.ls('FK_*_ctl')
cmds.parentConstraint(listCircleFK[0], listOrigeFK[1], mo = True)
cmds.parentConstraint(listCircleFK[1], listOrigeFK[2], mo = True)

#add_attribut_switch_IK_FK
cmds.addAttr(listCircleFK[0], ln = 'IK_FK', at = 'long', min = 0, max = 1, dv = 0)
cmds.setAttr(listCircleFK[0]+'.IK_FK', k=True)

#set_driven_key
listOrientConstraint = cmds.ls('*orientConstraint1')

cmds.setAttr('FK_' + nameBase[0] + '_ctl.IK_FK',0)

for i in jointBase:
    cmds.setAttr(i + '_orientConstraint1.IK_' + i +'W0', 1)
    cmds.setAttr(i + '_orientConstraint1.FK_' + i +'W1', 0)
    cmds.setDrivenKeyframe(i + '_orientConstraint1.IK_' + i +'W0', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')
    cmds.setDrivenKeyframe(i + '_orientConstraint1.FK_' + i +'W1', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')

cmds.setAttr('FK_' + nameBase[0] + '_ctl.IK_FK',1)

for i in jointBase:
    cmds.setAttr(i + '_orientConstraint1.IK_' + i +'W0', 0)
    cmds.setAttr(i + '_orientConstraint1.FK_' + i +'W1', 1)
    cmds.setDrivenKeyframe(i + '_orientConstraint1.IK_' + i +'W0', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')
    cmds.setDrivenKeyframe(i + '_orientConstraint1.FK_' + i +'W1', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')

