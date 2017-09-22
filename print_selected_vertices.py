# Prints selected vertices in Blender
# To run:
# 
# filename = "/full/path/to/myscript.py"
# exec(compile(open(filename).read(), filename, 'exec'))
#
import bpy
import bmesh


obj = bpy.context.active_object
if bpy.context.mode == 'EDIT_MESH':
    bm = bmesh.from_edit_mesh(obj.data)
    verts = [ v.index for v in bm.verts if v.select ]
else:
    verts = [ v.index for v in obj.data.vertices if v.select ]

print(verts)
