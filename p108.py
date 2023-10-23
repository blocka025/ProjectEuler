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

total_primes = []
f = open("C:/Users/blake/Documents/VSCode/Python/ProjectEuler/primes.txt", "r")
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

def get_divisors(num):
    if num <= 3 or is_prime2(num):
        return[]
    n = 2#I am excluding 1 and num
    divisors = []
    while num != 1:
        if num%(n)==0:
            divisors.append(n)
            num = num//n
            while num/n%1==0:
                divisors.append(n)
                num = num//n
            if is_prime2(num):
                divisors.append(num)
                return divisors
        n+=1
    return divisors


total = 0
n=120000
while total < 1000:
    total = 0
    n+=60
    inv_n = 1/n
    for x in range(n+1,2*n+1):
        if n*x%(x-n) == 0:
        # if (y := n*x%(x-n)) == 0:
            total +=1
            if total >1000 or 2*n-x+total<1000:
                break
        # print(x,y)
    
    # input()
    if total > 500:
        divs = get_divisors(n)
        divs.sort()
        print(n,total)
        print(divs,len(divs))    
print(n)