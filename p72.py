total_primes = []
f = open("ProjectEuler\primes.txt", "r")
for line in f:
  total_primes.append(int(line))
f.close()

def get_factors(num):
  factors = []
  if num in primes or num == 1:
    return factors
  else:
    for prime in total_primes:
      #print(prime)
      if num / prime % 1 == 0:
        factors.append(prime)
        while num / prime % 1 == 0 and num != 1:
          num = num // prime
      if num == 1:
        return factors

def in_primes():
  primes = set()
  f = open("ProjectEuler\primes.txt", "r")
  for line in f:
    primes.add(int(line))
  f.close()
  return primes

primes = in_primes()

def totient(n):
  product = int(n)
  if product == 1:
    return 1
  if product in primes:
    return product - 1
  else:
    factors = get_factors(product)
    for factor in factors:
      
      product *= (1 - factor**(-1))
    return int(product)

total = 0
for m in range(2,1000001):
  total += totient(m)
print(total)

''''
  1  	1	  2	  2	  4	  2	  6	  4	  6	  4
	10	4	  12	6	  8	  8	  16	6	  18	8
	12	10	22	8	  20	12	18	12	28	8
	30	16	20	16	24	12	36	18	24	16
	40	12	42	20	24	22	46	16	42	20
	32	24	52	18	40	24	36	28	58	16
	60	30	36	32	48	20	66	32	44	24
	70	24	72	36	40	36	60	24	78	32
	54	40	82	24	64	42	56	40	88	24
	72	44	60	46	72	32	96	42	60	40'''