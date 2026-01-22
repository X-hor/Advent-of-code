p, count = 50, 0
for line in open("input.txt"):
    direction, distance = line[0], int(line[1:])
    p = (p + (distance if direction == "R" else -distance)) % 100
    count += (p == 0)
print(count)