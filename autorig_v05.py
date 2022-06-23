#BASE

#joints creation 
def createSkeleton():
	cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = 'root_ctl' ) 
	cmds.joint( p=(0, 5, 0), n = 'hip_jnt' )
	cmds.joint( p=(-1, 4.5, 0), n= 'R_leg_jnt' )
	cmds.joint( p=(-1, 2.5, 0.7), n = 'R_knee_jnt' )
	cmds.joint( p=(-1, 0.5, 0), n = 'R_ankle_jnt' )
	cmds.joint( p=(-1, 0.25, 0.5), n = 'R_toes_jnt' )
	cmds.joint( p=(-1, 0, 1), n = 'R_toesEnd_jnt' )
	cmds.select( clear = True )
	cmds.select( 'R_ankle_jnt' )
	cmds.joint( p=(-1, 0, -0.5), n = 'R_heel_jnt' )
	cmds.select( clear = True )
	cmds.select( 'R_toes_jnt' )
	cmds.joint( p=(-1.25, 0, 0.5), n = 'R_pinkyToe_jnt' )
	cmds.select( clear = True )
	cmds.select( 'R_toes_jnt' )
	cmds.joint( p=(-0.75, 0, 0.5), n = 'R_bigToe_jnt' )
	cmds.select( clear = True )
	cmds.select( 'hip_jnt' )
	cmds.joint( p=(0, 6, 0), n = 'spine1_jnt' )
	cmds.joint( p=(0, 7, 0), n = 'spine2_jnt' )
	cmds.joint( p=(-0.5, 9, 0), n = 'R_scapula_jnt' )
	cmds.joint( p=(-1.5, 9, 0), n = 'R_shoulder_jnt' )
	cmds.joint( p=(-3.5, 9, -0.7), n = 'R_elbow_jnt' )
	cmds.joint( p=(-5.5, 9, 0), n = 'R_wrist_jnt' )
	cmds.joint( p=(-5.75, 9, -0.25), n = 'R_cup_jnt' )
	cmds.joint( p=(-6, 9, -0.5), n = 'R_pinkyFinger1_jnt' )
	cmds.joint( p=(-6.25, 9, -0.5), n = 'R_pinkyFinger2_jnt' )
	cmds.joint( p=(-6.5, 9, -0.5), n = 'R_pinkyFinger3_jnt' )
	cmds.joint( p=(-6.75, 9, -0.5), n = 'R_pinkyFinger4_jnt' )
	cmds.select( clear = True )
	cmds.select( 'R_cup_jnt' )
	cmds.joint( p=(-6, 9, -0.25), n = 'R_ringFinger1_jnt' )
	cmds.joint( p=(-6.25, 9, -0.25), n = 'R_ringFinger2_jnt' )
	cmds.joint( p=(-6.5, 9, -0.25), n = 'R_ringFinger3_jnt' )
	cmds.joint( p=(-6.75, 9, -0.25), n = 'R_ringFinger4_jnt' )
	cmds.select( clear = True )
	cmds.select( 'R_wrist_jnt' )
	cmds.joint( p=(-6, 9, 0), n = 'R_middleFinger1_jnt' )
	cmds.joint( p=(-6.25, 9, 0), n = 'R_middleFinger2_jnt' )
	cmds.joint( p=(-6.5, 9, 0), n = 'R_middleFinger3_jnt' )
	cmds.joint( p=(-6.75, 9, 0), n = 'R_middleFinger4_jnt' )
	cmds.select( clear = True )
	cmds.select( 'R_wrist_jnt' )
	cmds.joint( p=(-6, 9, 0.25), n = 'R_indexFinger1_jnt' )
	cmds.joint( p=(-6.25, 9, 0.25), n = 'R_indexFinger2_jnt' )
	cmds.joint( p=(-6.5, 9, 0.25), n = 'R_indexFinger3_jnt' )
	cmds.joint( p=(-6.75, 9, 0.25), n = 'R_indexFinger4_jnt' )
	cmds.select( clear = True )
	cmds.select( 'R_wrist_jnt' )
	cmds.joint( p=(-5.75, 9, 0.5), n = 'R_thumbFinger1_jnt' )
	cmds.joint( p=(-6, 9, 0.5), n = 'R_thumbFinger2_jnt' )
	cmds.joint( p=(-6.25, 9, 0.5), n = 'R_thumbFinger3_jnt' )
	cmds.joint( p=(-6.5, 9, 0.5), n = 'R_thumbFinger4_jnt' )
	cmds.select( clear = True )
	cmds.select( 'spine2_jnt' )
	cmds.joint( p=(0, 10, 0), n = 'neck_jnt' )
	cmds.joint( p=(0, 11, 0), n = 'head_jnt' )
	cmds.joint( p=(0, 12, 0), n = 'headEnd_jnt' )
	cmds.select( clear = True )
	cmds.select( 'head_jnt' )
	cmds.joint( p=(0, 10.5, 0.5), n = 'jaw_jnt' )
	cmds.joint( p=(0, 10.5, 1), n = 'jawEnd_jnt' )
	cmds.select( clear = True )
	cmds.select( 'head_jnt' )
	cmds.joint( p=(-0.5, 11.5, 0.5), n = 'R_eye_jnt' )
	cmds.joint( p=(-0.5, 11.5, 0.75), n = 'R_eyeEnd_jnt' )

