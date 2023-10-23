total = 1
for num in range(1,501):
  x = (2*num+1)**2
  y = 3*((2*num)**2 + 1)
  total += x+y
print(total)
