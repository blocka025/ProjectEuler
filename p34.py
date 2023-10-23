nums = []
import math
for n in range(3,10000000):
  tot = 0
  for letter in str(n):
    tot += math.factorial(int(letter))
  if tot == n:
    nums.append(n)
total = 0
for al in nums:
  total += al
print(total)