########################################################################################################################################################################################################################################################################################
createSkeleton()

#mirror_joint
mirrorGroup = ['R_leg_jnt', 'R_scapula_jnt', 'R_eye_jnt']

for a in mirrorGroup:
    cmds.mirrorJoint( a, searchReplace=('R_', 'L_'), mb = True)


#add_suffixe_SK
groupJoint = cmds.ls('*_jnt')

for s in groupJoint:
    cmds.rename(s, 'SK_'+s)


#IK_FK_joint
IKgroup = ['SK_R_leg_jnt', 'SK_R_scapula_jnt','SK_L_leg_jnt', 'SK_L_scapula_jnt']

for a in IKgroup:
    cmds.mirrorJoint( a, searchReplace=('SK_', 'IK_'), mb = True)
    cmds.mirrorJoint( a, searchReplace=('SK_', 'FK_'), mb = True)

#delete_part_of_hierarchi
deletedGroupIK_FK = ['IK_R_wrist_jnt', 'IK_L_wrist_jnt', 'FK_R_wrist_jnt', 'FK_L_wrist_jnt', 'IK_R_ankle_jnt', 'IK_L_ankle_jnt', 'FK_R_ankle_jnt', 'FK_L_ankle_jnt']

for i in deletedGroupIK_FK:
    child = cmds.listRelatives(i, c=True)
    cmds.delete(child)



#parenConstraint_group_jnt
selectJnt = cmds.select('*_jnt')
listJnt = cmds.ls(sl = True)

for i in listJnt:
    cmds.group(i, n = 'parentConstraint_'+i.replace('_jnt', '_grp'))



#create_controleur+orige
selectSK = cmds.select('*SK_*_grp')
listSK = cmds.ls(sl = True)

for i in listSK:
    #create_circle
    cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n = i.replace('_grp', '_ctl').replace('parentConstraint_', ''))
    #create_orige
    cmds.group(a = True, n = 'orige_'+i.replace('_jnt', '_grp').replace('parentConstraint_', ''))
    #variable_all_circle_create
    groupCircle = cmds.ls(sl = True)
    for z in groupCircle:
        #select_joint_in_orige
        u = cmds.pickWalk(i, direction = 'down')
        #constraint_parent_to_place_every_circle
        cmds.parentConstraint(u, z)
        #delete_parent_constraint
        cmds.delete(z, cn = True)
        #rotate
        if  'scapula' in z:
            cmds.setAttr(z + '.rz', 90)
        if  'shoulder' in z:
            cmds.setAttr(z + '.rz', 90)
        if  'elbow' in z:
            cmds.setAttr(z + '.rz', 90)
        if  'wrist' in z:
            cmds.setAttr(z + '.rz', 90)
        if  'cup' in z:
            cmds.setAttr(z + '.rz', 90)
        if  'Finger' in z:
            cmds.setAttr(z + '.rz', 90)            


#find_every_name_of_element(joint+ctl)
jointGroup = cmds.ls('SK_*_jnt')
listOfElement = []
for i in jointGroup:
    z = i.replace('_jnt', '')
    listOfElement.append(z)


