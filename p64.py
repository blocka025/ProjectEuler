def flip(N,numers,denoms):
  sub = (N**.5 + numers) //denoms
  new_numer = denoms * sub - numers
  new_denom = (N - new_numer**2)/denoms
  return (sub,new_numer,new_denom)

total = 0
for N in range(10001):
  n = N ** .5
  if n%1 != 0:
    first = flip(N,0,1)
    rep = False
    numer = first[1]
    denom = first[2]
    rep_start = flip(N,numer,denom)
    numer = rep_start[1]
    denom = rep_start[2]
    count = 0
    while not(rep):
      count += 1
      results = flip(N,numer,denom)
      if results == rep_start:
        rep = True
      numer = results[1]
      denom = results[2]
    if count%2== 1:
      total += 1
print(total)