def method_1():
    lines = open("input.txt").read().split("\n\n")[0]
    ranges = [list(map(int, r.split("-"))) for r in lines.splitlines()]
    ranges.sort()

    count = 0
    last_start, last_end = None, None

    for start, end in ranges:
        if last_start is None:
            last_start, last_end = start, end
        elif start <= last_end + 1:
            last_end = max(end, last_end)
        else:
            count += last_end - last_start + 1
            last_start, last_end = start, end

    if last_start is not None:
        count += last_end - last_start + 1

    return count

def method_2():
    ranges = sorted([list(map(int, r.split("-"))) for r in open("input.txt").read().split("\n\n")[0].splitlines()])

    merged = [ranges[0]]
    for start, end in ranges[1:]:
        if start <= merged[-1][1] + 1:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    total = sum(e - s + 1 for s, e in merged)

    return total

print(method_1())
print(method_2())