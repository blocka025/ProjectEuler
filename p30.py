poopy = []
for num in range(2,1000000):
  dig_sum = 0
  for letter in str(num):
    dig_sum += int(letter)**5
  if dig_sum == num:
    poopy.append(num)
total = 0
for dig in poopy:
  total += dig
print(total)