#parent_controler_to_group_joint
for e in listOfElement:
    cmds.parentConstraint(e+'_ctl', 'parentConstraint_'+ e+'_grp', mo = True, weight = True)
       

   



#create_IK_handle
cmds.ikHandle( sj='IK_L_shoulder_jnt', ee='IK_L_wrist_jnt', ap = True, w=.5, n= 'IK_handle_arm_L')
cmds.ikHandle( sj='IK_R_shoulder_jnt', ee='IK_R_wrist_jnt', ap = True, w=.5, n= 'IK_handle_arm_R')
cmds.ikHandle( sj='IK_L_leg_jnt', ee='IK_L_ankle_jnt', ap = True, w=.5, n= 'IK_handle_leg_L')
cmds.ikHandle( sj='IK_R_leg_jnt', ee='IK_R_ankle_jnt', ap = True, w=.5, n= 'IK_handle_leg_R')

#IK_handle_controler
IKhandleGroup = cmds.ls('IK_handle_*')
for i in IKhandleGroup:
    cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), n = 'controler_'+ i+'_ctl')
    cmds.group(a = True, n = 'orige_controler_' + i+'_grp')
    
    
IKhandleOrigeArmGroup = ['orige_controler_IK_handle_arm_R_grp', 'orige_controler_IK_handle_arm_L_grp']
for i in IKhandleOrigeArmGroup:
    cmds.rotate(0,0,90)

#place_controler_handle
groupParentHandle = ['IK_handle_arm_L', 'IK_handle_arm_R', 'IK_handle_leg_L', 'IK_handle_leg_R' ]
for i in groupParentHandle:
    cmds.parentConstraint(i, 'orige_controler_' + i+'_grp')
    cmds.delete(i, cn = True)
    cmds.parentConstraint('controler_'+ i+'_ctl', i)

#group_motion_handle
groupHandleElement = ['IK_handle_arm_L', 'IK_handle_arm_R', 'IK_handle_leg_L', 'IK_handle_leg_R', 'orige_controler_IK_handle_arm_L_grp', 'orige_controler_IK_handle_arm_R_grp', 'orige_controler_IK_handle_leg_L_grp', 'orige_controler_IK_handle_leg_R_grp']
cmds.select(groupHandleElement)
cmds.group(a = True, n = 'motion_systeme_handleIK_grp')



    
#hierarchi_circle
##contrainte_parent
###finger
fingerGroup = ['L_index', 'L_middle', 'L_pinky', 'L_ring', 'L_thumb', 'R_index', 'R_middle', 'R_pinky', 'R_ring', 'R_thumb']

for i in fingerGroup:
    cmds.parentConstraint('SK_' + i +'Finger1_ctl', 'orige_SK_' + i + 'Finger2_grp', mo = True)
    cmds.parentConstraint('SK_' + i +'Finger2_ctl', 'orige_SK_' + i + 'Finger3_grp', mo = True)
    cmds.parentConstraint('SK_' + i +'Finger3_ctl', 'orige_SK_' + i + 'Finger4_grp', mo = True)
 
  
cupGroup = ['pinky', 'ring']

for i in cupGroup:
    cmds.parentConstraint('SK_L_cup_ctl', 'orige_SK_L_'+i+'Finger1_grp', mo = True)
    cmds.parentConstraint('SK_R_cup_ctl', 'orige_SK_R_'+i+'Finger1_grp', mo = True)

    
wristGroup = ['index', 'middle', 'thumb']
for i in wristGroup:
    cmds.parentConstraint('SK_R_wrist_ctl', 'orige_SK_R_'+i+'Finger1_grp', mo =True)
    cmds.parentConstraint('SK_L_wrist_ctl', 'orige_SK_L_'+i+'Finger1_grp', mo =True)

cmds.parentConstraint('SK_R_wrist_ctl', 'orige_SK_R_cup_grp', mo =True)
cmds.parentConstraint('SK_R_wrist_ctl', 'orige_SK_L_cup_grp', mo =True)

###arm
LR = ['R_', 'L_']
for i in LR:
    cmds.parentConstraint('SK_'+i+'shoulder_ctl', 'orige_SK_'+i+'elbow_grp', mo =True)
    cmds.parentConstraint('SK_'+i+'elbow_ctl', 'orige_SK_'+i+'wrist_grp', mo =True)
    cmds.parentConstraint('SK_'+i+'scapula_ctl', 'orige_SK_'+i+'shoulder_grp', mo =True)

