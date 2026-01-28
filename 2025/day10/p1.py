from itertools import combinations

def min_presses(target, buttons) :
    n = len(buttons)
    minimum = float("inf")
    # Try all combinations of buttons
    for r in range(n + 1):
        for combo in combinations(range(n), r):
            # Simulate pressing these buttons once each
            state = [0] * len(target)
            for idx in combo:
                for light in buttons[idx]:
                    state[light] ^= 1
            if state == target : 
                minimum = min(minimum, len(combo))
    return minimum            
               
lines = [line.split() for line in open('input.txt')]
total = 0
for line in lines : 
    pattern = line[0][1:-1]
    target = [1 if c == '#' else 0 for c in pattern]
    joltage = list(map(int, line[-1][1:-1].split(",")))
    buttons = []
    for button in line[1:-1] :
        if "," in button[1:-1] :
            buttons.append(tuple(map(int, button[1:-1].split(","))))
        else :
            buttons.append((int(button[1:-1]), ))
    
    total += min_presses(target, buttons)
    
print(total)

