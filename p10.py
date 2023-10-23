num = 2
prime_sum = 0
while num <2000000:
  prime = True
  n=2
  while n<=num**(1/2):
    if num%(n)==0:
      prime = False
      break
    n+=1
  if prime:
    prime_sum +=num
    print()
  num +=1
print(prime_sum)