cmds.joint( p=(0, 0, 0), n = 'finguer_01_jnt' )
cmds.joint( p=(0, 5, 0), n = 'finguer_02_jnt' )
cmds.joint( p=(0, 10, 0), n = 'finguer_03_jnt' )
cmds.joint( p=(0, 15, 0), n = 'finguer_04_jnt' )


g = cmds.ls('*jnt')
for i in g:
    u = cmds.xform(i,q=1,ws=1,rp=1)
    px = u[0]
    py = u[1]
    pz = u[2]
    cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i.replace('jnt', 'ctl') ) 
    z = cmds.ls(sl = True)
    for u in z:
        cmds.group(a = True, n = 'orige_' + u.replace('ctl', 'grp'))
        e = cmds.ls(sl = True)
        for r in e:
            cmds.move(px, py, pz)
            cmds.orientConstraint(u, i)

cmds.parentConstraint('finguer_01_ctl', 'orige_finguer_02_grp', mo = True)
cmds.parentConstraint('finguer_02_ctl', 'orige_finguer_03_grp', mo = True)
cmds.parentConstraint('finguer_03_ctl', 'orige_finguer_04_grp', mo = True)


#second_part

allConstrolerSelect = cmds.ls(sl = True)
for i in allConstrolerSelect:
    cmds.group(i, a = True, n = 'setDrivenKey_' + i.replace('ctl', 'grp'))


cmds.addAttr(allConstrolerSelect[0], ln = 'folding', at = 'long', min = 0, max = 10, dv = 0)
cmds.setAttr(allConstrolerSelect[0]+'.folding', k=True)



setDrivenKeyGroup = cmds.ls('setDrivenKey_*_grp')
for z in setDrivenKeyGroup:
    cmds.setAttr(allConstrolerSelect[0] + '.folding', 0)
    cmds.setDrivenKeyframe(z + '.r', currentDriver = allConstrolerSelect[0] + '.folding')
    cmds.setAttr(allConstrolerSelect[0] + '.folding', 10)
    cmds.rotate('90deg', 0, 0, z)
    cmds.setDrivenKeyframe(z + '.r', currentDriver = allConstrolerSelect[0] + '.folding')















