def joltage(s):

    digits_need = 12
    length = len(s)
    result = []
    start = 0

    while len(result) < digits_need:
        remaining = digits_need - len(result)
        end = length - remaining

        window = s[start:end+1]
        maximun = max(window)

        result.append(maximun)
        start += window.index(maximun) + 1

    return "".join(result)


banks = open ("input.txt").read().splitlines()
result = sum(int(joltage(bank)) for bank in banks)
print("resutl : ", result)

