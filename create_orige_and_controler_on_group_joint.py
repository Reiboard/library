#create_orige+controler_on_group_joint

import maya.cmds as cmds

g = cmds.ls(sl = True)
baseGroup = []



for i in g:
    cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i.replace('jnt', 'ctl')) 
    cmds.group(a = True, n = 'orige_' + i.replace('jnt', 'grp'))
    
for i in g:
    u = i.replace('_jnt', '')
    baseGroup.append(u)

for z in baseGroup:
    cmds.parentConstraint(z + '_jnt', 'orige_' + z + '_grp')
    cmds.delete('orige_' + z + '_grp', cn = True)
    cmds.parent(z + '_jnt', z + '_ctl')
    