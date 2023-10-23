m = 2
n = 1
k = 1
dic = {}
from math import gcd
while 2 * m ** 2 <= 1500000:
    while 2 * m ** 2 + 2 * m * n <= 1500000 and m > n:
        while 2 * m ** 2 + 2 * m * n <= 1500000 / k and gcd(gcd(m**2-n**2,2*m*n), gcd(2*m*n,m**2+n**2))== 1:
            if k * (2 * m ** 2 + 2 * m * n) in dic:
                dic[k * (2 * m ** 2 + 2 * m * n)] += 1
            else:
                dic[k * (2 * m ** 2 + 2 * m * n)] = 1
            k += 1
        n += 1
        k = 1
    #print(m)
    m += 1
    n = 1

tot = 0
for key in dic:
    if dic[key] == 1 and key <= 1500000:
        tot +=1

print(tot)