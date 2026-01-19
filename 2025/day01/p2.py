import re

rotations = open ("input.txt").read().splitlines()
p = 50
count = 0
for rotation in rotations :
    match = re.match(r"^([A-Za-z]+)(\d+)$", rotation)
    direction = match[1]
    distance = int(match[2])

    if direction == "R" :
        div, mod = divmod(distance, 100)
        count += div
        if p + mod > 100 : 
            count += 1
    else :
        distance = - distance
        div, mod = divmod(distance, -100)
        count += div 
        if (p != 0) and (p + mod) < 0 :
            count += 1

    p = (p + distance) % 100

    if p == 0 :
        count += 1

print(count)