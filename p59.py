ascii_dict = dict()
ascii_in_number = range(0,256)
for i in ascii_in_number:
    ascii_dict[str(i)] = chr(i)
#print(ascii_dict)

f = open("p59_cipher.txt", "r")
for line in f:
  text= line.split(",")
f.close()
big = 0
for a in range(97,123):
  for b in range(97,123):
    for c in range(97,123):
      total = 0
      results = []
      count1 = 0
      count2 = 0
      count3 = 0
      count4 = 0
      count5 = 0
      count6 = 0
      q = False
      for num in range(len(text)):
        if num%3 == 0:
          results.append(a ^ int(text[num]))
        elif num%3 == 1:
          results.append(b ^ int(text[num]))
        elif num%3 == 2:
          results.append(c ^ int(text[num]))
      for count in range(len(text)-2):
        if (results[count] == 116 or results[count] == 84) and (results[count+1] == 104 or results[count+1] == 72) and (results[count+2] == 101 or results[count+2] == 69):
          count1 += 1
          #the
        if (results[count] == 97 or results[count] == 65) and (results[count+1] == 110 or results[count+1] == 78) and (results[count+2] == 100 or results[count+2] == 68):
          count2 += 1
          #and

      for count in range(len(text)-1):
        if (results[count] == 98 or results[count] == 66) and (results[count+1] == 101 or results[count+1] == 69):
          count3 += 1
          #be
        if (results[count] == 116 or results[count] == 84) and (results[count+1] == 111 or results[count+1] == 79):
          count4 += 1
          #to
        if (results[count] == 111 or results[count] == 79) and (results[count+1] == 102 or results[count+1] == 70):
          count5 += 1
          #of
        if (results[count] == 105 or results[count] == 73) and (results[count+1] == 110 or results[count+1] == 78):
          count6 += 1
          #in
      if count1>0 and count2>0 and count1 + count2 + count3 + count4 + count5 + count6 > big:
        data = (a,b,c)
        big = count1 + count2 + count3 + count4 + count5 + count6
results = []
for num in range(len(text)):
  if num%3 == 0:
    results.append(data[0] ^ int(text[num]))
  elif num%3 == 1:
    results.append(data[1] ^ int(text[num]))
  elif num%3 == 2:
    results.append(data[2] ^ int(text[num]))
total = 0
for num in results:
  print(ascii_dict[str(num)],end="")
for num in results:
  total += num
print()
print(total)