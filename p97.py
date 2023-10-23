num = 28433
for n in range(7830457):
    num*=2
    if len(str(num))>10:
        num = int(str(num)[1:])
print(num+1)