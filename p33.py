fracs = []
for a in range(11,100):
  for b in range(11,100):
    if a/b < 1 and str(a)[0] != "0" and str(b)[0] != "0" and str(a)[1]!= "0" and str(b)[1] != "0":
      a1 = str(a)[0]
      a2 = str(a)[1]
      b1 = str(b)[0]
      b2 = str(b)[1]
      if a1 == b1:
        if int(a2) / int(b2) == a/b:
          fracs.append(a/b)
      elif a1 == b2:
        if int(a2) / int(b1) == a/b:
          fracs.append(a/b)
      elif a2 == b1:
        if int(a1) / int(b2) == a/b:
          fracs.append(a/b)
      elif a2 == b2:
        if int(a1) / int(b1) == a/b:
          fracs.append(a/b)
print(fracs)
com = 1
for frac in fracs:
  com *= frac
print(com)