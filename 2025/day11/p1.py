def dfs(graph, root, target, visited) :
    if root == target :
        return 1
    
    total = 0
    visited.add(root)
    for neighbor in graph[root] :
        if neighbor not in visited :
            total += dfs(graph, neighbor, target, visited)
    visited.remove(root)
    return total   

graph = {}
for line in open("input.txt") :
    line = line.strip().split(":")
    graph[line[0]] = line[1].split()
    
print(dfs(graph, "you", "out", set()))