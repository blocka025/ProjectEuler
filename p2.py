num1 = 1
num2 = 2
total = 0
num3 = 0
while num3 < 4000000:
  if num2%2 == 0:
    total += num2
  num3 = num1 + num2 
  num1 = num2
  num2 = num3
print(total)