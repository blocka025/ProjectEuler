def is_pandig(st):
  nums = ["1","2","3","4","5","6","7","8","9"]
  nums = nums[:len(st)]
  poop = []
  for letter in st:
    poop.append(letter)
  poop.sort()
  if poop == nums:
    return True
  return False
def is_prime(num):
  if num%2 ==0:
    return False
  n = 3
  while n**2<=num:
    if num%(n)==0:
      return False
    n+=2
  return True
biggest = 0
for num in range(1,7654321):
  if is_pandig(str(num)) and is_prime(num):
    if num > biggest:
      biggest = num
print(biggest)