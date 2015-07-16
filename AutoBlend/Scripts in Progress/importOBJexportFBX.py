import bpy
import sys
 
#Get command line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "—"
obj_in = argv[0] #we have to change this to OBJ 
fbx_out = argv[0] + ".fbx"
 
# Import the OBJ file
# See http://www.blender.org/api/blender_python_api_2_60_0/bpy.ops.import_scene.html
bpy.ops.import_scene.obj(filepath=obj_in, check_existing=True, filter_glob="*.obj;*.mtl")

# Export as FBX 
# See http://www.blender.org/documentation/blender_python_api_2_62_1/bpy.ops.export_scene.html
bpy.ops.export_scene.fbx(filepath=fbx_out, check_existing=True, filter_glob="*.fbx",)