#Authors _ God Bennett and GPT for this particular file
#Note, I found out that for this to work I edited face it/rigging/pivot_manager.py line 314, by adding dpi param to func call. Blend 2.91/3.7 combo does not allow 2 params, needs dpi a 3rd param. I used 92 for dpi related to 1920x1080 screns.

import bpy

def show_objects_in_armature(armature_obj):
    # Get all objects in the scene
    all_objects = bpy.context.scene.objects
    
    # Iterate through all objects
    for obj in all_objects:
        # Check if object is parented to the armature
        if obj.parent and obj.parent.type == 'ARMATURE' and obj.parent.data == armature_obj.data:
            print("Object:", obj.name)

# Name of the armature object
armature_name = "FaceitRig"

# Get the armature object
armature_obj = bpy.data.objects.get(armature_name)

if armature_obj and armature_obj.type == 'ARMATURE':
    show_objects_in_armature(armature_obj)
else:
    print("Armature object not found or is not of type ARMATURE.")