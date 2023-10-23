def init_is_prime2():
  primes = []
  f = open("ProjectEuler\primes.txt", "r")
  for line in f:
    primes.append(int(line))
  f.close()
  return primes
primes = init_is_prime2()

def is_prime2(num):
  if num == 2:
    return True
  if num%2 ==0 or num == 1:
    return False
  n = 0
  while primes[n]**2<=num:
    if num%(primes[n])==0:
      return False
    n+=1
  return True

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
  
a =[]
b=[]
x = 10**5
print("start")
for num in range(x):
  if is_prime(num):
    a.append(num)
print(len(a))

for num in range(x):
  if is_prime2(num):
    b.append(num)
print(len(b))
