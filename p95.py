def prop_div(num):
  n = 1
  divisors = []
  while n<=num**(1/2):
    if num%(n)==0:
      divisors.append(n)
      if not(num//n in divisors) and not(n==1):
        divisors.append(num//n)  
    n+=1
  return divisors

def summer(lists):
    total = 0
    for ints in lists:
        total += ints
    return total

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

longestchain = []
for n in range(2,1000001):
    if not(is_prime2(n)):
        chain = [n]
        chainlen = 0
        new = n
        while True:
            new = summer(prop_div(new))
            if new == n and len(chain)>len(longestchain):
                    longestchain = chain
                    # print(chain,'weiner')
                    break
            elif new > 1000000 or new in chain or is_prime2(new):
                break
            chain.append(new)

print(longestchain)
print(min(longestchain))
