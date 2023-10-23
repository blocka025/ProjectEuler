total_primes = []
f = open("ProjectEuler\primes.txt", "r")
for line in f:
  total_primes.append(int(line))
f.close()


def is_prime2(num):
  if num == 2:
    return True
  if num%2 ==0 or num == 1:
    return False
  n = 0
  while total_primes[n]**2<=num:
    if num%total_primes[n]==0:
      return False
    n+=1
  return True

big = (2,2)
for n in range(3,10**7+1,2):
    rels = n - 1
    num = n
    for prime in total_primes:
      if num % prime == 0:
        rels -= n//prime - 1
        if n/rels > big[0]:
          break
        while num % prime == 0:
          num //= prime
        if is_prime2(num):
          rels -= n//num - 1
          break
      elif prime == num or (prime**2 > n and num == n):
        break
    if n/rels < big[0] and len(str(n)) == len(str(rels)):
      ns = []
      relss = []
      for i in range(len(str(n))):
        ns.append(str(n)[i])
        relss.append(str(rels)[i])
      ns.sort()
      relss.sort()
      if ns==relss and n/rels < big[0]:
        big = (n/rels,n)
print(big)