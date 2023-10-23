total_primes = []
f = open("primes.py", "r")
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


def get_n_dig_primes(num_digits):
  primes = []
  for n in range(1, 10 ** (num_digits)):
      if is_prime2(n):
          primes.append(n)
  return primes


def main():
  lowest = 10 ** 10
  for num_digits in range(4, 10):
    #print(num_digits)
    primes = get_n_dig_primes(num_digits)
    for a in primes:
      if a> lowest:
        return lowest
      for b in primes:
        if a<b and is_prime2(int(str(a)+str(b))) and is_prime2(int(str(b)+str(a))):
          #print(b)
          for c in primes:
            if b<c and is_prime2(int(str(a)+str(c))) and is_prime2(int(str(c)+str(a))) and is_prime2(int(str(b)+str(c))) and is_prime2(int(str(c)+str(b))):
              for d in primes:
                if c<d and is_prime2(int(str(a)+str(d))) and is_prime2(int(str(d)+str(a))) and is_prime2(int(str(b)+str(d))) and is_prime2(int(str(d)+str(b))) and is_prime2(int(str(c)+str(d))) and is_prime2(int(str(d)+str(c))):
                  for e in primes:
                    if d<e and is_prime2(int(str(a)+str(e))) and is_prime2(int(str(e)+str(a))) and is_prime2(int(str(b)+str(e))) and is_prime2(int(str(e)+str(b))) and is_prime2(int(str(c)+str(e))) and is_prime2(int(str(e)+str(c))) and is_prime2(int(str(d)+str(e))) and is_prime2(int(str(e)+str(d))):
                      if a+b+c+d+e<lowest:
                        lowest = a+b+c+d+e
                        print(a,b,c,d,e)
print(main())