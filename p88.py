import copy
def summer(lists):
    total = 0
    if type(lists) is list:
        for ints in lists:
            if ints != 1:
                total += ints
        return total
    elif type(lists) is dict:
        for key in lists:
            total += lists[key]
        return total
def product(lists):
    product = 1
    for ele in lists:
        product *= ele
    return product

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
        return[]
    n = 2#excluding 1 and num
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

def allsame(nums):
    first = nums[0]
    for num in nums:
        if num != first:
            return False
    return True

def combinations(numofgroups,inputdata,outputdata,i):
    if len(outputdata) == 0:
        for ind in range(numofgroups):
            outputdata.append([])
    if i == len(inputdata):
        divgroups.append(outputdata)
    else:
        for a in range(outlen(outputdata)+1):#a is the index of the bucket that each number is dropped into.
            if a != 0:
                outputdata[a-1].remove(inputdata[i])
            outputdata[a].append(inputdata[i])
            combinations(numofgroups,inputdata,copy.deepcopy(outputdata),i+1)
def samecomb(numofgroups,inputdata,outputdata,i):
    if len(outputdata) == 0:
        for ind in range(numofgroups):
            outputdata.append([])
    if i == len(inputdata):
        divgroups.append(outputdata)
    else:
        for a in range(outlen(outputdata)+1):#a is the index of the bucket that each number is dropped into.
            if a != 0:
                outputdata[a-1].remove(inputdata[i])
            outputdata[a].append(inputdata[i])
            b = True
            for box in outputdata:
                if len(box) > len(outputdata[0]):
                    b = False
                    break
            if b:
                samecomb(numofgroups,inputdata,copy.deepcopy(outputdata),i+1)
       

def hasonlyones(nums,n):
    for num in nums:
        if num == n:
            return True
        elif num != 1:
            return False
    return False

def getlen(nums):
    count = 0
    for num in nums:
        if num != 1:
            count += 1
    return count
def outlen(out):
    length = 0
    for list in out:
        if len(list) > 0:
            length += 1
        else:
            return length
    return length
minnums = {}
n = 4
while len(minnums) < 11999:
    if not(is_prime2(n)):
        # print(n,len(minnums))
        divs = get_divisors(n)#this gets divisiors except 1 and itself
        divgroups = []
        if allsame(divs):
            samecomb(len(divs),divs,[],0)
        else:
            combinations(len(divs),divs,[],0)
        #this assumes that combinations puts out a list of divisor groups which are nested in the external list. This should contain every combinatin of divisors that could make n with numofgroups numbers. Duplicates are fine, but disencouraged
        for group in divgroups:
            divnums = []
            for numbers in group:
                divnums.append(product(numbers))
            k = n - summer(divnums) + getlen(divnums)
            if k <=12000 and not(hasonlyones(divnums,n)):
                if not(k in minnums):
                    minnums[k] = n
    n += 1

a = []
total = 0
for n in range(12002):
    if n in minnums:
        if not(minnums[n] in a):
            total += minnums[n]
            a.append(minnums[n])
print(total)

# f = open("ProjectEuler\p88data.txt", "w")
# for k in minnums:
#     f.write(str(k) +':'+str(minnums[k])+"\n")
# f.close()

# f = open("ProjectEuler\p88uni.txt", "w")
# uniques.sort()
# for ele in uniques:
#     f.write(str(ele) +"\n")
# f.close()