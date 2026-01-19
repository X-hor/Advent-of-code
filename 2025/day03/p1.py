lines = open("input.txt").read().splitlines()

count = 0
for line in lines :
    l = []
    line = str(line)
    for c in line :
        l.append(int(c))

    m = max(l[:-1])
    n = max(l[l.index(m)+1:])

    count += m*10 + n



    
print("counter = ", count)