###hip
####toes
toesGroup = ['orige_SK*pinkyToe_grp', 'orige_SK*toesEnd_grp', 'orige_SK*bigToe_grp']
cmds.select(toesGroup)
toesList = cmds.ls(sl = True)
for i in toesList:
    if 'L' in i:
        cmds.parentConstraint('SK_L_toes_ctl', i, mo =True)
    if 'R' in i:
        cmds.parentConstraint('SK_R_toes_ctl', i, mo =True)

####foot
footGroup = ['orige_SK_*_toes_grp', 'orige_SK_*_heel_grp']
cmds.select(footGroup)
footList = cmds.ls(sl = True)
for i in footList:
    if 'L' in i:
        cmds.parentConstraint('SK_L_ankle_ctl', i, mo =True)
    if 'R' in i:
        cmds.parentConstraint('SK_R_ankle_ctl', i, mo =True)

####leg
for i in LR:
    cmds.parentConstraint('SK_'+i+'leg_ctl', 'orige_SK_'+i+'knee_grp', mo =True)
    cmds.parentConstraint('SK_'+i+'knee_ctl', 'orige_SK_'+i+'ankle_grp', mo =True)

###head
cmds.parentConstraint('SK_neck_ctl', 'orige_SK_head_grp', mo =True)
cmds.parentConstraint('SK_jaw_ctl', 'orige_SK_jawEnd_grp', mo =True)
headGroupContraint = ['jaw', 'headEnd']
for i in headGroupContraint:
    cmds.parentConstraint('SK_head_ctl', 'orige_SK_*'+i+'_grp', mo =True)
    for z in LR:
        cmds.parentConstraint('SK_head_ctl', 'orige_SK_'+z+'eye_grp', mo =True)
        cmds.parentConstraint('SK_'+z+'eye_ctl', 'orige_SK_'+z+'eyeEnd_grp', mo =True)

###body
cmds.parentConstraint('SK_hip_ctl', 'orige_SK_spine1_grp', mo =True)
cmds.parentConstraint('SK_spine1_ctl', 'orige_SK_spine2_grp', mo =True)
for i in LR:
    cmds.parentConstraint('SK_spine2_ctl', 'orige_SK_'+i+'scapula_grp', mo =True)



##group_hierarchie
###fingerGroup
for i in fingerGroup:
    cmds.group('orige_SK_' + i +'Finger*_grp', a = True, n = 'motionSysteme_' + i +'_grp')
    
handL = cmds.ls('motionSysteme_L*_grp') + ['orige_SK_L_wrist_grp', 'orige_SK_L_cup_grp']
handR = cmds.ls('motionSysteme_R*_grp') + ['orige_SK_R_wrist_grp', 'orige_SK_R_cup_grp']
cmds.group(handL, a = True, n = 'motionSysteme_hand_L_grp')
cmds.group(handR, a = True, n = 'motionSysteme_hand_R_grp')

###armGroup
armL = ['orige_SK_L_shoulder_grp', 'orige_SK_L_elbow_grp', 'motionSysteme_hand_L_grp', 'orige_SK_L_scapula_grp']
cmds.group(armL, a = True, n = 'motionSysteme_arm_L_grp')
armR = ['orige_SK_R_shoulder_grp', 'orige_SK_R_elbow_grp', 'motionSysteme_hand_R_grp', 'orige_SK_R_scapula_grp']
cmds.group(armR, a = True, n = 'motionSysteme_arm_R_grp')


###hipGroup
####toes
toesToGroupR = cmds.ls('orige*R*oe*_grp')
cmds.group(toesToGroupR, a = True, n = 'motionSysteme_toes_R_grp')
toesToGroupL = cmds.ls('orige*L*oe*_grp')
cmds.group(toesToGroupL, a = True, n = 'motionSysteme_toes_L_grp')

