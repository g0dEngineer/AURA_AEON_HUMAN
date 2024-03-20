#Authors _ God Bennett and GPT for this particular file
#Note, I found out that for this to work I edited face it/rigging/pivot_manager.py line 314, by adding dpi param to func call. Blend 2.91/3.7 combo does not allow 2 params, needs dpi a 3rd param. I used 92 for dpi related to 1920x1080 screns.

import bpy

# Name of the armature object
armature_name = "FaceitRig"

# Get the armature object
armature_obj = bpy.data.objects.get(armature_name)

if armature_obj and armature_obj.type == 'ARMATURE':
    # Access the armature data
    armature = armature_obj.data
    
    # Print names of all bones
    for bone in armature.bones:
        print("Bone:", bone.name)
else:
    print("Armature object not found or is not of type ARMATURE.")
