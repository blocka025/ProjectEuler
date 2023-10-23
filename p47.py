def get_primes(num,lis):
  #will not work for prime numbers
  if num%2 ==0:
    if not(2 in lis):
      lis.append(2)
    return get_primes(num//2,lis)
  n = 3
  while n**2<=num:
    if num%(n)==0:
      if not(n in lis):
        lis.append(n)
      return get_primes(num//n, lis)
    n+=2
  if not(num in lis) and num != 1:
    lis.append(num)
  return lis

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

l1 = []
l2 = []
l3 = []
l4 = []
m = 1
t = True
while t:
  if not(is_prime(m)):
    l1 = get_primes(m,[])
    if len(l1) != 4:
      m+=1
    else:
      if not(is_prime(m+1)):
        l2 = get_primes(m+1,[])
        if len(l2) != 4:
          m+=2
        else:
          if not(is_prime(m+2)):
            l3 = get_primes(m+2,[])
            if len(l3) != 4:
              m+=3
            else:
              if not(is_prime(m+3)):
                l4 = get_primes(m+3,[])
                if len(l4) != 4:
                  m+=4
                else:
                  print(m)
                  t = False
              else:
                m+=4
          else:
            m+=3
      else:
        m+=2
  else:
    m+=1