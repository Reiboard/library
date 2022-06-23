import maya.cmds as cmds

def driver(z):
    selectDrive = []
    select1 = cmds.ls(sl=True)
    selectDrive.append(select1)
    cmds.select(clear=True)


def x(*args):
    driver = selectDrive[0][0] + '.rx'
    list = cmds.ls(sl=1)
    for i in list:
        cmds.setDrivenKeyframe(i+'.t', currentDriver = driver)
        cmds.setDrivenKeyframe(i+'.r', currentDriver = driver)
        
def y(*args):
    driver = selectDrive[0][0] + '.ry'
    list = cmds.ls(sl=1)
    for i in list:
        cmds.setDrivenKeyframe(i+'.t', currentDriver = driver)
        cmds.setDrivenKeyframe(i+'.r', currentDriver = driver)
        
def z(*args):
    driver = selectDrive[0][0] + '.rz'
    list = cmds.ls(sl=1)
    for i in list:
        cmds.setDrivenKeyframe(i+'.t', currentDriver = driver)
        cmds.setDrivenKeyframe(i+'.r', currentDriver = driver)




cmds.window( width=300 )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='selectDriver', command=driver)
cmds.button( label='x', command=x)
cmds.button( label='y', command=y)
cmds.button( label='z', command=x)
cmds.showWindow()
