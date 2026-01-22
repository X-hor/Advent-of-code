ranges = [list(map(int, range.split("-"))) for range in open("input.txt").read().split(",")]
numbers = sum((list(range(a, b+1)) for a, b in ranges), [])

def devisers_of_n(num) :    
    devisers = []
    for i in range(1, num//2 +1):
        if num % i == 0 : 
            devisers.append(i)
    return devisers

counter = 0
for num in numbers :
    s = str(num)
    for d in devisers_of_n(len(s)) :
        if s[:d] * (len(s) // d) == s:
            counter += int(s)
            break
print(counter)