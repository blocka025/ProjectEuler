n = 286
while ((1+(1+24*(n*(n+1)/2))**.5)/6)%1 != 0 or ((1+(1+8*(n*(n+1)/2))**.5)/4)%1 != 0:
  n+=1
print(n*(n+1)/2)