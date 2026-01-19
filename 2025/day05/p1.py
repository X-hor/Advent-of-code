lines = open("input.txt").read().splitlines()

blank_line_index = lines.index("")
ranges = lines[:blank_line_index]
ids = lines[blank_line_index+1:]

count = 0
for id in ids:
    id = int(id)
    for r in ranges:
        start, end = map(int, r.split("-"))
        if id in range(start, end + 1) :
            count += 1
            break

print("fresh ingredient : ", count)