lines = open("input.txt").read().split("\n\n")[0]
ranges = [list(map(int, r.split("-"))) for r in lines.splitlines()]
ranges.sort()

count = 0
last = None
for start, end in ranges:
    if last is None:
        last = (start, end)
    elif start <= last[1] : # 2-10, 5-15
        last = (last[0], max(end, last[1]))
    else: # 2-10, 12-15
        count += last[1] - last[0]+1
        last = (start, end)
        
count += last[1] - last[0]+1
print(count)


