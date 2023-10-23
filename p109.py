def check_under(data,lim=171):
    t = 0
    for d in data:
        t += int(d[1:])
    if t<lim:
        return True
    return False


sing = list(range(1,21))
sing.append(25)
dub = list(range(2,42,2))
dub.append(50)
trip = list(range(3,63,3))
for i in range(len(sing)):
    sing[i] = 's'+str(sing[i])
for i in range(len(dub)):
    dub[i] = 'd'+str(dub[i])
for i in range(len(trip)):
    trip[i] = 't'+str(trip[i])
al = sing+dub+trip
# print(al)
total = 0
l = 100
for a in dub:
    for b in al:
        for c in al:
                if int(b[1:])>=int(c[1:]) and check_under([a,b,c],l):
                    if int(b[1:])==int(c[1:]):
                        d = b[0]
                        e = c[0]
                        if d == e or (d=='s' and e =='d') or (d=='s' and e =='t') or (d=='d' and e =='t'):
                            total+=1
                    else:
                        total+=1

for a in dub:
    for b in al:
        if check_under([a,b],l):
            total+=1
        
for a in dub:
    if check_under([a],l):
        total+=1
print(total)