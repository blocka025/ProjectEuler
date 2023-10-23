from math import gcd
total = 0
for d in range(4,12001):
 i = d//3 + 1
 while i * 2 < d:
  if gcd(i,d) == 1:
     total += 1
     #print(i,d)
     #input()
  i += 1
print(total)