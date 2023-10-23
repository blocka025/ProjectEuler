import copy
import numpy as np

def get_arrs(leng,dat):
    if len(dat)<leng:
        dat1 = copy.deepcopy(dat)
        dat2 = copy.deepcopy(dat)
        dat1.append(0)
        dat2.append(1)
        return get_arrs(leng,dat1) and get_arrs(leng,dat2)
    else:
        if np.sum(dat)==0:
            return True
        else:
            return get_subarrs(leng,dat,[])

def get_subarrs(leng,old_dat,dat):
    if len(dat)==leng:
        s1 = 0
        s2 = 0 
        for i,n1 in enumerate(old_dat):
            if n1:
                s1 += new_data[i]
        for i,n2 in enumerate(dat):
            if n2:
                s2 += new_data[i] 
        if np.sum(dat)==0:
            # print(old_dat,dat)
            # input()
            return True
        if s1==s2:
            # print('poop')
            # print(dat,old_dat)
            return False
        if (s1>s2 and np.sum(old_dat)<np.sum(dat)) or (s1<s2 and np.sum(old_dat)>np.sum(dat)):
            # print('pooper')
            return False 
        else:
            # print('huh?')
            return True
    else:
        # print(old_dat,dat)
        if not(old_dat[len(dat)]):
            dat1 = copy.deepcopy(dat)
            dat2 = copy.deepcopy(dat)
            dat1.append(0)
            dat2.append(1)
            return get_subarrs(leng,old_dat,dat1) and get_subarrs(leng,old_dat,dat2)
        else:
            dat1 = copy.deepcopy(dat)
            dat1.append(0)
            return get_subarrs(leng,old_dat,dat1)



f = open("C:/Users/blake/Documents/VSCode/Python/ProjectEuler/p105_sets.txt", "r")
sets = []
for line in f:
    sets.append(line.strip().split(","))
f.close()
summ = 0
for s in sets:
    new_data = []
    for n in s:
        new_data.append(int(n))
    if get_arrs(len(new_data),[]):
        summ += np.sum(new_data)
print(summ)