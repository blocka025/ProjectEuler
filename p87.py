total_primes = []
f = open("ProjectEuler\primes.txt", "r")
for line in f:
  total_primes.append(int(line))
f.close()
total = 0
nums = set()
for a in total_primes:
    for b in total_primes:
        for c in total_primes:
            test = a**2+b**3+c**4
            if test < 50000000:
                if not(test in nums):
                    nums.add(test)
                    total+=1
            if c**4 > 50000000:
                break
        if b**3 > 50000000:
                break
    if a**2 > 50000000:
                break
print(total)