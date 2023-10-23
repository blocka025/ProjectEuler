import math

def is_pal(numw):
  p = True
  for m in range(len(str(numw))):
    if str(numw)[m]!=str(numw)[-(m+1)]:
      return False
  return p

def binary(numb):
  output = ""
  for m in range(int(math.log2(numb)),-1,-1):
    output += str(numb // 2**m)
    numb-=(numb // 2**m)*(2**m)
  return output

pals = []
for num in range(1,1000000):
  if is_pal(num) and is_pal(int(binary(num))):
    pals.append(num)
total = 0
for pal in pals:
  total += pal
print(total)