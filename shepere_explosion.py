import random

for i in range (1, 2000):
    #cmds.joint( p=(random.uniform(-10,10), random.uniform(-10,10), random.uniform(-10,10)) )
    cmds.polyPlane(w = 1, h = 1, sx = 10, sy = 10 , ax =(1,1,1))
    #cmds.move(random.uniform(-10,10),random.uniform(-10,10), random.uniform(-10,10))
    cmds.rotate(random.uniform(0,360), random.uniform(0,360), random.uniform(0,360))
    cmds.select(cl = True)