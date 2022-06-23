
groupCircle = cmds.ls(sl = True)

cmds.selectKey(groupCircle)
cmds.bakeResults( sampleBy = 1, oversamplingRate = 1, preserveOutsideKeys = 1, sparseAnimCurveBake = 0)
cmds.selectKey(groupCircle)
cmds.keyframe(animation = 'keys', option = 'over', relative = True, timeChange = (0 + 100)) 
cmds.currentTime('101')
cmds.setKeyframe(groupCircle)

cmds.currentTime('1')

attr = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz']

for i in groupCircle:
    for z in attr:
        cmds.setAttr(i + z, 0)
        cmds.setKeyframe(i)


