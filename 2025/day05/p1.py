ranges = [list(map(int, line.split("-"))) for line in open('input.txt').read().split("\n\n")[0].splitlines()]
ids = [int(id) for id in open("input.txt").read().split("\n\n")[1].splitlines()]
count = 0
for id in ids:
    for r in ranges:
        start, end = r
        if start <= id <= end :
            count += 1
            break
print(count)