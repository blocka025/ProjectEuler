def get_primes(end):
  primes = [2]
  for num in range(3,end+1,2):
    if len(prop_div(num)) == 1:
      primes.append(num)
  return primes

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


def primeSumCount(N,p1s,first = True):
    if len(p1s) == 1 and N % p1s[0] == 0:
        #print('return',N,p1s[0])
        return 1
    elif len(p1s) == 1 and N % p1s[0] == 1:
        return 0
    tot = 0
    for p1 in p1s:
        #print(N,p1,p1s,"butt")
        p = 0
        p2s = []
        if (N == p1 and first) or p1s[-1] == p1 and N-p1 == 0:
            tot += 1
        else:
            while N - p1 >= primes[p] and p1 >= primes[p]:
                p2s.append(primes[p])
                p +=1
            if len(p2s) > 0:
                #print(N,p2s,'penis')
                #input()
                tot += primeSumCount(N-p1,p2s,False)
        #print(p1,'tot =',tot)
    return tot
            
primes = get_primes(5000)   
for n in range(2,5001):
    #is the number being checked
    p = 0
    totsum = 0
    ps = []
    while n >= primes[p]:
        ps.append(primes[p])
        p +=1 
        #making a list of all the primes less than n
    totsum = primeSumCount(n,ps)
    print(n,totsum)
    #input()
    if totsum >= 5000:
        print(n)
        break