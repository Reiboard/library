mesh = cmds.xform(i,q=1,ws=1,rp=1)
vertex = cmds.xform( i, query=True, translation=True, worldSpace=True )
