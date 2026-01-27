points = [list(map(int, line.strip().split(","))) for line in open("input.txt")]
max_area = 0
for i, (x1, y1) in enumerate(points) :
    for x2, y2 in points[i+1:] :
        a = abs(x2-x1)+1
        b = abs(y2-y1)+1
        area = a * b
        max_area = max(max_area, area)
        
print(max_area)