combos = []
for a in range(0,10):
    for b in range(0,10):
        if b<a:
            for c in range(0,10):
                if c<b:
                    for d in range(0,10):
                        if d<c:
                            for e in range(0,10):
                                if e<d:
                                    for f in range(0,10):
                                        if f<e:
                                            combos.append([a,b,c,d,e,f])
# print(len(combos))
# print(combos)
count = 0
for i,c1 in enumerate(combos):
    for j,c2 in enumerate(combos):
        if i>=j:
            if (0 in c1 and 1 in c2) or (1 in c1 and 0 in c2):
                if (0 in c1 and 4 in c2) or (4 in c1 and 0 in c2):
                    if (0 in c1 and (9 in c2 or 6 in c2)) or ((9 in c1 or 6 in c1)and 0 in c2):
                        if (1 in c1 and (6 in c2 or 9 in c2)) or ((6 in c1 or 9 in c1) and 1 in c2):
                            if (2 in c1 and 5 in c2) or (5 in c1 and 2 in c2):
                                if (3 in c1 and (6 in c2 or 9 in c2)) or ((6 in c1 or 9 in c1) and 3 in c2):
                                    if (4 in c1 and (9 in c2 or 6 in c2)) or ((9 in c1 or 6 in c1)and 4 in c2):
                                        if ((6 in c1 or 9 in c1) and 4 in c2) or (4 in c1 and (6 in c2 or 9 in c2)):
                                            if (8 in c1 and 1 in c2) or (1 in c1 and 8 in c2):
                                                count += 1
print(count)