longest = [0,0]
chain = 0
for m in range(1000000):
  num = m
  chain = 0
  while num != 1 and num != 0:
    if num%2==0:
      num /=2
    else:
      num = 3*num + 1
    chain +=1
  if chain > longest[0]:
      longest = [chain,m]
print(longest[1])