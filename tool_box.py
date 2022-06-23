#boite_a_outil

import maya.cmds as cmds
import maya.mel as mel
import maya.cmds as mc

listObjects = cmds.ls(sl=True)
numberListObject = len(listObjects)


def buildCircleAndOrigeOnJoint(*args):
    g = cmds.ls(sl = True)
    for i in g:
        cmds.group(i, a = True, n = 'parentConstraint_' + i + '_grp')
        cmds.rename(i, i + '_jnt')
        Px = cmds.getAttr( i  + '_jnt.tx')
        Py = cmds.getAttr( i  + '_jnt.ty')
        Pz = cmds.getAttr( i  + '_jnt.tz')
        Rx = cmds.getAttr( i  + '_jnt.rx')
        Ry = cmds.getAttr( i  + '_jnt.ry')
        Rz = cmds.getAttr( i  + '_jnt.rz')
        #print(Px, Py, Pz, Rx, Ry, Rz)
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i + '_ctl') 
        cmds.group(a = True, n = 'orige_' + i + '_grp')
        cmds.move(Px, Py, Pz)
        cmds.rotate(Rx, Ry, Rz)
        cmds.parentConstraint(i + '_ctl', 'parentConstraint_' + i + '_grp')
        cmds.orientConstraint(i + '_ctl', i + '_jnt')


def buildCircleAndOrigeOnVertex(*args):
    g = cmds.ls(sl = True)    
    vertexList = []    
    for vertex in mc.ls(sl=1, fl=1):
        u = vertex
        vertexList.append(u)        
    cmds.select(cl = True)    
    for i in vertexList:
        Position = cmds.xform( i, query=True, translation=True, worldSpace=True )
        print(Position)
        cmds.joint( p=(Position[0], Position[1], Position[2]) )
        listJoint = cmds.ls(sl = True)
        for i in listJoint:
            cmds.group(i, a = True, n = 'parentConstraint_' + i + '_grp')
            cmds.rename(i, i + '_jnt')
            Px = cmds.getAttr( i  + '_jnt.tx')
            Py = cmds.getAttr( i  + '_jnt.ty')
            Pz = cmds.getAttr( i  + '_jnt.tz')
            Rx = cmds.getAttr( i  + '_jnt.rx')
            Ry = cmds.getAttr( i  + '_jnt.ry')
            Rz = cmds.getAttr( i  + '_jnt.rz')
            #print(Px, Py, Pz, Rx, Ry, Rz)
            cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i + '_ctl') 
            cmds.group(a = True, n = 'orige_' + i + '_grp')
            cmds.move(Px, Py, Pz)
            cmds.rotate(Rx, Ry, Rz)
            cmds.parentConstraint(i + '_ctl', 'parentConstraint_' + i + '_grp')
            cmds.orientConstraint(i + '_ctl', i + '_jnt')    
        cmds.select(cl = True)
    




def buildChainJoint(*args):
    cmds.joint( p=(0, 0, 0), n = 'finguer_01_jnt' )
    cmds.joint( p=(0, 5, 0), n = 'finguer_02_jnt' )
    cmds.joint( p=(0, 10, 0), n = 'finguer_03_jnt' )
    cmds.joint( p=(0, 15, 0), n = 'finguer_04_jnt' )
    
    
    g = cmds.ls('*jnt')
    for i in g:
        u = cmds.xform(i,q=1,ws=1,rp=1)
        px = u[0]
        py = u[1]
        pz = u[2]
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i.replace('jnt', 'ctl') ) 
        z = cmds.ls(sl = True)
        for u in z:
            cmds.group(a = True, n = 'orige_' + u.replace('ctl', 'grp'))
            e = cmds.ls(sl = True)
            for r in e:
                cmds.move(px, py, pz)
                cmds.orientConstraint(u, i)
    
    cmds.parentConstraint('finguer_01_ctl', 'orige_finguer_02_grp', mo = True)
    cmds.parentConstraint('finguer_02_ctl', 'orige_finguer_03_grp', mo = True)
    cmds.parentConstraint('finguer_03_ctl', 'orige_finguer_04_grp', mo = True)
    
