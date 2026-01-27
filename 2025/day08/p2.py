def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

def root(x):
    if parent[x] != x:
        parent[x] = root(parent[x]) 
    return parent[x]

def union(x, y) :
    parent[root(x)] = root(y)

points = []
for line in open('input.txt'):
    x, y, z = map(int, line.strip().split(","))
    points.append((x, y, z))
    
pairs = []
for i, p1 in enumerate(points) :
    for j, p2 in enumerate(points[i+1:]) :
        dist = distance(p1, p2)
        pairs.append((dist, i, i+1+j))

pairs.sort()
parent = list(range(len(points)))
num_circuits = len(points)
for dist, a, b in pairs :
    if root(a) != root(b) :
        union(a, b)
        num_circuits -= 1
    if num_circuits == 1 : 
        print(points[a][0]*points[b][0])
        break