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

def summer(lists):
  total = 0
  for ints in lists:
    total += ints
  return total
penis = []
for num in range(10000):
  num1 = summer(prop_div(num+1))
  num2 = summer(prop_div(num1))
  if num+1 == num2 and not(num2 in penis) and num1 != num2:
    penis.append(num1)
    penis.append(num2)
print(summer(penis))
print(penis)