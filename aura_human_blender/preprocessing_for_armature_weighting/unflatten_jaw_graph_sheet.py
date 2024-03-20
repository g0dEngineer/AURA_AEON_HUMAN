import bpy

# Switch to Graph Editor workspace
bpy.context.area.type = 'GRAPH_EDITOR'

# Deselect all nodes
bpy.ops.graph.select_all(action='DESELECT')

# Select all nodes
bpy.ops.graph.select_all(action='SELECT')

# Get selected F-curves
selected_fcurves = bpy.context.selected_editable_fcurves

# Change interpolation mode to Bezier for selected F-curves
for fcurve in selected_fcurves:
    for keyframe_point in fcurve.keyframe_points:
        keyframe_point.interpolation = 'BEZIER'
        keyframe_point.handle_left_type = 'FREE'
        keyframe_point.handle_right_type = 'FREE'