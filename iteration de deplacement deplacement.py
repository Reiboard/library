#iteration de deplacement deplacement

listObjects2 = cmds.ls(sl=True)

positionZ = 0

for i in listObjects2:
		cmds.select(i)
		cmds.move(0, 0, positionZ)
		positionZ = positionZ + 2
		 