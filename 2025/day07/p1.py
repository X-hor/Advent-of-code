grid = [line.strip() for line in open('input.txt')]
start_col = grid[0].index('S')

beams = {start_col}
count = 0
for row in range(1, len(grid)) :
    new_beams = set()
    for col in beams :
        if grid[row][col] == "^" :
            count += 1
            if col-1 >= 0 :
                new_beams.add(col-1)
            if col+1 <= len(grid[0]) :
                new_beams.add(col+1)
        else :
            new_beams.add(col)
    
    beams = new_beams
    
print(count)