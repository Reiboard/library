#auto_key_setdrivenkey

import maya.cmds as cmds

driver = 'FKNeck_M.rz'

listDrivenKey = ['setDrivenkey_scarf_shest_serie_1_bot_main_grp','setDrivenkey_scarf_shest_serie_2_bot_main_grp','setDrivenkey_scarf_shest_serie_3_bot_main_grp','setDrivenkey_scarf_shest_serie_4_bot_main_grp','setDrivenkey_scarf_shest_serie_5_bot_main_grp', 
'setDrivenkey_scarf_shest_serie_6_bot_main_grp', 'setDrivenkey_scarf_shest_serie_7_bot_main_grp', 'setDrivenkey_scarf_shest_serie_9_bot_main_grp', 'setDrivenkey_scarf_shest_serie_8_bot_main_grp', 'setDrivenkey_scarf_shest_serie_11_bot_main_grp', 
'setDrivenkey_scarf_shest_serie_12_bot_main_grp', 'setDrivenkey_scarf_shest_serie_13_bot_main_grp', 'setDrivenkey_scarf_main_side_top_01_grp', 'setDrivenkey_scarf_shest_serie_3_top_main_grp', 'setDrivenkey_scarf_shest_serie_2_top_main_grp', 
'setDrivenkey_scarf_shest_serie_1_top_main_grp', 'setDrivenkey_scarf_shest_serie_4_top_main_grp', 'setDrivenkey_scarf_shest_serie_5_top_main_grp', 'setDrivenkey_scarf_shest_serie_6_top_main_grp', 'setDrivenkey_scarf_main_side_top_03_grp',
'setDrivenkey_scarf_main_side_top_02_grp', 'setDrivenkey_scarf_shest_serie_7_top_main_grp', 'setDrivenkey_scarf_shest_serie_8_top_main_grp', 'setDrivenkey_scarf_shest_serie_9_top_main_grp', 'setDrivenkey_scarf_main_side_top_04_grp', 'setDrivenkey_scarf_shest_serie_10_top_main_grp', 
'setDrivenkey_scarf_shest_serie_11_top_main_grp', 'setDrivenkey_scarf_shest_serie_12_top_main_grp', 'setDrivenkey_scarf_main_side_top_05_grp', 'setDrivenkey_scarf_shest_serie_15_top_main_grp', 'setDrivenkey_scarf_shest_serie_14_top_main_grp', 
'setDrivenkey_scarf_shest_serie_13_top_main_grp']

cmds.select(listDrivenKey)


for obj in listDrivenKey:
    cmds.select(obj)
    trans = cmds.getAttr(obj+'.t')
    rot = cmds.getAttr(obj+'.r')
    if (trans >0.01) or (trans<0.01):
        cmds.setDrivenKeyframe(obj+'.t', currentDriver = driver)
    if (rot > 0.01) or (rot < 0.01):
        cmds.setDrivenKeyframe(obj+'.r', currentDriver = driver)




