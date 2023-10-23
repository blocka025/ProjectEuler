def get_digs(num):
  word = []
  for letter in str(num):
      word.append(letter)
  word.sort()
  return word

master = []
n = 0
dig_count = 1
solved = False
while not(solved):
  n += 1
  digs = get_digs(n**3)
  if len(digs) > dig_count:
    dig_count += 1
    master = [digs]
  else:
    master.append(digs)
    if master.count(digs) == 5:
      solved = True
for num in range(n+1):
  if get_digs(num**3) == digs:
    print(num, num**3)
    #print(digs)