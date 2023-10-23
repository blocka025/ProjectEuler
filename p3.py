num = 600851475143
counter = 2
while num != counter:
  if num%counter == 0:
    num /= counter
  counter += 1
print(int(num))