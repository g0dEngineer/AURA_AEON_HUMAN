import bpy

def save_scene_type():
    # Save current scene type
    saved_scene_type = bpy.context.scene.render.engine
    return saved_scene_type

def reset_scene_type(saved_scene_type):
    # Reset scene type to saved type
    bpy.context.scene.render.engine = saved_scene_type

def remove_sound_strip():
    # Remove sound strips from sequencer
    scene = bpy.context.scene
    for strip in scene.sequence_editor.sequences:
        if strip.type == 'SOUND':
            scene.sequence_editor.sequences.remove(strip)

# Save current scene type
saved_scene_type = save_scene_type()

# Remove sound strip
remove_sound_strip()

# Reset scene type
reset_scene_type(saved_scene_type)