####foot
ankleGroupR = ['motionSysteme_toes_R_grp', 'orige_SK_R_heel_grp', 'orige_SK_R_ankle_grp']
cmds.group(ankleGroupR, a = True, n = 'motionSysteme_foot_R_grp')
ankleGroupL = ['motionSysteme_toes_L_grp', 'orige_SK_L_heel_grp', 'orige_SK_L_ankle_grp']
cmds.group(ankleGroupL, a = True, n = 'motionSysteme_foot_L_grp')

####leg
legR_group = [ 'orige_SK_R_leg_grp', 'orige_SK_R_knee_grp', 'motionSysteme_foot_R_grp']
cmds.group(legR_group, a = True, n = 'motionSysteme_leg_R_grp')
legL_group = [ 'orige_SK_L_leg_grp', 'orige_SK_L_knee_grp', 'motionSysteme_foot_L_grp']
cmds.group(legL_group, a = True, n = 'motionSysteme_leg_L_grp')

###headGroup
headGroup = ['orige_SK_neck_grp', 'orige_SK_head_grp', 'orige_SK_jaw_grp', 'orige_SK_jawEnd_grp', 'orige_SK_headEnd_grp', 'orige_SK_L_eye_grp', 'orige_SK_R_eye_grp', 'orige_SK_L_eyeEnd_grp', 'orige_SK_R_eyeEnd_grp']
cmds.group(headGroup, a = True, n = 'motionSysteme_head_grp')

###body
bodyGroup = ['orige_SK_hip_grp', 'orige_SK_spine1_grp', 'orige_SK_spine2_grp']
cmds.group(bodyGroup, a = True, n = 'motionSysteme_body_grp')

###motion_systeme_SK
motionSystemeGroup = cmds.ls('motionSysteme*')
cmds.group(motionSystemeGroup, a = True, n = 'motionSysteme_SK_grp')


#contraintOrient
listJointIK_FK = cmds.ls('IK_L_*_jnt')
listbaseIK = []
for i in listJointIK_FK:
    u = i.replace('IK_L_', '').replace('_jnt', '')
    listbaseIK.append(u)

for i in listbaseIK:
    for z in LR:
        #cmds.orientConstraint('IK_'+ z + i +'_jnt', 'SK_'+ z + i +'_jnt')
        #cmds.orientConstraint('FK_'+ z + i +'_jnt', 'SK_'+ z + i +'_jnt')
        print('IK_'+ z + i +'_jnt', 'SK_'+ z + i +'_jnt')
        print('FK_'+ z + i +'_jnt', 'SK_'+ z + i +'_jnt')

#delete_contraint_SK_in_FK_circle
for i in listbaseIK:
    for z in LR:
        cmds.delete('parentConstraint_SK_'+z+i+'_grp_parentConstraint1')
        

#rename_SK_
listFKcontroler = []
for i in listbaseIK:
    listFKcontroler
    
    
for z in listbaseIK:
    cmds.rename('orige_SK_R_'+z+'_grp' , 'orige_FK_R_'+z+'_grp')
    cmds.rename('orige_SK_L_'+z+'_grp' , 'orige_FK_L_'+z+'_grp')
    cmds.rename('SK_R_'+z+'_ctl' , 'FK_R_'+z+'_ctl')
    cmds.rename('SK_L_'+z+'_ctl' , 'FK_L_'+z+'_ctl')
        

#delete_constraint_wrist
cmds.delete('FK_*wrist_ctl', cn= True)
cmds.delete('FK_*ankle_ctl', cn= True)

#inverse_L_R
IKlistjoint = cmds.ls('IK_*_jnt')
IKlistgroup = cmds.ls('parentConstraint_IK_*_grp')
FKlistjoint = cmds.ls('FK_*_jnt')
FKlistgroup = cmds.ls('parentConstraint_FK_*_grp')
listIK_FKreverseLR = IKlistjoint + IKlistgroup + FKlistjoint + FKlistgroup
for i in listIK_FKreverseLR:
    if 'R' in i:
        cmds.rename(i, i.replace('R', 'L')+'1')
    if 'L' in i:
        cmds.rename(i, i.replace('L', 'R')+'1')

for i in listIK_FKreverseLR:
    cmds.rename(i+'1', i.replace('1', ''))

#new_parent_constraint
for i in listbaseIK:
    cmds.parentConstraint('FK_R_'+i+'_ctl', 'parentConstraint_FK_R_'+i+'_grp', mo = True)
    cmds.parentConstraint('FK_L_'+i+'_ctl', 'parentConstraint_FK_L_'+i+'_grp', mo = True)

