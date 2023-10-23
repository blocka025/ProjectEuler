from math import gcd

big = (0, 0)
for d in range(1,1000001):
  n = d*3//7-1
  if n / d > big[0] and gcd(n,d) == 1:
    big = (n/d,n,d)
print(big)