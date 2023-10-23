def prop_div(num):
  n = 1
  divisors = []
  while n<=num**(1/2):
    if num%(n)==0:
      divisors.append(n)
      if not(num//n in divisors or n==1):
        divisors.append(num//n)
    n+=1
  return divisors

def summer(lists):
  total = 0
  for ints in lists:
    total += ints
  return total

abuns = []
for num in range(1,28124):
  if summer(prop_div(num)) > num:
    abuns.append(num)

can_sum = []
for num1 in range(1,28124):
  for num2 in abuns:
    if num2>=num1:
      break
    elif num1 - num2 in abuns:
      can_sum.append(num1)
      break

cant_sum = []
for num3 in range(1,28124):
  if not(num3 in can_sum):
    cant_sum.append(num3)

print(summer(cant_sum))
