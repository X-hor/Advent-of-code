from z3 import *
import re

def min_presses(target, buttons):
    m = len(buttons)
    n = len(target)

    x = [Int(f"x{i}") for i in range(m)]
    opt = Optimize()

    for xi in x:
        opt.add(xi >= 0)

    for i in range(n):
        opt.add(Sum(x[j] for j in range(m) if i in buttons[j]) == target[i])

    opt.minimize(Sum(x))
    opt.check()
    model = opt.model()

    return sum(model[xi].as_long() for xi in x)


total = 0
for line in open("input.txt"):
    lights = re.search(r"\[(.*?)\]", line)  # ignored in part 2
    buttons = [
        list(map(int, b.split(",")))
        for b in re.findall(r"\((.*?)\)", line)
    ]
    targets = list(map(int, re.search(r"\{(.*?)\}", line).group(1).split(",")))

    total += min_presses(targets, buttons)

print(total)
