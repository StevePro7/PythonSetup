import meshcore

m = meshcore.Mesh()
m.vertices = [
    meshcore.Vector3(0,0,0),
    meshcore.Vector3(1,0,0),
    meshcore.Vector3(0,1,0),
]

m.smooth()