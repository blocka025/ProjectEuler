import math
s=str(math.factorial(100))
print(s)
total = 0
for num in s:
  total+=int(num)
print(total)