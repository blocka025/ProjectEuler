product = 0
for num1 in range(1000):
  for num2 in range(1000):
    if ((num1+1)**2+(num2+1)**2)**(1/2) + num1 + num2 + 2 == 1000.0:
      product = int((num1+1)*(num2+1)*(((num1+1)**2+(num2+1)**2)**(1/2)))
print(product)