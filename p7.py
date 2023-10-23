prime_count = 0
num = 2
while prime_count <10001:
  prime = True
  n=2
  while n<=num**(1/2):
    if num%(n)==0:
      prime = False
      break
    n+=1
  if prime:
    prime_count +=1
  num +=1
print(num-1)

  