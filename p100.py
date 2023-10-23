import math

total_primes = []
f = open("ProjectEuler\primes.txt", "r")
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

def get_divisors(num):
    if num <= 3 or is_prime2(num):
        return[num]
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

def final_check(num):
    top = get_divisors(num) + get_divisors(num-1)
    N = int((1+(1+8*num*(num-1))**.5)/2)
    bottom = get_divisors(N) + get_divisors(N-1)
    # print(num,N)
    # print(top,bottom)
    # input()
    top.append(2)
    if sorted(top) == sorted(bottom):
        return True
    else:
        return False



# print(get_divisors(707106783028))
# print(get_divisors(707106783027))

# print()

# print(get_divisors(1000000002604))
# print(get_divisors(1000000002603))
# input()

def is_sq(num):
    i = int(num**.5)
    if i**2 == num:
        # print(num)
        return True
    else:
        return False


#https://www.desmos.com/calculator/y8dfgoro5q where I guess my starting number
n = 756872312736 #this is a guessing starting point using fitting
i = 0
while True:
    if is_sq(1+8*(n+i)*(n+i-1)) and final_check(n+i):
        print(n+i)#,(1+(1+8*((n+i)**2-(n+i)))**.5)//2)
        break
    if is_sq(1+8*(n-i)*(n-i-1)) and final_check(n-i):
        print(n-i,(1+(1+8*((n-i)**2-(n-i)))**.5)//2)
        break
    i += 1
# print(i) #my guess was 14737 off of 7*10^11...damn I'm good
# print(n+i-int(1e12*(2**-.5))+1)

# i = 1
# while True:
#     if is_sq(1+8*i*(i-1)) and final_check(i):
#         print(i,(1+(1+8*(i**2-i))**.5)//2)
#     i += 1

# n=int(1e12*(2**-.5))+1
# # n = 500
# # while not(((1+8*(n**2-n))**.5-1)%2==0 and final_check(n)):
# while not(is_sq(1+8*n*(n-1)) and final_check(n)):
#     n-=1
#     # print(n)
# N = (1+(1+8*(n**2-n))**.5)//2
# print(n,(1+(1+8*(n**2-n))**.5)/2)
# print((n**2-n)/(N**2-N))
# print(math.log10(N))