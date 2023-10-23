D = 100000000
for n in range(1,10000):
  for m in range(1,1500):
    if n!=m:
      a = n*(3*n-1)//2
      b = m*(3*m-1)//2
      if ((1+(1+24*(a+b))**.5)/6)%1 == 0 and ((1+(1+24*abs(a-b))**.5)/6)%1 == 0:
        if abs(a-b) < D:
          D = abs(a-b)
          print(D)
          print(a,b)

print(D)