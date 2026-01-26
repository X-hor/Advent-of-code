grid = [line.strip() for line in open('input.txt')]
start_col = grid[0].index('S')

count = {start_col: 1}
for row in range(1, len(grid)) :
    new_count = {}
    
    for col, c in count.items() :
        if grid[row][col] == "^" :
            if col-1 >= 0 :
                new_count[col-1] = new_count.get(col-1, 0) + c
            if col+1 <= len(grid[0]) :
                new_count[col+1] = new_count.get(col+1, 0) + c
        else :
            new_count[col] = new_count.get(col, 0) + c
    count = new_count        
    
print(sum(count.values()))