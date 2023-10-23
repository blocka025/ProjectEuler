def is_cyclic(num1,num2,num3,num4,num5,num6):
  if str(num1)[2:] == str(num2)[:2] and str(num2)[2:] == str(num3)[:2] and str(num3)[2:] == str(num4)[:2] and str(num4)[2:] == str(num5)[:2] and str(num5)[2:] == str(num6)[:2] and str(num6)[2:] == str(num1)[:2]:
    return True
  else:
    return False

def is_polygonal(num):
  if ((-1+(1+8*num)**.5)/2)%1 == 0 or num**.5%1 == 0 or ((1+(1+24*num)**.5)/6)%1 == 0 or ((1+(1+8*num)**.5)/4)%1 == 0 or ((3+(9+40*num)**.5)/10)%1 == 0 or ((1+(1+3*num)**.5)/3)%1 == 0:
    return True
  else:
    return False

def get_polygonal(num,lis,i):
  lis[i] = []
  if ((-1+(1+8*num)**.5)/2)%1 == 0:
    lis[i].append(0)
  if num**.5%1 == 0:
    lis[i].append(1)
  if ((1+(1+24*num)**.5)/6)%1 == 0:
    lis[i].append(2)
  if((1+(1+8*num)**.5)/4)%1 == 0:
    lis[i].append(3)
  if ((3+(9+40*num)**.5)/10)%1 == 0:
    lis[i].append(4)
  if ((1+(1+3*num)**.5)/3)%1 == 0:
    lis[i].append(5)
  return lis
  
def has_all(nums):
  all = [0,1,2,3,4,5]
  for num in nums:
    if len(num) == 1:
      if num[0] in all:
        all.remove(num[0])
      else:
        return False
  if len(all) == 0:
    return True
  final = []
  for num in nums:
    if len(num) != 1:
      final.append(num)
  if len(final) == 1 and len(all) == 1 and (final[0][0] in all or final[0][1] in all):
    return True
  if len(final) == 2 and len(all) == 2 and final[0][0] == all[0] and final[1][1] == all[1]:
    return True
  for val in all:
    if val != 0 and val != 3:
      return False

nums = []
for num in range(1000,10000):
  if is_polygonal(num):
    nums.append(num)

for a in nums:
  poly = [[],[],[],[],[],[]]
  poly = get_polygonal(a,poly,0)
  for b in nums:
    if a != b and str(a)[2:] == str(b)[:2]:
      poly = get_polygonal(b,poly,1)
      for c in nums:
        if c != b and c!=a and str(b)[2:] == str(c)[:2]:
          poly = get_polygonal(c,poly,2)
          for d in nums :
            if d != b and d!=a and d != c and str(c)[2:] == str(d)[:2]:
              poly = get_polygonal(d,poly,3)
              for e in nums:
                if e != b and e!=a and e != c and e!=d and str(d)[2:] == str(e)[:2]:
                  poly = get_polygonal(e,poly,4)
                  for f in nums:
                    if f != b and f!=a and f != c and f!=d and f != e and str(e)[2:] == str(f)[:2]  and str(f)[2:] == str(a)[:2]:
                      poly = get_polygonal(f,poly,5)
                      if has_all(poly):
                        print(a,b,c,d,e,f)
