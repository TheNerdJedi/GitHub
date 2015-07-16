# Convert obj to obj using Blender
#
# Run as follows:
#   blender -b dummy.blend -P bl_3ds2obj.py -- file.3ds ...
#
# dummy.blend is just an empty Blender file needed as an argument.
# Put one or more .3ds files on the end of the command. (in our case OBJs)
# The .obj files will be created with the same name (and path) as
# the .3ds file, but with the .obj extension.
# The export creates a .mtl file for each .obj file also.
 
import bpy #this is for blender  
import sys
import os.path
 
for i in range(1, len(sys.argv)):
    if sys.argv[i] == "--":
        break
 
for file in sys.argv[i+1:]:
    # Start with an empty scene
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
 
    # Read a .obj file
    bpy.ops.import_scene.obj(filepath=file)
 
    # Write a .obj file
    outfile = os.path.splitext(file)[0]+".obj"
    bpy.ops.export_scene.obj(filepath=outfile)