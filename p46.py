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
for n in range(10000):
  if is_prime(n):
    primes.append(n)
    
for n in range (9,1000000,2):
  if not(is_prime(n)):
    q = False
    for a in primes:
      if q:
        break
      elif a>n:
        print("winner winner chicken dinner\n{}".format(n))
        break
      for b in range(1,10000):
        if a+2*b**2> n:
          break
        elif a+2*b**2 == n:
          q = True
          break
