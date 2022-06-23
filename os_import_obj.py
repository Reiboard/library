import os


for root, dirs, files in os.walk("D:\\group\\objet", topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if '.obj' in name:
            cmds.file(os.path.join(root, name) , i = True, type = "OBJ", ignoreVersion = True, mergeNamespacesOnClash = False, namespace = name, options = "mo=1", pr = True, importFrameRate = True, importTimeRange = "override")

    
      

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      