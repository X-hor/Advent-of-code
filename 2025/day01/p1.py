import re
rotations = open ("input.txt").read().splitlines()
p = 50
count = 0
for rotation in rotations :
    match = re.match(r"^([A-Z])(\d+)$", rotation)
    direction = match[1]
    distance = int(match[2])

    if direction == "R" :
        p += distance
    else :
        p -= distance 
    
    p = p % 100

    if p == 0 :
        count += 1

print(count)