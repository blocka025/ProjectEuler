highest=0
for num1 in range(999,100,-1):
  for num2 in range(999,100,-1):
    test = num1*num2
    teststr = str(test)
    pal = True
    for i in range(3):
      if len(teststr)!=6 or test<highest:
        break
      if teststr[i] != teststr[-(i+1)]:
        pal = False
        break
    if pal:
      if test > highest:
        highest = test
print(highest)