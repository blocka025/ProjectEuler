def is_prime(num):
  if num%2 ==0:
    return False
  n = 3
  while n**2<=num:
    if num%(n)==0:
      return False
    n+=2
  return True

circs = [2,3,5,7]
is_circ = False
for num in range(11,1000000):
  if is_prime(num):
    numq = str(num)
    is_circ = True
    for n in range(len(numq)):
      numq = str(numq) + str(numq)[0]
      numq = numq[1:]
      if not(is_prime(int(numq))):
        is_circ = False
    if is_circ:
      circs.append(num)
print(len(circs))
