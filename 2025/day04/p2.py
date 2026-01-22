def get_neighbors(row, col, grid):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
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

def removed_rolls(grid) :
    # new_grid = [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]
    new_grid = [list(row) for row in grid]
    
    count = 0
    for y in range(len(grid)) :
        for x in range(len(grid[0])) :
            if grid[y][x] == "@" :
                if is_accessed_rolls(x, y, grid) :
                    count += 1
                    new_grid[y][x] = "."
    return new_grid, count

grid = open ("input.txt").read().splitlines()
result = 0
while True :
    grid, removed = removed_rolls(grid)
    if removed == 0 :
        break
    result += removed

print(result)