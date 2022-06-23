import random
import maya.cmds as cmds



def random_key(*args):
    Ctl = cmds.ls(sl=True)
    positionKey = cmds.currentTime( query=True )
    positionKeyN = positionKey + 2
    
    for i in Ctl:
        cmds.move(random.uniform(-1, 1),random.uniform(-1, 1),random.uniform(-1, 1))
        cmds.setKeyframe(i + '.t')
    
    cmds.currentTime(positionKeyN)







cmds.window( width=300 )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='camera_shake', command=random_key)
cmds.showWindow()
