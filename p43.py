digs = ["1","2","3","4","5","6","7","8","9","0"]
primes = [2,3,5,7,11,13,17]

def pick_num(num):
  digs = ["1","2","3","4","5","6","7","8","9","0"]
  if len(num) == 10:
    p = True
    for num1 in range(7):
      if int(num[num1+1] + num[num1+2] + num[num1+3])% int(primes[num1]) != 0:
        p =False
        break
    if p:
      return int(num)
    else:
      return 0
  elif len(num) == 1:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1]) + pick_num(num + f[2]) + pick_num(num + f[3]) + pick_num(num + f[4]) + pick_num(num + f[5]) + pick_num(num + f[6]) + pick_num(num + f[7]) + pick_num(num + f[8])
  elif len(num) == 2:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1]) + pick_num(num + f[2]) + pick_num(num + f[3]) + pick_num(num + f[4]) + pick_num(num + f[5]) + pick_num(num + f[6]) + pick_num(num + f[7])
  elif len(num) == 3:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1]) + pick_num(num + f[2]) + pick_num(num + f[3]) + pick_num(num + f[4]) + pick_num(num + f[5]) + pick_num(num + f[6])
  elif len(num) == 4:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1]) + pick_num(num + f[2]) + pick_num(num + f[3]) + pick_num(num + f[4]) + pick_num(num + f[5])
  elif len(num) == 5:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1]) + pick_num(num + f[2]) + pick_num(num + f[3]) + pick_num(num + f[4])
  elif len(num) == 6:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1]) + pick_num(num + f[2]) + pick_num(num + f[3])
  elif len(num) == 7:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1]) + pick_num(num + f[2])
  elif len(num) == 8:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0]) + pick_num(num + f[1])
  elif len(num) == 9:
    f = digs
    for dig in num:
      f.remove(dig)
    return pick_num(num + f[0])
  else:
    return pick_num(num + "0") + pick_num(num + "1") + pick_num(num + "2") + pick_num(num + "3") + pick_num(num + "4") + pick_num(num + "5") + pick_num(num + "6") + pick_num(num + "7") + pick_num(num + "8") + pick_num(num + "9")

print(pick_num(""))