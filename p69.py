from math import gcd
def is_rel_prime(num,denom):
  if gcd(num,denom) == 1:
    return True
  else:
    return False
big = (0,0)
for n in range(2,1000001):
  rels = 1
  n = 510510
  for m in range(2,n):
    if is_rel_prime(n,m):
      rels += 1
      if n/rels<big[0]:
        break
  if n/rels > big[0]:
    big = (n/rels,n)
    if n == 510510:
      print(rels)
print(big)