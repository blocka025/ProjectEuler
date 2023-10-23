factorial = {'0':1,'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880}

total = 0
for start in range(1,1000000):
  da_set = set([start])
  old = start
  summ = start
  #input(da_set)
  while True:
    old = summ
    summ = 0
    for digit in str(old):
      summ += factorial[digit]
      #print(factorial[digit])
      #print(start,digit,summ)
    if summ in da_set:
      break
    else:
     da_set.add(summ)
  #if start == 69 or start == 871 or start == 872 or start == 78 or start == 540:
    #print(da_set)
    #input()

  if len(da_set) == 60:
    total += 1
    #print(start,da_set)
print(total)