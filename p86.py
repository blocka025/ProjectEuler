#We can break down this into 2 dimesions. The shortest path will allows be the hypotenuse of a right triangle with one leg as the longest length of the cube, and the other leg the length of the sum of the other two sides.
M = 1
total = 0
while 1:
    for sum in range(2,2*M+1):
            if (sum**2 + M**2)**.5 % 1 == 0:
                #print('sum',sum,'M',M)
                for leg in range(sum//2,0,-1):
                    if sum - leg <= M:
                        total += 1
                        #print(leg,sum-leg,M)
                    else:
                        break
    if total > 1000000:
        break
    M += 1
print(M)