#reverse_R_L_IK_handle
IKhandleList = cmds.ls('IK_handle*')
IKhandleGroup = cmds.ls('orige_controler_IK*_grp')
IKcontrolerList = cmds.ls('controler_IK*_ctl')
IKlistAdd = IKhandleList + IKhandleGroup + IKcontrolerList
cmds.select(IKlistAdd)
u = cmds.ls(sl = True)
for i in u:
    if 'R' in i:
        cmds.rename(i, i.replace('R', 'L')+'1')
    if 'L' in i:
        cmds.rename(i, i.replace('L', 'R')+'1')

for i in u:
    cmds.rename(i+'1', i.replace('1', ''))


#constraint_parent_IK_FK_ankle_wrist
wristConstraint = ['cup', 'indexFinger1', 'middleFinger1', 'thumbFinger1']
ankleConstraint = ['heel', 'toes']
for i in wristConstraint:    
    cmds.parentConstraint('FK_R_wrist_ctl', 'orige_SK_R_'+i+'_grp', mo = True)
    cmds.parentConstraint('FK_L_wrist_ctl', 'orige_SK_L_'+i+'_grp', mo = True)
    cmds.parentConstraint('controler_IK_handle_arm_R_ctl', 'orige_SK_R_'+i+'_grp', mo = True)
    cmds.parentConstraint('controler_IK_handle_arm_L_ctl', 'orige_SK_L_'+i+'_grp', mo = True)
for i in ankleConstraint:
    cmds.parentConstraint('FK_L_ankle_ctl', 'orige_SK_L_'+i+'_grp', mo = True)
    cmds.parentConstraint('FK_R_ankle_ctl', 'orige_SK_R_'+i+'_grp', mo = True)
    cmds.parentConstraint('controler_IK_handle_leg_L_ctl', 'orige_SK_L_'+i+'_grp', mo = True)
    cmds.parentConstraint('controler_IK_handle_leg_R_ctl', 'orige_SK_R_'+i+'_grp', mo = True)


#add_attribut
controlerReceveAttr = ['FK_L_shoulder_ctl', 'FK_R_shoulder_ctl', 'FK_R_leg_ctl', 'FK_L_leg_ctl']
for i in controlerReceveAttr:
    cmds.addAttr(i, ln = 'IK_FK', at = 'long', min = 0, max = 1, dv = 0)
    cmds.setAttr(i+'.IK_FK', k=True)

#setDriven_key_IK_FK
elementTop = ['scapula', 'shoulder', 'elbow', 'wrist']
elementBot = ['leg', 'knee', 'ankle']


for i in elementTop:
    for z in LR:
        cmds.parentConstraint('parentConstraint_IK_' + z + i +'_grp', 'parentConstraint_SK_' + z + i +'_grp', mo = True)
        cmds.parentConstraint('parentConstraint_FK_' + z + i +'_grp', 'parentConstraint_SK_' + z + i +'_grp', mo = True)
for i in elementBot:
    for z in LR:
        cmds.parentConstraint('parentConstraint_IK_' + z + i +'_grp', 'parentConstraint_SK_' + z + i +'_grp', mo = True)
        cmds.parentConstraint('parentConstraint_FK_' + z + i +'_grp', 'parentConstraint_SK_' + z + i +'_grp', mo = True)



for z in LR:
    cmds.setAttr('FK_'+ z +'shoulder_ctl.IK_FK', 1)
    for i in elementTop:
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', 0)
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', 1)
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', currentDriver = 'FK_'+ z +'shoulder_ctl.IK_FK')
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', currentDriver = 'FK_'+ z +'shoulder_ctl.IK_FK')
    cmds.setAttr('FK_'+ z +'shoulder_ctl.IK_FK', 0)
    for i in elementTop:
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', 1)
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', 0)
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', currentDriver = 'FK_'+ z +'shoulder_ctl.IK_FK')
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', currentDriver = 'FK_'+ z +'shoulder_ctl.IK_FK')


