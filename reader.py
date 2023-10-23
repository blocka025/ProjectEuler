def summer(lists):
    total = 0
    if type(lists) is list:
        for ints in lists:
            total += ints
        return total
real = {}
total = 0
f = open('ProjectEuler/p88data.txt')
for line in f:
    data = line.split(':')
    #print(data)
    real[int(data[0])] = int(data[1])
f.close()
a = []
for n in range(12002):
    #print(n)
    if n in real:
        if not(real[n] in a):
            total += real[n]
            a.append(real[n])
print(total)