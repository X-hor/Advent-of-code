count = 0
for line in open("input.txt").read().splitlines() :
    numbers = list(map(int, line.strip()))
    first = max(numbers[:-1])
    second = max(numbers[numbers.index(first)+1:])
    count += first*10 + second
    
print(count)