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

nums = [1,1,2,3,5,7,11,15,22]
pents = []
a = 1
while len(pents)<10:
    pents.append(a*(3*a-1)//2)
    pents.append(-a*(-3*a-1)//2)
    a += 1
while 1:
    new = 0
    for i, pent in enumerate(pents):
        if pent <= len(nums):
            if i % 4 == 0 or i % 4 == 1:
                new += nums[-pent]
            else:
                new -= nums[-pent]
    nums.append(new)
    if new % 10**6 == 0:
        break
    if len(nums)>= pents[-1]:
        pents.append(a*(3*a-1)//2)
        pents.append(-a*(-3*a-1)//2)
        a += 1
print(len(nums)-1)
print()
print(new)