for z in LR:
    cmds.setAttr('FK_'+ z +'leg_ctl.IK_FK', 1)
    for i in elementBot:
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', 0)
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', 1)
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', currentDriver = 'FK_'+ z +'leg_ctl.IK_FK')
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', currentDriver = 'FK_'+ z +'leg_ctl.IK_FK')
    cmds.setAttr('FK_'+ z +'leg_ctl.IK_FK', 0)
    for i in elementBot:
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', 1)
        cmds.setAttr('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', 0)
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_IK_'+ z + i +'_grpW0', currentDriver = 'FK_'+ z +'leg_ctl.IK_FK')
        cmds.setDrivenKeyframe('parentConstraint_SK_'+ z + i +'_grp_parentConstraint1.parentConstraint_FK_'+ z + i +'_grpW1', currentDriver = 'FK_'+ z +'leg_ctl.IK_FK')



fingerDeleteConstraint = ['cup', 'middleFinger1', 'indexFinger1', 'thumbFinger1']
toesDeleteConstraint = ['toes', 'heel']
deleteConstraint = fingerDeleteConstraint + toesDeleteConstraint

for i in deleteConstraint:
    for z in LR:
        cmds.delete('orige_SK_'+ z + i +'_grp', cn = True)

for i in toesDeleteConstraint:
    for z in LR:
        cmds.parentConstraint('parentConstraint_SK_'+ z + 'ankle_grp', 'orige_SK_'+ z + i +'_grp', mo = True)
        
for i in fingerDeleteConstraint:
    for z in LR:
        cmds.parentConstraint('parentConstraint_SK_'+ z + 'wrist_grp', 'orige_SK_'+ z + i +'_grp', mo = True)

#*#


#hide_handle
listHandle = cmds.ls('IK_handle*')
for i in listHandle:
    try:
        cmds.setAttr(i + '.visibility', 0)
    except:
        listHandle.remove(i)
        
        
       
    
    

#visibility_IK_FK_setDrivenKey

FK_R_top = ['orige_FK_R_elbow_grp', 'orige_FK_R_wrist_grp', 'parentConstraint_FK_R_shoulder_grp', 'parentConstraint_FK_R_elbow_grp', 'parentConstraint_FK_R_wrist_grp']
cmds.select(FK_R_top)
FK_L_top = ['orige_FK_L_elbow_grp', 'orige_FK_L_wrist_grp', 'parentConstraint_FK_L_shoulder_grp', 'parentConstraint_FK_L_elbow_grp', 'parentConstraint_FK_L_wrist_grp']
cmds.select(FK_L_top)
FK_R_bot = ['orige_FK_R_knee_grp', 'orige_FK_R_ankle_grp', 'parentConstraint_FK_R_leg_grp', 'parentConstraint_FK_R_knee_grp', 'parentConstraint_FK_R_ankle_grp']
cmds.select(FK_R_bot)
FK_L_bot = ['orige_FK_L_knee_grp', 'orige_FK_L_ankle_grp', 'parentConstraint_FK_L_leg_grp', 'parentConstraint_FK_L_knee_grp', 'parentConstraint_FK_L_ankle_grp']
cmds.select(FK_R_bot)

IK_R_top = ['orige_controler_IK_handle_arm_R_grp', 'parentConstraint_IK_R_shoulder_grp', 'parentConstraint_IK_R_elbow_grp', 'parentConstraint_IK_R_wrist_grp']
cmds.select(IK_R_top)
IK_L_top = ['orige_controler_IK_handle_arm_L_grp', 'parentConstraint_IK_L_shoulder_grp', 'parentConstraint_IK_L_elbow_grp', 'parentConstraint_IK_L_wrist_grp']
cmds.select(IK_L_top)
IK_L_bot = ['orige_controler_IK_handle_leg_L_grp', 'parentConstraint_IK_L_leg_grp', 'parentConstraint_IK_L_knee_grp', 'parentConstraint_IK_L_ankle_grp']
cmds.select(IK_L_bot)
IK_R_bot = ['orige_controler_IK_handle_leg_R_grp', 'parentConstraint_IK_R_leg_grp', 'parentConstraint_IK_R_knee_grp', 'parentConstraint_IK_R_ankle_grp']
cmds.select(IK_R_bot)



IK_top = IK_R_top + IK_L_top
cmds.select(IK_top)
IK_bot = IK_R_bot + IK_L_bot 
cmds.select(IK_bot)

