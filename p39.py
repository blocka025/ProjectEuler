most = 0
j = 0
counts = 1001*[0]
for a in range(1,334):
  for b in range(3,1000):
    for c in range(5,1000):
      if a**2+b**2 == c**2:
        p = a+b+c
        if p<=1000:
          counts[p] += 1
        break
      elif c>a+b or a>=b:
        break
for i, num in enumerate(counts):
  if num>most:
    j = i
    most = num
print(j)