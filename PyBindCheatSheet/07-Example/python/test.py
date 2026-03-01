import my_api_py

def print_vertices(mesh):
    print("Vertices:")
    for v in mesh.vertices:
        print(f"({v.x:.2f}, {v.y:.2f}, {v.z:.2f})")

m = my_api_py.Mesh()
m.vertices = [
    my_api_py.Vector3(0,0,1),
    my_api_py.Vector3(1,0,0),
    my_api_py.Vector3(0,1,0),
]

print_vertices(m)
m.smooth()
print_vertices(m)
