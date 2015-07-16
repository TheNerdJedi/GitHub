# So finally I found the time to do some documentation. I rode a small script for looping the import of x3d files. It works like this:


# In the Main Scene first you do the setup (Camera position etc.).
# After that you have to set up the script parameters (filenames, materials, resize).
# Then execute the script.

# The script copies the Main Scene to the Render Scene and imports in there the time step of the 3xd file, renders and deletes it.

# It is a quite simple script and it works only with one object for each x3d file, Blender 2.48a.


import Blender 
import bpy
import import_web3d
from Blender import Types, Object, Mesh, Camera, Lamp, Scene, Window, Material, NMesh
from Blender.Scene import Render

#http://www.futura-designs.de/

print '+++start import+++'
print" __ "
print" _) _| "
print")( __)(_| "

#Parameter
frameS = 45 #Startframe
frameE = 46 #Endframe
name = "step_" #Filename
input ="C:/Users/"
output ="C:/render/"

for frame in range(frameS,frameE):
#NEW Scene
scn=Scene.GetCurrent()
scn2=scn.copy(2)
scn2.setName('renderScene')
scn2.makeCurrent()

#Import
frame_n = frame*100
tmp=input+name+str(frame_n)+".x3d"
print tmp
import_web3d.load_web3d(tmp) 


#Editing add parameters
water = bpy.data.materials['blue']

for me in bpy.data.meshes:
me.materials = [water]
for me in bpy.data.objects:
me.setSize(0.2,2,0.2)

#Rendering
scn2=Scene.GetCurrent()
context = scn2.getRenderingContext()
context.renderPath = output
context.getRenderPath()
context.render()
context.saveRenderedImage(name+str(frame_n), 0)
#Render.CloseRenderWindow()
Window.RedrawAll() 
scn=Scene.Get('Scene')
scn.makeCurrent()
Scene.Unlink(scn2)

print '+++end import+++'