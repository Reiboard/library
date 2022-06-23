import maya.cmds as cmds


def RedshiftMaxonNoiseSettingPerso(*args):
    ramp = []
    RedshiftMaxonNoise = []
    
    cmds.shadingNode('ramp', asTexture = True)
    
    g = cmds.ls(sl = True)
    ramp.append(g)
    
    cmds.shadingNode('RedshiftMaxonNoise', asTexture = True)
    
    u = cmds.ls(sl = True)
    RedshiftMaxonNoise.append(u)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.noise_type', 8)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.octaves', 8)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.coord_source',3)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.coord_scale_global',7000)
    
    
    cmds.connectAttr(RedshiftMaxonNoise[0][0] + '.outColorR', ramp[0][0] + '.vCoord', f = True)

def RedshiftMaxonNoise(*args):
    ramp = []
    RedshiftMaxonNoise = []
    
    cmds.shadingNode('ramp', asTexture = True)
    
    g = cmds.ls(sl = True)
    ramp.append(g)
    
    cmds.shadingNode('RedshiftMaxonNoise', asTexture = True)
    
    u = cmds.ls(sl = True)
    RedshiftMaxonNoise.append(u)
    
    cmds.connectAttr(RedshiftMaxonNoise[0][0] + '.outColorR', ramp[0][0] + '.vCoord', f = True)

def RedshiftMaxonNoiseMoreBump(*args):
    ramp = []
    RedshiftMaxonNoise = []
    bump = []
    
    cmds.shadingNode('ramp', asTexture = True)
    
    g = cmds.ls(sl = True)
    ramp.append(g)
    
    cmds.shadingNode('RedshiftMaxonNoise', asTexture = True)
    
    u = cmds.ls(sl = True)
    RedshiftMaxonNoise.append(u)
    
    cmds.shadingNode('RedshiftBumpMap', asTexture = True)
    
    z = cmds.ls(sl = True)
    bump.append(z)
    
    
    cmds.connectAttr(ramp[0][0] + '.outColor', bump[0][0] + '.input', f = True)
    
    cmds.connectAttr(RedshiftMaxonNoise[0][0] + '.outColorR', ramp[0][0] + '.vCoord', f = True)
    

def RedshiftMaxonNoiseMoreBumpSettingPerso(*args):
    ramp = []
    RedshiftMaxonNoise = []
    bump = []
    
    cmds.shadingNode('ramp', asTexture = True)
    
    g = cmds.ls(sl = True)
    ramp.append(g)
    
    cmds.shadingNode('RedshiftMaxonNoise', asTexture = True)
    
    u = cmds.ls(sl = True)
    RedshiftMaxonNoise.append(u)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.noise_type', 8)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.octaves', 8)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.coord_source',3)
    cmds.setAttr(RedshiftMaxonNoise[0][0] + '.coord_scale_global',7000)
    
    cmds.shadingNode('RedshiftBumpMap', asTexture = True)
    
    z = cmds.ls(sl = True)
    bump.append(z)
    
    
    cmds.connectAttr(ramp[0][0] + '.outColor', bump[0][0] + '.input', f = True)
    
    cmds.connectAttr(RedshiftMaxonNoise[0][0] + '.outColorR', ramp[0][0] + '.vCoord', f = True)



cmds.window( width=300, t = 'shading_tool_box_pour_mon_petit_Vincent' )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Redshift_Maxon_Noise(original)', command=RedshiftMaxonNoise)
cmds.button( label='Redshift_Maxon_Noise_Setting_Perso', command=RedshiftMaxonNoiseSettingPerso)
cmds.button( label='Redshift_Maxon_Noise+Bump(original)', command=RedshiftMaxonNoiseMoreBump)
cmds.button( label='Redshift_Maxon_Noise+Bump_Setting_Perso', command=RedshiftMaxonNoiseMoreBumpSettingPerso)


cmds.showWindow()

