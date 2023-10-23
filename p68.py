for a in range(1,11):
  for b in range(1,11):
    if a <b:
      for c in range(1,11):
        if b !=c and a <c:
          for d in range(1,11):
            if b !=d and a <d and c !=d:
              for e in range(1,11):
                if b !=e and a <e and c !=e and d != e:
                  for f in range(1,10):
                    if b !=f and a !=f and c !=f and d != f and e !=f:
                      for g in range(1,10):
                        if b !=g and a !=g and c !=g and d != g and e != g and f != g:
                          for h in range(1,10):
                            if b !=h and a !=h and c !=h and d != h and e != h and f != h and g !=h:
                              for i in range(1,10):
                                if b !=i and a !=i and c !=i and d != i and e != i and f != i and g !=i and h !=i:
                                  for j in range(1,10):
                                    if b !=j and a !=j and c !=j and d != j and e != j and f != j and g !=j and h !=j and j !=i:
                                      if a+f+g==b+g+h==c+h+i==e+j+f==d+i+j:
                                        print(a,f,g)
                                        print(b,g,h)
                                        print(c,h,i)
                                        print(d,i,j)
                                        print(e,j,f)
                                        print()                        