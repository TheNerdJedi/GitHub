# I'm importing an .obj file. Applying a material and a texture and then exporting again. 
# I've come to importing the file and creating a new material etc but now I need to apply it to the 
# imported object. But how do I access the object functions for the imported object?


import Blender
from Blender import Scene, Object, Material
import import_obj

ob = import_obj.load_obj('/home/arnaud/Documents/z25/bodycount/scans/Arnaud/scan_faceFrnt_scl8_tst02.obj',CLAMP_SIZE=10.0)
print(ob)

mat = Material.New('gezichtMat')
mat.rgbCol = [0.8, 0.2, 0.2]
ob.setMaterials(mat)

Blender.Redraw()




# import_obj dosnt return 1 object. make a new scene for each import, then loop on its objects.
# also, set the materials for the mesh, not the object
# ob.getData(mesh=1).materials = [mymat]