from functools import cache
@cache
def dfs(root, target):
    if root == target:
        return 1
    if root not in graph:
        return 0
    
    return sum(dfs(neighbor, target) for neighbor in graph[root])

graph = {}
for line in open("input.txt"):
    line = line.strip().split(":")
    graph[line[0]] = line[1].split()

print(dfs("svr", "fft") 
      * dfs("fft", "dac") 
      * dfs("dac", "out") 
      + dfs("svr", "dac") 
      * dfs("dac", "fft") 
      * dfs("fft", "out")
)