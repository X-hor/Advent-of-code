# p, count = 50, 0
# for line in open("input.txt") :
#     direction, distance = line[0], int(line[1:])
#     distance = distance if direction == "R" else -distance
    
#     # Count full rotations
#     count += abs(distance) // 100
    
#     # Check if we cross zero on partial rotation
#     new_p = (p + distance) % 100
    
#     if direction == "R" and p + (distance % 100) > 100 : 
#         count += 1
#     elif direction == "L" and p > 0 and new_p > p : # Wrapped around
#         count += 1
        
#     p = new_p
#     count += (p == 0)

# print(count)


p, count = 50, 0
for line in open("input.txt") :
    direction, distance = line[0], int(line[1:])
    distance = distance if direction == "R" else -distance

    count += abs(distance) // 100 
    if direction == "R" :
        if p + (distance % 100) > 100 : 
            count += 1
    else :
        mod = distance % -100
        if (p != 0) and (p + mod) < 0 :
            count += 1

    p = (p + distance) % 100
    count += (p == 0)

print(count)