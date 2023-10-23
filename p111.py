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

import numpy as np

def get_n_count(data,n):
    output = 0
    for l in str(data):
        if l == str(n):
            output +=1
    return output

M = {
   0:3,
   1:3,
   2:3,
   3:3,
   4:3,
   5:3,
   6:3,
   7:3,
   8:3,
   9:3,
}
#max number of repeated digits for a given digit

S = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
}

for main_dig in range(10):
  for gap_space1 in range(10):
      for gap_dig1 in range(10):
          s = str(main_dig)*10
          s = s[:gap_space1] + str(gap_dig1) + s[gap_space1+1:]
          if is_prime2(int(s)) and int(s)>1e9:
              S[main_dig] += int(s)
              M[main_dig] = 9
for main_dig in range(10):
  if M[main_dig]<9:
      
    for gap_space1 in range(10):
        for gap_space2 in range(10):
            if gap_space2> gap_space1:
                for gap_dig1 in range(10):
                    for gap_dig2 in range(10):
                        s = str(main_dig)*10
                        s = s[:gap_space1] + str(gap_dig1) + s[gap_space1+1:gap_space2]  + str(gap_dig2) + s[gap_space2+1:]
                        if is_prime2(int(s)) and int(s)>1e9:
                            S[main_dig] += int(s)
                            M[main_dig] = 8

for main_dig in range(10):
  if M[main_dig]<8:
    for gap_space1 in range(10):
        for gap_space2 in range(10):
            if gap_space2> gap_space1:
                for gap_space3 in range(10):
                    if gap_space3> gap_space2:
                        for gap_dig1 in range(10):
                            for gap_dig2 in range(10):
                                for gap_dig3 in range(10):
                                  s = str(main_dig)*10
                                  s = s[:gap_space1] + str(gap_dig1) + s[gap_space1+1:gap_space2]  + str(gap_dig2) + s[gap_space2+1:gap_space3] + str(gap_dig3) + s[gap_space3+1:]
                                  if is_prime2(int(s)) and int(s)>1e9:
                                      
                                      S[main_dig] += int(s)
                                      M[main_dig] = 7 

print(summer(S))