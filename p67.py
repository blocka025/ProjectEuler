f = open("p67_triangle.txt", "r")
tri = []
for line in f:
  tri.append(line.strip().split(" "))
f.close()
length =100
active  = [(tri[0][0],0)]
for row in range(len(tri)-1):
  sus = []
  for num in active:
    sus.append((int(num[0]) + int(tri[row + 1][num[1]]),num[1]))
    sus.append((int(num[0]) + int(tri[row + 1][num[1] + 1]),num[1]+1))
  active = []
  for num1 in range(row+2):
    big = 0
    for su in sus:
      if su[1] == num1 and su[0] > big:
        big = su[0]
    active.append((big,num1))
big = 0
for su in active:
  if su[0] > big:
    big = su[0]
print(big)