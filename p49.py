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

def get_digs(num):
  l = []
  for letter in num:
   l.append(letter)
  l.sort()
  return l

for a in range(1000,10000):
  if is_prime(a):
    for m in range(1,10000):
      if a + 2*m < 9999:
        b = a + m
        if is_prime(b): 
          c = b + m
          if is_prime(c):
            if get_digs(str(a)) == get_digs(str(b)) == get_digs(str(c)):
              print(a,b,c)
