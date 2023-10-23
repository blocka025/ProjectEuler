m=1 
divisors = 0
while divisors < 500:
  divisors = 0
  tri_num = m*(m+1)/2
  n=1
  while n<=tri_num**(1/2):
    if n == tri_num**(1/2):
      divisors+=1  
    elif tri_num%(n)==0:
      divisors+=2
    n+=1
  m+=1
print(int(tri_num))