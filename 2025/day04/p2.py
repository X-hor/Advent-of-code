

def neighbors(x, y) :
    for dx in [-1, 0, 1] :
        for dy in [-1, 0, 1] :
            if dx == 0 and dy == 0 :
                continue
            yield(x + dx, y + dy)

def accessed_rolls(grid,x, y) :
    rolls = 0
    for nx, ny in neighbors(x, y) :
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == "@":
            rolls += 1
    return rolls


def removed_rolls(grid) :
    new_grid = [[grid[y][x] for x in range(len(grid[0]))] for y in range(len(grid))]
    count = 0
    for y in range(len(grid)) :
        for x in range(len(grid[0])) :
            if grid[y][x] == "@" :
                rolls = accessed_rolls(grid, x, y)
                if rolls < 4 :
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