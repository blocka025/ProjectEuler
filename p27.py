def get_primes(end):
  primes = [2]
  for num in range(3,end+1,2):
    if len(prop_div(num)) == 1:
      primes.append(num)
  return primes

def prop_div(num):
  n = 1
  divisors = []
  while n**2<=num:
    if num%(n)==0:
      num //= n 
      divisors.append(n)
      if not(num//n in divisors or n==1):
        divisors.append(num//n)
    n+=2
  return divisors
big = 0
a0 = 0
b0 = 0
primes = get_primes(1000)
for a in range(-999,1000):
  for b in primes:
    m = 0
    while len(prop_div(m**2+a*m+b))==1:
      m+=1
    if m+1>big:
      big = m+1
      a0 = a
      b0 = b
print(big, a0*b0)
