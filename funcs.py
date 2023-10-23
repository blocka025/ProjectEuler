def prop_div(num):
  n = 1
  divisors = []
  while n<=num**(1/2):
    if num%(n)==0:
      divisors.append(n)
      if not(num//n in divisors) and not(n==1):
        divisors.append(num//n)  
    n+=1
  return divisors

def summer(lists):
    total = 0
    if type(lists) is list or type(lists) is set:
        for ints in lists:
            total += ints
        return total
    elif type(lists) is dict:
        for key in lists:
            total += lists[key]
        return total

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

def long_div (dividend, divisor,st,longest_rep):
  while dividend < divisor:
    dividend *=10
  st += str(dividend//divisor)
  dividend = dividend%divisor
  print(st,dividend,divisor)
  if dividend == 0:
    print("poopass")
    return st
  elif check_rep(st):
    if len(st)//2>longest_rep:
      longest_rep = len(st)//2
    return st
  long_div(dividend,divisor,st,longest_rep)
  
def check_rep(st):
  if len(st)%2 != 0:
    return False
  
  for n in range(len(st)//2):
    print(st[n],st[n+len(st)//2])
    if st[n]!=st[n+len(st)//2]:
      return False
  return True

def get_primes(end):
  primes = [2]
  for num in range(3,end+1,2):
    if len(prop_div(num)) == 1:
      primes.append(num)
  return primes

def is_pal(numw):
  p = True
  for m in range(len(str(numw))):
    if str(numw)[m]!=str(numw)[-(m+1)]:
      return False
  return p

import math
def binary(numb):
  output = ""
  for m in range(int(math.log2(numb)),-1,-1):
    output += str(numb // 2**m)
    numb-=(numb // 2**m)*(2**m)
  return output

def is_prime(num):
  if num%2 ==0:
    return False
  n = 3
  while n**2<=num:
    if num%(n)==0:
      return False
    n+=2
  return True

def is_pandig(st):
  nums = ["1","2","3","4","5","6","7","8","9"]
  if len(st) == 9:
      poop = []
      for letter in st:
        poop.append(letter)
      poop.sort()
      if poop == nums:
        return True
  return False

def get_primes2(num,lis):
  #will not work for prime numbers
  if num%2 ==0:
    if not(2 in lis):
      lis.append(2)
    return get_primes(num//2,lis)
  n = 3
  while n**2<=num:
    if num%(n)==0:
      if not(n in lis):
        lis.append(n)
      return get_primes(num//n, lis)
    n+=2
  if not(num in lis) and num != 1:
    lis.append(num)
  return lis

def get_digs(num):
  l = []
  for letter in num:
   l.append(letter)
  l.sort()
  return l

def get_letters(numb):
  output = []
  for letter in numb:
    output.append(letter)
  return output

def add_pal(num):
  return num + int(str(num)[::-1])

def is_lychrel(n):
  for num2 in range(50):
    n = add_pal(n)
    if is_pal(n):
      return False
  return True

def get_dig_sum(num):
  output = 0
  for dig in str(num):
    output+= int(dig)
  return output 

total_primes = []
f = open("C:/Users/blake/Documents/VSCode/Python/ProjectEuler/primes.txt", "r")
for line in f:
  total_primes.append(int(line))
f.close()


def is_prime2(num):
  if num == 2:
    return True
  if num%2 ==0 or num == 1:
    return False
  n = 0
  while total_primes[n]**2<=num:
    if num%total_primes[n]==0:
      return False
    n+=1
  return True


def get_n_dig_primes(num_digits):
  primes = []
  for n in range(1, 10 ** (num_digits)):
      if is_prime2(n):
          primes.append(n)
  return primes

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

from math import gcd
def is_rel_prime(num,denom):
  if gcd(num,denom) == 1:
    return True
  else:
    return False

def init_is_prime2():
  primes = []
  f = open("ProjectEuler\primes.txt", "r")
  for line in f:
    primes.append(int(line))
  f.close()
  return primes
primes = init_is_prime2()

def in_primes():
  primes = set()
  f = open("ProjectEuler\primes.txt", "r")
  for line in f:
    primes.add(int(line))
  f.close()
  return primes

#https://www.youtube.com/watch?v=iJ8pnCO0nTY&t=752s
def partition(n):
    nums = [1,1,2,3,5,7,11,15,22]
    if n+1<= len(nums):
        return nums[n]
    pents = []
    a = 1
    while len(pents) < 5:
        pents.append(a*(3*a-1)//2)
        pents.append(-a*(-3*a-1)//2)
        a += 1
    while len(nums)<n+1:
        new = 0
        for i, pent in enumerate(pents):
            if pent <= len(nums):
                if i % 4 == 0 or i % 4 == 1:
                    new += nums[-pent]
                else:
                    new -= nums[-pent]
        nums.append(new)
        if len(nums)>= pents[-1]:
            pents.append(a*(3*a-1)//2)
            pents.append(-a*(-3*a-1)//2)
            a += 1
    return nums[-1]

def get_divisors(num):
    if num <= 3 or is_prime2(num):
        return[]
    n = 2#I am excluding 1 and num
    divisors = []
    while num != 1:
        if num%(n)==0:
            divisors.append(n)
            num = num//n
            while num/n%1==0:
                divisors.append(n)
                num = num//n
            if is_prime2(num):
                divisors.append(num)
                return divisors
        n+=1
    return divisors