def single_unflip(n,d,l):
  new_numer = n*l+d
  new_denom = n
  return (new_numer,new_denom)
num = 1
dem = 0
for k in range(66,0,-2):
  results = single_unflip(num,dem,1)
  num = results[0]
  dem = results[1]
  results = single_unflip(num,dem,k)
  num = results[0]
  dem = results[1]
  results = single_unflip(num,dem,1)
  num = results[0]
  dem = results[1]
last_num = dem+2*num
total = 0
for dig in str(last_num):
  total += int(dig)
print(total)