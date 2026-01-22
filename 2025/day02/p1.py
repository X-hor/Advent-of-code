ranges = [list(map(int, range.split("-"))) for range in open("input.txt").read().split(",")]
numbers = sum((list(range(a, b+1)) for a, b in ranges), [])

count = 0
for num in numbers :
    s = str(num)
    if (len(s) % 2 == 0) and (s[:len(s) // 2] * 2 == s) :
        count += num

print(count)