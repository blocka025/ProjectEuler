def get_letters(numb):
  output = []
  for letter in numb:
    output.append(letter)
  return output

solved = False
num1 = 10000
while not(solved):
  num1 += 1
  ns = "1" + str(num1)
  #print(ns)
  for num2 in range(2,7):
    list1 = get_letters(ns)
    list2 = get_letters(str(int(ns)*num2))
    list1.sort()
    list2.sort()
    '''
    print(ns,list1)
    print(str(int(ns)*num2), list2)
    print()
    '''
    if list1 != list2:
      break
    elif num2 == 6:
      solved = True
print(ns)