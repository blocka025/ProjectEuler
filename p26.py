def long_div (dividend, divisor,st,longest_rep):
  while dividend < divisor:
    dividend *=10
  st += str(dividend//divisor)
  dividend = dividend%divisor
  print(st,dividend,divisor)
  if dividend == 0:
    print("poopass")
    return st
  elif check_rep(st):
    if len(st)//2>longest_rep:
      longest_rep = len(st)//2
    return st
  long_div(dividend,divisor,st,longest_rep)
  
def check_rep(st):
  if len(st)%2 != 0:
    return False
  
  for n in range(len(st)//2):
    print(st[n],st[n+len(st)//2])
    if st[n]!=st[n+len(st)//2]:
      return False
  return True

def prop_div(num):
  n = 1
  divisors = []
  while n**2<=num:
    if num%(n)==0:
      num //= n 
      divisors.append(n)
      if not(num//n in divisors or n==1) and num//n<=1000:
        divisors.append(num//n)
    n+=2
    if n>1000:
      break
  return divisors
s = ""
poop = []
long_div(1,983,"",0)
print("poopoo")
for num in range(10000):
  s+="9"
  vals = prop_div(int(s))
  for val in vals:
    if not(val in poop):
      #print(val)
      poop.append(val)
      if val == 983:
        print(len(s))
print(len(poop))
for num in poop:
  if len(prop_div(num)) ==1:
    print(num)