def buildFoldingSetDrivenKey(*args):   
    allConstrolerSelect = cmds.ls(sl = True)
    for i in allConstrolerSelect:
        cmds.group(i, a = True, n = 'setDrivenKey_' + i.replace('ctl', 'grp'))
    
    
    cmds.addAttr(allConstrolerSelect[0], ln = 'folding', at = 'long', min = 0, max = 10, dv = 0)
    cmds.setAttr(allConstrolerSelect[0]+'.folding', k=True)
    
    
    
    setDrivenKeyGroup = cmds.ls('setDrivenKey_*_grp')
    for z in setDrivenKeyGroup:
        cmds.setAttr(allConstrolerSelect[0] + '.folding', 0)
        cmds.setDrivenKeyframe(z + '.r', currentDriver = allConstrolerSelect[0] + '.folding')
        cmds.setAttr(allConstrolerSelect[0] + '.folding', 10)
        cmds.rotate('90deg', 0, 0, z)
        cmds.setDrivenKeyframe(z + '.r', currentDriver = allConstrolerSelect[0] + '.folding')
    
    

def buildIK_FK(*args):
    jointSelected = cmds.ls(sl = True)
    
    jointBase = []
    for i in jointSelected:
        jointBase.append(i)
    #position_joint_start
    joint1 = cmds.select(jointBase[0])
    joint1P = cmds.xform(joint1,q=1,ws=1,rp=1)
    joint1Px = joint1P[0]
    joint1Py = joint1P[1]
    joint1Pz = joint1P[2]
    joint2 = cmds.select(jointBase[1])
    joint2P = cmds.xform(joint2,q=1,ws=1,rp=1)
    joint2Px = joint2P[0]
    joint2Py = joint2P[1]
    joint2Pz = joint2P[2]
    joint3 = cmds.select(jointBase[2])
    joint3P = cmds.xform(joint3,q=1,ws=1,rp=1)
    joint3Px = joint3P[0]
    joint3Py = joint3P[1]
    joint3Pz = joint3P[2]
    
    #nameBase
    nameBase = []
    for i in jointBase:
        u = i.replace('_jnt', '')
        nameBase.append(u)
    
    #create_IK_FK_chain
    for i in jointBase:
        cmds.select(i)
        position = cmds.xform(i,q=1,ws=1,rp=1)
        px = position[0]
        py = position[1]
        pz = position[2]
        cmds.select(cl = True)
        cmds.joint( p=(px, py, pz), n = 'IK_' + i )
        cmds.select(cl = True)
        cmds.joint( p=(px, py, pz), n = 'FK_' + i )
    
    #constrainte_orient
    IK_FK = ['IK_', 'FK_']
    
    for i in IK_FK:
        cmds.parent(i + jointBase[1], i + jointBase[0])
        cmds.parent(i + jointBase[2], i + jointBase[1])
        for z in jointBase:
            cmds.orientConstraint(i+z, z)
    
    
    #create_IK_handle+circle
    cmds.ikHandle( sj='IK_'+ jointBase[0] , ee='IK_'+ jointBase[2], ap = True, w=.5, n= 'IK_handle')
    positionHandle = cmds.xform('IK_handle',q=1,ws=1,rp=1)
    handlePx = position[0]
    handlePy = position[1]
    handlePz = position[2]
    cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = 'IK_handle_controler_ctl' ) 
    cmds.group('IK_handle_controler_ctl', a = True, n = 'orige_IK_handle_controler_grp')
    cmds.move(handlePx, handlePy, handlePz, 'orige_IK_handle_controler_grp')
    cmds.parent('IK_handle', 'IK_handle_controler_ctl')
    
    
    #controler_FK_and_contraint
    listFK = cmds.ls('FK_*_jnt')
    for i in listFK:
        cmds.circle( nr=(0, 1, 0), c=(0, 0, 0), n = i.replace('jnt', 'ctl') )
        g = cmds.ls(sl = True)
        for z in g:
            cmds.group(z, a = True, n = 'orige_' + z.replace('ctl', 'grp'))
    
    
    listOrigeFK = cmds.ls('orige_FK*_grp')
    cmds.move(joint1Px, joint1Py, joint1Pz, listOrigeFK[0])
    cmds.move(joint2Px, joint2Py, joint2Pz, listOrigeFK[1])
    cmds.move(joint3Px, joint3Py, joint3Pz, listOrigeFK[2])
    
    #constraint_joint_FK
    for i in nameBase:
        cmds.parentConstraint('FK_' + i + '_ctl', 'FK_' + i + '_jnt')
    
    listCircleFK = cmds.ls('FK_*_ctl')
    cmds.parentConstraint(listCircleFK[0], listOrigeFK[1], mo = True)
    cmds.parentConstraint(listCircleFK[1], listOrigeFK[2], mo = True)
    
    #add_attribut_switch_IK_FK
    cmds.addAttr(listCircleFK[0], ln = 'IK_FK', at = 'long', min = 0, max = 1, dv = 0)
    cmds.setAttr(listCircleFK[0]+'.IK_FK', k=True)
    
    #set_driven_key
    listOrientConstraint = cmds.ls('*orientConstraint1')
    
    cmds.setAttr('FK_' + nameBase[0] + '_ctl.IK_FK',0)
    
    for i in jointBase:
        cmds.setAttr(i + '_orientConstraint1.IK_' + i +'W0', 1)
        cmds.setAttr(i + '_orientConstraint1.FK_' + i +'W1', 0)
        cmds.setDrivenKeyframe(i + '_orientConstraint1.IK_' + i +'W0', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')
        cmds.setDrivenKeyframe(i + '_orientConstraint1.FK_' + i +'W1', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')
    
    cmds.setAttr('FK_' + nameBase[0] + '_ctl.IK_FK',1)
    
    for i in jointBase:
        cmds.setAttr(i + '_orientConstraint1.IK_' + i +'W0', 0)
        cmds.setAttr(i + '_orientConstraint1.FK_' + i +'W1', 1)
        cmds.setDrivenKeyframe(i + '_orientConstraint1.IK_' + i +'W0', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')
        cmds.setDrivenKeyframe(i + '_orientConstraint1.FK_' + i +'W1', currentDriver = 'FK_' + nameBase[0] + '_ctl.IK_FK')
    


def hideGroup(z):
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

def renameGroup(z):
    nameGroupe = cmds.ls(sl = True)[0]
    listOfChild = cmds.listRelatives(nameGroupe, ad=True, type="transform")
    list = cmds.select(listOfChild)
    childSelected = cmds.ls(sl = True)
    
    
    for z in childSelected:
        cmds.rename(z , nameGroupe+"_01")
        
    cmds.rename(nameGroupe, nameGroupe + '_grp')
        
    ########################################################################################
    '''
    cmds.select(nameGroupe)
    cmds.select(list)
    '''
    
    listObjects = cmds.ls(sl=True)
    
    for i in listObjects:
    	try:
    		currentShape = cmds.listRelatives(i)
    		currentType = cmds.objectType(currentShape)
    		print(currentType)
    	
    	except:
    		currentType = cmds.objectType(i)	
    	
    	if currentType == "mesh":
    		if not i.endswith("_msh"):
    			cmds.rename(i , i + "_msh")
    		
    
    	if currentType == "nurbsCurve":
    		if not i.endswith("crv"):
    			cmds.rename(i , i + "_crv")	
    
    	if currentType == "joint":
    		if not i.endswith("jnt"):
    			cmds.rename(i , i + "_jnt")	
    	
    	if currentType == "transform":
    		if not i.endswith("_grp"):
    			cmds.rename(i , i + "_grp")
    			
def renameSuffixe(z):
    listObjects = cmds.ls(sl=True)
    
    for i in listObjects:
    	try:
    		currentShape = cmds.listRelatives(i)
    		currentType = cmds.objectType(currentShape)
    		print(currentType)
    	
    	except:
    		currentType = cmds.objectType(i)	
    	
    	if currentType == "mesh":
    		if not i.endswith("_msh"):
    			cmds.rename(i , i + "_msh")
    		
    
    	if currentType == "nurbsCurve":
    		if not i.endswith("crv"):
    			cmds.rename(i , i + "_crv")	
    
    	if currentType == "joint":
    		if not i.endswith("jnt"):
    			cmds.rename(i , i + "_jnt")	
    	
    	if currentType == "transform":
    		if not i.endswith("_grp"):
    			cmds.rename(i , i + "_grp")
    			
def setDrivenKeyGroup(z):
    selectObject = cmds.ls(sl = True)

    for i in selectObject:
        cmds.group(i, n = 'setDrivenkey_' + i. replace('ctl', 'grp'))
        
        
def snapGroupObjs(z):
    objGroup = cmds.ls(sl = True)

    obj1 = cmds.ls(sl = True)[-1] 
    
    
    objGroup[:-1]
    
    obj2 = cmds.ls(sl = True)[1] 
    
    for i in objGroup[:-1]:
        cmds.parentConstraint(obj1, i)
        cmds.delete(i, cn = True)
    
def snapObject(z):
    obj1 = cmds.ls(sl = True)[0] 
    obj2 = cmds.ls(sl = True)[1]     
    cmds.parentConstraint(obj1, obj2)
    cmds.delete(obj2, cn = True)
    
    
    
    
def snapCurveToVertex(z):
    vertex = cmds.ls(sl = True)[0]
    slobject = cmds.ls(sl = True)[1]        
    cmds.xform(slobject,t=cmds.pointPosition( vertex, local=True),ws=True)
    
def snapOrige(z):
    obj1 = cmds.ls(sl = True)[0] 
    obj2 = cmds.ls(sl = True)[1] 
    
    cmds.parentConstraint(obj1, obj2)
    cmds.delete(obj2, cn = True)
    cmds.rename(obj2, 'orige_' + obj1. replace("_jnt", "_grp"))
    
    listSelected = cmds.ls(sl = True)
    slectedObj1 = cmds.ls(sl = True)[0] 
    slectedObj2 = cmds.ls(sl = True)[1] 
    cmds.select(cl = True)
    cmds.select(slectedObj2)
    
    
    
    nameGroupe = cmds.ls(sl = True)[0]
    listOfChild = cmds.listRelatives(nameGroupe, ad=True, type="transform")
    list = cmds.select(listOfChild)
    childSelected = cmds.ls(sl = True)
    
    
    
    for z in childSelected:
        cmds.rename(z , slectedObj1. replace("_jnt", "_ctl"))
    
    
    
    
    slObject = cmds.ls(sl = True)
    
    cmds.parent(slObject[0]. replace('ctl', '') + 'jnt', slObject[0])
    
def resetAttr(z):
    listSelect = cmds.ls(sl=True)

    for obj in listSelect:
        cmds.xform(obj, t =( 0,0,0), ro = (0,0,0))
    
cmds.window( width=300, t = 'Tool_Box' )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='hide_Group', command=hideGroup)
cmds.button( label='rename_Group', command=renameGroup)
cmds.button( label='set_Driven_Key_Group', command=setDrivenKeyGroup)
cmds.button( label='rename_Suffixe', command=renameSuffixe)
cmds.button( label='snap_Group_Objs', command=snapGroupObjs)
cmds.button( label='snap_Object', command=snapObject)
cmds.button( label='snap_Curve_To_Vertex', command=snapCurveToVertex)
cmds.button( label='snap_Orige', command=snapOrige)
cmds.button( label='reset_Attr', command=resetAttr)
cmds.button( label='build_IK_FK', command=buildIK_FK)
cmds.button( label='build_chain_joint', command=buildChainJoint)
cmds.button( label='build_folding_set_driven_key', command=buildFoldingSetDrivenKey)
cmds.button( label='build_Circle_And_Orige_On_group_Joint', command=buildCircleAndOrigeOnJoint)
cmds.button( label='build_Circle_And_Orige_On_group_Vertex', command=buildCircleAndOrigeOnVertex)

cmds.showWindow()
