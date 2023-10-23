def self_compose(a,b,k,D):
  return a**2+D*b**2,2*a*b,k**2

def main(D):
    if D ** .5 % 1 != 0:
      b = 1
      solved = False
      bot = D**.5//1
      top = bot + 1
      if abs(D - bot**2) < abs(D - top**2) and bot != 0:
          a = bot
      else:
          a = top
      k = int(a**2 - D)
      while not(solved):
          if k == 1:
            return int(a),int(b),D,k
          elif k == -1:
            return 2*a**2+1,2*b*a,D,k
          elif k == 2 and b != 1:
            return a**2-1,a*b,D,k
          elif k == -2:
            return a**2+1,a*b,D,k
          elif k == 4:
            if a % 2 == 1:
              return a/2*(a**2-3),b/2*(a**2-1),D,k
            else:
              return (a**2-2)/2,a*b/2,D,k
              
          last_val = -10**10
          last_m = 0
          t = 0
          x = 1
          while (a + b * x) % int(abs(k)) != 0:
            x += 1
          while True: 
              m = abs(k) * t + x
              val = m**2 - D
              if val * last_val < 0:
                  if abs(val) > abs(last_val) or m**2 == D:
                      m = last_m
                  break
              last_m = m
              last_val = val
              t += 1
          old_a = a
          a = int((a*m + D * b)//abs(k))
          b = int((old_a + m * b) // abs(k))
          k = int((m**2 - D) / k)

big_x = (0, 0, 0)
for D in range(1, 1001):
  output = main(D)
  if output != None:
    print(int(output[2]),int(output[0]),int(output[1]))
  if output != None and output[0] > big_x[0]:
    big_x = output
print()
print(int(big_x[2]),int(big_x[0]),int(big_x[1]))