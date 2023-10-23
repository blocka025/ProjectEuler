tot = 0
for n in range(2,100):
    if round(n**.5,7) != n**.5:
        digs = 0
        for i in range(1,101):
            c = n * 100**(i-1)
            if n >9:
                c/10    
            l = 0
            r = 10
            while r-l > 1:
                if (digs + l + (r-l)//2)**2 <c:
                    l += (r-l)//2
                else:
                    r = l+(r-l)//2
            digs += l
            digs *= 10
        for d in str(digs):
            tot += int(d)
print(tot)
           