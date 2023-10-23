import numpy as np
import matplotlib.pyplot as plt

def prop_div(num):
  n = 1
  divisors = []
  while n<=num**(1/2):
    if num%(n)==0:
      divisors.append(n)
      if not(num//n in divisors):
        divisors.append(num//n)  
    n+=1
  return divisors

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

def get_divisors(num):
    if num <= 3 or is_prime2(num):
        return[]
    n = 2#I am manually including
    divisors = [1,num]
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

def get_pair_count(n):
    total = 0
    for x in range(n+1,2*n+1):
        if n*x%(x-n) == 0:
            total +=1
            # print('beaner',n,x-n)
    return total

def get_pair_count2(num):
    n = 1
    divisors = []
    while n<=num**(1/2):
        if num%(n)==0:
            divisors.append(n)
            if not(num//n in divisors) and not(n==1):
                divisors.append(num//n)  
        n+=1
    return divisors

def p_info(n):
#    print(n,'\t',get_pair_count(n),get_divisors(n),len(a:=prop_div(n)))
    print(n,'\t',get_pair_count(n),get_divisors(n),(len(a:=prop_div(n**2))+1)//2)
    a.sort()

def convert_to_pairs(data):
    total = 1
    for n in data:
      total *=2*n+1
    return total//2 +1

def strictly_decreasing_lists(x):
    def generate_lists(target_sum, current_list, start):
        if target_sum == 0 and len(current_list) == x:
            current_list.sort(reverse=True)  # Sort in descending order
            result.append(current_list)
            return
        if len(current_list) >= x or target_sum < 0:
            return

        for i in range(start, target_sum + 1):
            new_list = current_list + [i]
            generate_lists(target_sum - i, new_list, i)

    if x <= 0:
        return [[]] if x == 0 else []

    result = []
    generate_lists(x, [], 0)
    return result

def lst_to_n (lst):
    ps = total_primes[:(l:=len(lst))]
    n = 1
    for i in range(l):
        n *= ps[i]**lst[i]
    return n
      

# Example usage:
maxim = (0,np.inf,0)
for x in range(25):
    result = strictly_decreasing_lists(x)
    
    for lst in result:
        a  = convert_to_pairs(lst)
        # if a>maxim[1]:
        #     maxim = (x,a,lst_to_n(lst),lst)
        #     print(maxim)
        if a>4e6 and (n :=lst_to_n(lst))<maxim[1]:
        #    print(a,n,maxim[1])
           maxim = (a,n,lst)
# print(maxim)
print(maxim[1])




# print(2*2*2*3*3*3*5*5*7*7*11*13*17*19*23*29*31*37)