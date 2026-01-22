# 8 directions (including diagonals)
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def get_neighbors(row, col, grid):
    neighbors = []
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            neighbors.append((nr, nc))
    return neighbors

def is_accessed_rolls(x, y, grid) :
    rolls = 0
    for nx, ny in get_neighbors(x, y, grid) :
        if grid[ny][nx] == "@":
            rolls += 1
    return rolls < 4


grid = open ("input.txt").read().splitlines()
count = 0
for y in range(len(grid)) :
    for x in range(len(grid[0])) :
        if grid[y][x] != "@" :
            continue
        if is_accessed_rolls(x, y, grid) :
            count += 1

print(count)