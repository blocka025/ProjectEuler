import math

f = open("ProjectEuler/p99_exps.txt", "r")
nums = []
for line in f:
  nums.append(line.strip().split(","))
f.close()
# print(nums)

exps = []
for num in nums:
    exps.append(int(num[1])*math.log(int(num[0])))
print(exps.index(max(exps))+1)