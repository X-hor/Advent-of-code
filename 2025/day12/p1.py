import re

lines = open("input.txt").read().split("\n\n")[-1].splitlines()
total = 0

for line in lines:
    x, y, *counts = list(map(int, re.findall(r"\d+", line)))
    print(x, y, counts)
    if (x // 3) * (y // 3) >= sum(counts):
        total += 1

print(total)

# This solution doesn't work with the exmple input 
# but work with the puzzle input 
# idk how but yeh its work!
