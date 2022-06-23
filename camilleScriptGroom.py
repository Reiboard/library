groupSelect = cmds.ls(sl = True)

value = 4

for i in groupSelect:
    z = cmds.listRelatives(i, s=True)[0]
    cmds.setAttr(i + '|' + z + '.innerRadius', value)
    cmds.setAttr(i + '|' + z + '.outerRadius', value)
    