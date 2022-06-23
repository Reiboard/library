#picker_advanced_skeleton

armLeft = [ 'FKElbow_L', 'FKWrist_L', 'FKThumbFinger1_L', 'FKCup_L', 'FKThumbFinger2_L', 'FKThumbFinger3_L', 'FKIndexFinger1_L', 'FKIndexFinger2_L', 'FKIndexFinger3_L', 'FKMiddleFinger1_L', 'FKMiddleFinger2_L', 'FKMiddleFinger3_L', 'FKRingFinger1_L', 
'FKRingFinger2_L', 'FKRingFinger2_L', 'FKPinkyFinger1_L', 'FKPinkyFinger2_L', 'FKPinkyFinger3_L', 'Fingers_L', 'IKArm_L', 'PoleArm_L', 'FKShoulder_L']

handLeft = [ 'FKThumbFinger1_L', 'FKCup_L', 'FKThumbFinger2_L', 'FKThumbFinger3_L', 'FKIndexFinger1_L', 'FKIndexFinger2_L', 'FKIndexFinger3_L', 'FKMiddleFinger1_L', 'FKMiddleFinger2_L', 'FKMiddleFinger3_L', 'FKRingFinger1_L', 
'FKRingFinger2_L', 'FKRingFinger2_L', 'FKPinkyFinger1_L', 'FKPinkyFinger2_L', 'FKPinkyFinger3_L', 'Fingers_L', 'FKWrist_L']

amrRight = ['FKElbow_R', 'FKWrist_R', 'FKThumbFinger1_R', 'FKCup_R', 'FKThumbFinger2_R', 'FKThumbFinger3_R', 'FKIndexFinger1_R', 'FKIndexFinger2_R', 'FKIndexFinger3_R', 'FKMiddleFinger1_R', 'FKMiddleFinger2_R', 'FKMiddleFinger3_R', 'FKRingFinger1_R', 
'FKRingFinger2_R', 'FKRingFinger2_R', 'FKPinkyFinger1_R', 'FKPinkyFinger2_R', 'FKPinkyFinger3_R', 'Fingers_R', 'IKArm_R', 'PoleArm_R', 'FKShoulder_R']

handRight = [ 'FKWrist_R', 'FKThumbFinger1_R', 'FKCup_R', 'FKThumbFinger2_R', 'FKThumbFinger3_R', 'FKIndexFinger1_R', 'FKIndexFinger2_R', 'FKIndexFinger3_R', 'FKMiddleFinger1_R', 'FKMiddleFinger2_R', 'FKMiddleFinger3_R', 'FKRingFinger1_R', 
'FKRingFinger2_R', 'FKRingFinger2_R', 'FKPinkyFinger1_R', 'FKPinkyFinger2_R', 'FKPinkyFinger3_R', 'Fingers_R']

IK_FK = [ 'FKIKLeg_R', 'FKIKLeg_L', 'FKIKSpine_M', 'FKIKArm_L', 'FKIKArm_R', 'HipSwinger_M']

legLeft = [ 'PoleLeg_L', 'IKLeg_L', 'RollHeel_L', 'RollToes_L', 'IKToes_L', 'RollToesEnd_L', 'FKKnee_L', 'FKAnkle_L', 'FKToes_L', 'FKHip_L' ]

legRight = [ 'PoleLeg_R', 'IKLeg_R', 'RollHeel_R', 'RollToes_R', 'IKToes_R', 'RollToesEnd_R', 'FKKnee_R', 'FKAnkle_R', 'FKToes_R', 'FKHip_R' ]

head = ['FKNeck_M', 'FKJaw_M', 'FKEye_L', 'FKEye_R', 'FKHead_M', 'AimEye_M', 'AimEye_R', 'AimEye_L']

general = [ 'FKScapula_R', 'FKScapula_L', 'FKChest_M', 'FKSpine1_M', 'FKRoot_M', 'RootX_M', 'IKSpine1_M', 'IKhybridSpine1_M', 'IKSpine2_M', 'IKhybridSpine2_M', 'IKSpine3_M', 'IKhybridSpine3_M', 'Main']+ head + legRight + legLeft + IK_FK + handRight + amrRight + handLeft + armLeft

def buttonArmLeft(z):
    cmds.select(armLeft)

def buttonHandLeft(z):
    cmds.select(handLeft)

def buttonAmrRight(z):
    cmds.select(amrRight)

def buttonHandRight(z):
    cmds.select(handRight)

def buttonIK_FK(z):
    cmds.select(IK_FK)

def buttonLegLeft(z):
    cmds.select(legLeft)

def buttonLegRight(z):
    cmds.select(legRight)

def buttonHead(z):
    cmds.select(head)

def buttonGeneral(z):
    cmds.select(general)

cmds.window( width=300 )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='armLeft', command=buttonArmLeft)
cmds.button( label='handLeft', command=buttonHandLeft)
cmds.button( label='amrRight', command=buttonAmrRight)
cmds.button( label='handRight', command=buttonHandRight)
cmds.button( label='IK_FK', command=buttonIK_FK)
cmds.button( label='legLeft', command=buttonLegLeft)
cmds.button( label='legRight', command=buttonLegRight)
cmds.button( label='head', command=buttonHead)
cmds.button( label='general', command=buttonGeneral)

cmds.showWindow()

