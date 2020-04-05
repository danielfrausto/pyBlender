import bpy
def vMove(ObjectName,vUp):
    zUp = 0
    for v in bpy.data.objects[ObjectName].data.vertices:
        v.co[2] =v.co[2] + zUp
        zUp =zUp + vUp 

zUp = 0
for v in bpy.data.objects["Circle"].data.vertices:
    v.co[2] = zUp
    zUp =zUp +0.05
