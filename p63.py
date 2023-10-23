b = 1
n = 1
total = 0
while True:
  while len(str(b**n)) <= n:
    if len(str(b**n)) == n:
      total += 1
    b += 1
  n += 1
  b = 1
  print(total)
