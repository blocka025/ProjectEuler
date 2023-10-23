def fib(final):
  if final == 1:
    return [1]
  elif final == 2:
    return [1,1]
  else:
    count = 2
    fib_nums = [1,1]
    while final > count:
      fib_nums.append(fib_nums[-1]+fib_nums[-2])
      count += 1
    return fib_nums
import math
n=1

while math.log10(fib(n)[-1])<999:
  n+=1
print(n)
print(fib(n)[-1])