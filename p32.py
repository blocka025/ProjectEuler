nums = ["1","2","3","4","5","6","7","8","9"]
poopy = []
for a in range(2,50):
  for b in range(50,10000):
    c = a*b
    if len(str(a)) + len(str(b)) + len(str(c)) == 9:
      poop = []
      for letter in str(a):
        poop.append(letter)
      for letter in str(b):
        poop.append(letter)
      for letter in str(c):
        poop.append(letter)
      poop.sort()
      if poop == nums and not(c in poopy):
        poopy.append(c)
        print(a,b,c)
total = 0
print(poopy)
for num in poopy:
  total+= num
print(total)