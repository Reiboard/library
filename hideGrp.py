#hideGrp


import maya.cmds as cmds
import maya.mel as mel

#List all selected items
listObjects = cmds.ls(sl=True)

#create circle
cmds.circle( nr=(0, 0, 0), c=(0, 0, 0), n = 'controler_hide_ctl' )
cmds.rotate( '90deg', 0, 0, r=True )
#list all elements
numberListObject = len(listObjects)

#cmds.addAttr(listObjects, ln="basename", dataType="string")

#Create MEL variable from Python to store how many elements
mel.eval('int $objetNNN = python("str(numberListObject)")')

#Add attribute with min/max vlaue
mel.eval('addAttr -ln "Hide" -min 1 -max $objetNNN -dv 1 |controler_hide_ctl;')
mel.eval('setAttr -e-keyable true |controler_hide_ctl.Hide;')

cmds.delete('controler_hide_ctl', constructionHistory = True) 
cmds.makeIdentity('controler_hide_ctl', apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

###################################################################

#List all elements
#listObjects = cmds.ls(sl=True)
cmds.select(listObjects)
#elements to display
controlerNumber = 1


for i in listObjects:
    listObjects = cmds.ls(sl=True)

    #SetDrivenKey current element to display
    cmds.setAttr("controler_hide_ctl.Hide", controlerNumber)

    #Set visibility on current object
    cmds.setAttr(i + '.visibility', 1)
    

    #SetDrivenKey current geometry to display   
    cmds.setDrivenKeyframe( i + '.visibility', currentDriver = 'controler_hide_ctl.Hide')
    
    #remove current item from all elements in the lsit
    listObjects.remove(i)
    
    for currentObject in listObjects:
        
        #set visibility on other geometry  to 0
        cmds.setAttr(currentObject + '.visibility', 0)
        
        #setDrivenKey on aother geometry
        cmds.setDrivenKeyframe(currentObject + '.visibility', currentDriver = "controler_hide_ctl.Hide" )
        
        
    #Move to the next geometry to display
    controlerNumber += 1
