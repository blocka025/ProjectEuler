total = 0
summ = 0
for num in range(100):
  total += (num+1)
  summ += (num+1)**2
print(total**2-summ)