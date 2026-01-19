

ranges = open("input.txt").read().splitlines()[0]

ranges = ranges.split(",")

counter = 0

def devisers_of_n(num) :    
    devisers = []
    for i in range(1, num//2 +1):
        if num % i == 0 : 
            devisers.append(i)
    return devisers

def devided_by_n(str_num, div=3) : 
    parts = []
    i = 0
    while i < len(str_num) :
        parts.append(str_num[i:i+div])
        i += div

    if parts.count(parts[0]) == len(parts) : 
        return True
    
    return False



for r in ranges :
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])

    for i in range(start, end + 1) :
        i = str(i)

        for d in devisers_of_n(len(i)) :
            if devided_by_n(i, d) :
                counter += int(i)
                break


print(counter)
