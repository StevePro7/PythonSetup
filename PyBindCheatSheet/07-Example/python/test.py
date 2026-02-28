import my_api_py

m = my_api_py.Mesh()
m.vertices = [
    my_api_py.Vector3(0,0,0),
    my_api_py.Vector3(1,0,0),
    my_api_py.Vector3(0,1,0),
]

m.smooth()

print("Vertices:")
for v in m.vertices:
    print(f"({v.x}, {v.y}, {v.z})")