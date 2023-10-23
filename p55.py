def add_pal(num):
  return num + int(str(num)[::-1])

def is_pal(num):
  if str(num) == str(num)[::-1]:
    return True
  else:
    return False

def is_lychrel(n):
  for num2 in range(50):
    n = add_pal(n)
    if is_pal(n):
      return False
  return True

total = 0
for num1 in range(1,10000):
  if is_lychrel(num1):
    total+=1
    print(num1)
    
print(total)