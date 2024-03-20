#Authors _ God Bennett and GPT for this particular file
#Note, I found out that for this to work I edited face it/rigging/pivot_manager.py line 314, by adding dpi param to func call. Blend 2.91/3.7 combo does not allow 2 params, needs dpi a 3rd param. I used 92 for dpi related to 1920x1080 screns.

#Note these rouge bones showed up in pose mode @pose layer position, but not in edit mode. Because they couldn't be deleted, they cause massive warping of aeon human avatar mesh. This script deletes those rouge bones programmatically

#This basically verified the hypothesis that in edit bones the bones exist, but were hidden somehow. In ui, viewport had bones checked, and also, alt+h was toggled to show all hidden. The ui still hid the bones, but this script deleted.

#To check if bones "DEF-teeth.B", "DEF-teeth.T" stil existed, I used show_armature_bones.py script in this same dir.

import bpy

def delete_bones_by_name(armature_obj, bone_names):
    # Switch to Edit Mode
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Access the edit bones
    edit_bones = armature_obj.data.edit_bones
    
    # Iterate through bones
    for bone_name in bone_names:
        # Check if bone exists
        if bone_name in edit_bones:
            # Get the bone object
            bone = edit_bones[bone_name]
            # Remove the bone
            edit_bones.remove(bone)

    # Switch back to Object Mode
    bpy.ops.object.mode_set(mode='OBJECT')



# Name of the armature object
armature_name = "FaceitRig"

# Names of bones to delete
bones_to_delete = ["DEF-teeth.B", "DEF-teeth.T"]


# Get the armature object
armature_obj = bpy.data.objects.get(armature_name)

if armature_obj and armature_obj.type == 'ARMATURE':
    delete_bones_by_name(armature_obj, bones_to_delete)
else:
    print("Armature object not found or is not of type ARMATURE.")

