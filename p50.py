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
primes = [2]
for num1 in range(3, 100000,2):
  if is_prime(num1):
    primes.append(num1)

big = 0
for n in range(6):
  total = 0
  for prime in primes[n:]:
    total += prime
    if total > 1000000:
      break
    elif is_prime(total):
      if big < total:
        big = total
  
print(big)
