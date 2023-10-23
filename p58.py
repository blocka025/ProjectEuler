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

below_10 = False
length = 1
prime_count = 0
total = 1
while not(below_10):
  length +=2
  x = length**2 - (length-1)
  y = x - (length-1)
  z = y - (length-1)
  total += 4
  #print(x,y,x)
  if is_prime(x):
    prime_count += 1
  if is_prime(y):
    prime_count += 1
  if is_prime(z):
    prime_count += 1
  if prime_count/total < .1:
    below_10 = True
  
print(length)