

count = 0
for num in range(1,10000000):
    # print(num)
    chain = [num]
    while True:
        digits = list(str(num))
        newnum = 0
        for digit in digits:
            newnum += int(digit)**2
        if newnum == 89:
            count += 1
            break
        elif newnum in chain:
            if 89 in chain:
                count += 1
            break
        else:
            chain.append(newnum)
            num = newnum
    # print(chain,count)
    # input()
print(count)