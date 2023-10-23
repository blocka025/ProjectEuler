def get_dig_sum(num):
  output = 0
  for dig in str(num):
    output+= int(dig)
  return output 

max = 0
for a in range(100):
  for b in range(100):
    if get_dig_sum(a**b)>max:
      max = get_dig_sum(a**b)
print(max)