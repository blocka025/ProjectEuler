def is_inc(num):
    for d in range(len(s:=str(num))-1):
        if int(s[d]) > int(s[d+1]):
            return False
    return True

def is_dec(num):
    for d in range(len(s:=str(num))-1):
        if int(s[d]) < int(s[d+1]):
            return False
    return True

def is_bouncy(num):
    return not(is_inc(num) or is_dec(num))


bouncies = set([])
non_bouncies = set([1,2,3])
n = 3
while len(bouncies)/(len(bouncies)+len(non_bouncies))<.99:
    n +=1
    if is_bouncy(n):
        bouncies.add(n)
    else:
        non_bouncies.add(n)
print(n)