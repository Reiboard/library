#rename_part_of_name_in_list


list =cmds.ls(sl=1)

for i in list:
    cmds.rename(i, i.replace("ecl_rig_def_rework__test__V22_HS:", ""))
