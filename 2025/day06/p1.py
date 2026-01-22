lines = [line.strip().split() for line in open("input.txt")]
cols = list(zip(*lines))
total = 0
for *numbers, op in cols:
    total += eval(op.join(numbers))
print(total)
#  One-liner potential
print(sum(eval(op.join(nums)) for *nums, op in zip(*[line.split() for line in open("input.txt")])))