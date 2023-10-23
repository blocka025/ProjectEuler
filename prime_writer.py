def is_prime(num):
  n = 3
  while n**2<=num:
    if num%(n)==0:
      return False
    n+=2
  return True

primes = open("ProjectEuler\primes.txt", "w")
primes.write(str(2) +"\n")
n = 3
while n<1e7:
  if is_prime(n):
    primes.write(str(n) +"\n")
  n+=2
primes.close()
