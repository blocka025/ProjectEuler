total_primes = set()
f = open("ProjectEuler\primes.txt", "r")
for line in f:
  total_primes.add(int(line))
f.close()