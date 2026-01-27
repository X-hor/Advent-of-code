from collections import Counter

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
for _, a, b in pairs[:10] :
    if root(a) != root(b) :
        union(a, b)
print(parent)
# count circuit sizes
circuit_sizes = Counter(root(i) for i in range(len(points)))
print(circuit_sizes)
print(parent)
sizes = sorted(circuit_sizes.values(), reverse=True)
print(sizes)

# Product of 3 largest circuits
print(sizes[0] * sizes[1] * sizes[2])

print(parent)

#[x] 1. Parse all 3D points (x, y, z)
#[x] 2. Calculate distances between ALL pairs of points
#[x] 3. Sort pairs by distance (smallest first)
#[x] 4. Take the first 1000 pairs
#[x] 5. Use Union-Find to merge circuits as you connect pairs
#[x] 6. Find the 3 largest circuit sizes and multiply them