def is_prime(num):
  if num == 2:
    return True
  if num%2 ==0 or num == 1:
    return False
  n = 3
  while n**2<=num:
    if num%(n)==0:
      return False
    n+=2
  return True

primes = []
n = 11
while len(primes)!= 11:
  p = True
  for m in range(len(str(n))):
    q = str(n)[m:]
    if not(is_prime(int(q))):
      p = False
      break
  for m in range(len(str(n))-1):
    q = str(n)[:-(m+1)]
    if not(is_prime(int(q))):
      p = False
      break
  if p:
    primes.append(n)
  n +=2
total = 0
for nu in primes:
  total += nu
print(total)