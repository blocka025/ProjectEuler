"""total=1
for n in range(21):
  print(n)
  ans = 2*((n+1)*(1+(n/2)*((n-2)*(n-1))/2))
  ans2 = ((n+1)*(1+(n/2)*(2**(n-1)-1)))

  print(int(ans),int(ans2))
for n in range(1,20):
  total += (n-1)*19
print(2*total)"""
def main(x,y):
  if x==20 and y==20:
    return 1 
  elif x == 20:
    return main(x,y+1)
  elif y == 20:
    return main(x+1,y)
  else:
    return main(x+1,y) + main(x,y+1)
for n in range(21):
  print(n,main(20-n,20-n))