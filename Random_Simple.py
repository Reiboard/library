#Random_Simple

import maya.cmds as mc
import random

Ctl = cmds.ls(sl=True)
for i in Ctl:
    random_number = random.randint(1, 18)
    cmds.setAttr (i+".Hide", random_number)