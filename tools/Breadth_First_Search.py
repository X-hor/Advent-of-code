def floodFill(grid, row, col, p) :
    start = grid[row][col]
    queue = [(row, col)]
    visited = set()

    while len(queue) > 0 :
        row, col = queue.pop(0)
        visited.add((row, col))
        grid[row][col] = p

        for row, col in neighbors(grid, row, col, start) :
            if (row, col) not in visited :
                queue.append((row, col))
    return grid

def neighbors(grid, row, col, start) :
    indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [(row, col) for row, col in indices if is_valid(grid, row, col) and grid[row][col] == start]

def is_valid(grid, row, col) :
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])


grid = [[1, 0, 1, 1, 0], 
       [0, 1, 0, 1, 0], 
       [1, 1, 1, 1, 1], 
       [0, 0, 1, 0, 1], 
       [1, 0, 0, 0, 0]]

print(floodFill(grid, 2, 2, 2))

# output ;

[[1, 0, 2, 2, 0], 
 [0, 2, 0, 2, 0], 
 [2, 2, 2, 2, 2], 
 [0, 0, 2, 0, 2], 
 [1, 0, 0, 0, 0]]