FK_top = FK_R_top + FK_L_top
cmds.select(FK_top)
FK_bot = FK_R_bot + FK_L_bot
cmds.select(FK_bot)

#top_R
groupFK_R = ['FK_R_elbow_ctl', 'FK_R_wrist_ctl']

cmds.setAttr('FK_R_shoulder_ctl.IK_FK', 1)
for i in groupFK_R:
    cmds.setAttr(i+'.visibility', 1)   
    cmds.setAttr('controler_IK_handle_arm_R_ctl.visibility',0)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_R_shoulder_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_arm_R_ctl.visibility', currentDriver = 'FK_R_shoulder_ctl.IK_FK')

cmds.setAttr('FK_R_shoulder_ctl.IK_FK', 0)
for i in groupFK_R:
    cmds.setAttr(i+'.visibility', 0)
    cmds.setAttr('controler_IK_handle_arm_R_ctl.visibility',1)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_R_shoulder_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_arm_R_ctl.visibility', currentDriver = 'FK_R_shoulder_ctl.IK_FK')
    

#top_L
groupFK_L = ['FK_L_elbow_ctl', 'FK_L_wrist_ctl']

cmds.setAttr('FK_L_shoulder_ctl.IK_FK', 1)
for i in groupFK_L:
    cmds.setAttr(i+'.visibility', 1)   
    cmds.setAttr('controler_IK_handle_arm_L_ctl.visibility',0)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_L_shoulder_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_arm_L_ctl.visibility', currentDriver = 'FK_L_shoulder_ctl.IK_FK')

cmds.setAttr('FK_L_shoulder_ctl.IK_FK', 0)
for i in groupFK_L:
    cmds.setAttr(i+'.visibility', 0)
    cmds.setAttr('controler_IK_handle_arm_L_ctl.visibility',1)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_L_shoulder_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_arm_L_ctl.visibility', currentDriver = 'FK_L_shoulder_ctl.IK_FK')




#bot_R
groupFK_R = ['FK_R_ankle_ctl', 'FK_R_knee_ctl']

cmds.setAttr('FK_R_leg_ctl.IK_FK', 1)
for i in groupFK_R:
    cmds.setAttr(i+'.visibility', 1)   
    cmds.setAttr('controler_IK_handle_leg_R_ctl.visibility',0)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_R_leg_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_leg_R_ctl.visibility', currentDriver = 'FK_R_leg_ctl.IK_FK')

cmds.setAttr('FK_R_leg_ctl.IK_FK', 0)
for i in groupFK_R:
    cmds.setAttr(i+'.visibility', 0)
    cmds.setAttr('controler_IK_handle_leg_R_ctl.visibility',1)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_R_leg_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_leg_R_ctl.visibility', currentDriver = 'FK_R_leg_ctl.IK_FK')

#bot_L
groupFK_L = ['FK_L_ankle_ctl', 'FK_L_knee_ctl']

cmds.setAttr('FK_L_leg_ctl.IK_FK', 1)
for i in groupFK_L:
    cmds.setAttr(i+'.visibility', 1)   
    cmds.setAttr('controler_IK_handle_leg_L_ctl.visibility',0)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_L_leg_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_leg_L_ctl.visibility', currentDriver = 'FK_L_leg_ctl.IK_FK')

cmds.setAttr('FK_L_leg_ctl.IK_FK', 0)
for i in groupFK_L:
    cmds.setAttr(i+'.visibility', 0)
    cmds.setAttr('controler_IK_handle_leg_L_ctl.visibility',1)
    cmds.setDrivenKeyframe(i+'.visibility', currentDriver = 'FK_L_leg_ctl.IK_FK')
    cmds.setDrivenKeyframe('controler_IK_handle_leg_L_ctl.visibility', currentDriver = 'FK_L_leg_ctl.IK_FK')
#color_curve
colorCurve = cmds.ls('*ctl')
for i in colorCurve:
    cmds.setAttr(i + ".overrideEnabled", 1)
    cmds.setAttr(i + ".overrideColor", 17)

#group_finale
group_finale = ['root_ctl', 'motion_systeme_handleIK_grp', 'motionSysteme_SK_grp']
cmds.group(group_finale, a = True, n = 'rig_grp')
