

def neighbors(x, y) :
    for dx in [-1, 0, 1] :
        for dy in [-1, 0, 1] :
            if dx == 0 and dy == 0 :
                continue
            yield(x + dx, y + dy)

def accessed_rolls(x, y) :
    rolls = 0
    for nx, ny in neighbors(x, y) :
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == "@":
            rolls += 1
    return rolls


grid = open ("input.txt").read().splitlines()
count = 0
for y in range(len(grid)) :
    for x in range(len(grid[0])) :
        if grid[y][x] != "@" :
            continue
        rolls = accessed_rolls(x, y)
        if rolls < 4 :
            count += 1

print(count)