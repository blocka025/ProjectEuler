def u(n):
    return 1+n**2+n**4+n**6+n**8+n**10-n-n**3-n**5-n**7-n**9
# the formula that I derived was u(n)=sum of i=1 to k [of the (product when i!=j of (n-j)/(i-j)) * u(n=i)] where k is the number
# of points used to make the approximation
wrongsum = 0
for k in range(1,11):
    nval = k+1
    sum = 0
    for i in range(1,k+1):
        product = 1
        for j in range(1,k+1):
            if i != j:
                product *= (nval-j)/(i-j)
        sum += product * u(i)
    # if k == 1:
    #     sum += u(k)
    # print(sum,k)
    wrongsum += sum
print(wrongsum)