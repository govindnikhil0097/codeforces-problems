import sys
def func():
    l = sys.stdin.read().split()
    if not l:
        return
    words = [str(x) for x in l[1:]]
    faces = 0
    for i in words:
        if i == "Icosahedron":
            faces += 20
        if i == "Cube":
            faces += 6
        if i == "Tetrahedron":
            faces += 4
        if i == "Dodecahedron":
            faces += 12        
        if i == "Octahedron":
            faces += 8
    print(faces)
if __name__ == "__main__":
    func()