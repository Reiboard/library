#bout_de_script


fullGroup = cmds.ls(sl = True)



pppList = []
fffList = []

for obj in fullGroup:
    if 'fff_' in obj:
        fffList.append(obj)
    if 'ppp_' in obj:
        pppList.append(obj)
      
      
      
clusterppp = cmds.ls(pppList, typ = 'skinCluster')
clusterfff = cmds.ls(fffList, typ = 'skinCluster')

  
cmds.select('ppp_box_01_msh')
cmds.select('fff_box_01_msh', tgl = True)


mel.eval('copySkinWeights -ss skinCluster2 -ds skinCluster1 -mirrorMode YZ -surfaceAssociation closestPoint -influenceAssociation closestJoint;')

cmds.copySkinWeights( noMirror = True, sa = 'closestPoint', ia = 'closestJoint')

##############################################################################################################################################################################

obj1 = cmds.getAttr('pCube1.translate')[0][0]
obj2 = cmds.getAttr('pCube2.translate')[0][0]

result = obj1 - obj2

difference = mag(obj1 - obj2)

cmds.getAttr('pCube3.translate')

cmds.xform('pCube3', ws = True)

cmds.move('nurbsCircle1', 

##############################################################################################################################################################################


IKhandleGroupStart = ['IK_L_leg_jnt', 'IK_R_leg_jnt', 'IK_L_shoulder_jnt', 'IK_R_shoulder_jnt']
IKhandleGroupEnd = ['IK_L_ankle_jnt', 'IK_R_ankle_jnt', 'IK_L_wrist_jnt', 'IK_R_wrist_jnt']



for i in IKhandleGroupStart:
    for z in IKhandleGroupEnd:        
        print(i, z)
 
##############################################################################################################################################################################
import random

g = cmds.ls(sl = True)



for i in g:
    randomX = random.uniform(-3, 3)
    randomY = random.uniform(-3, 3)
    randomZ = random.uniform(-3, 3)
    cmds.move( randomX, randomY, randomZ, r = True,  os = True, wd = True)


##############################################################################################################################################################################

g = cmds.ls(sl=True)
for i in g:
    
    
g = cmds.ls(sl=True)

u = g[0].split('.e')

u[0]
z = u[1].replace('[','').replace(']','')

cmds.polySelect(u[0], edgeLoop=z)