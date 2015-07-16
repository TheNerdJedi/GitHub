# http://blenderartists.org/forum/showthread.php?372944-Batch-3D-import-export-file-conversion-missing-can-t-find-textures&highlight=import

import bpy
import sys
 
#Get command line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "—"
mdl_in = argv[0]
fbx_out = argv[0] + ".fbx"
 
bpy.ops.nvb.importmdl(filepath=mdl_in, filter_glob="*.mdl")

bpy.ops.export_scene.fbx(filepath=fbx_out, axis_forward='-Z', axis_up='Y', version='BIN7400', use_selection=False, bake_space_transform=True, use_anim=False, bake_anim=False)