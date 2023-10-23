import math
num = 999999
for n in range(9,-1,-1):
  print(num//math.factorial(n))
  num -= (num//(math.factorial(n)))*math.factorial(n)