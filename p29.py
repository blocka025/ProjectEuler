l = []
for a in range(2,101):
  for b in range(2,101):
    x = a**b
    if not(x in l):
      l.append(x)
print(len(l))