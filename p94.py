total = 0
# ls = []
for l in range(3,(1000000005)//3,2):
    if ((3*l+1)*(l-1))**.5%1 ==0:
        if 3*l+1<=1e9 and (int(((3*l+1)*(l-1))**.5))**2 == (3*l+1)*(l-1):
            total += 3*l+1
            # print(l,'+1')
            # ls.append(l)
            # if len(ls)>1:
            #     print('l ratio =',ls[-1]/ls[-2])
    if ((3*l-1)*(l+1))**.5%1 ==0:
        if 3*l-1<=1e9 and (int(((3*l-1)*(l+1))**.5))**2 == (3*l-1)*(l+1):
            total += 3*l-1
            # print(l,'-1')
            # ls.append(l)
            # if len(ls)>1:
            #     print('l ratio =',ls[-1]/ls[-2])
print(total)