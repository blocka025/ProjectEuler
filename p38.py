def is_pandig(st):
  nums = ["1","2","3","4","5","6","7","8","9"]
  if len(st) == 9:
      poop = []
      for letter in st:
        poop.append(letter)
      poop.sort()
      if poop == nums:
        return True
  return False

penis = ""
biggest = 0
for num1 in range(2,5):
  for num2 in range(10**(5-num1),10**(6-num1)):
    penis = ""
    for num3 in range(num1):
      penis+=str(((num3+1)*num2))
    if is_pandig(penis):
      if int(penis) > biggest:
        biggest = int(penis)
print(biggest)
