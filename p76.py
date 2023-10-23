nums = [1,1,2,3,5,7,11,15,22]
pents = []
for n in range(1,9):
    pents.append(n*(3*n-1)//2)
    pents.append(-n*(-3*n-1)//2)
while len(nums) < 101:
    new = 0
    for i, pent in enumerate(pents):
        if pent <= len(nums):
            if i % 4 == 0 or i % 4 == 1:
                coef = 1
            else:
                coef = -1
            new += coef* nums[-pent]
    nums.append(new)

print(nums[100]-1)