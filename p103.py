import numpy as np
import random
import copy
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

guess1 = [20,31,38,39,40,42,45]
lowest = [1000,'']
old_data = copy.deepcopy(guess1)
new_data = []
a = []
# for n in range(50000):
#     new_data = copy.deepcopy(old_data)
#     for m in range(3):
#         i = random.randint(0,6)
#         j = random.randint(0,1)
#         if j:
#             new_data[i] +=1
#         else:
#             new_data[i] -=1
    # input(new_data)
amp = 5
t = 0
f2 = 0
f = 0
for n1 in range(amp):
    for n2 in range(amp):
        for n3 in range(amp):
            for n4 in range(amp):
                for n5 in range(amp):
                    for n6 in range(amp):
                        for n7 in range(amp):
                            new_data = copy.deepcopy(guess1)
                            new_data[0] += n1 - amp + 2
                            new_data[1] += n2 - amp + 2
                            new_data[2] += n3 - amp + 2
                            new_data[3] += n4 - amp + 2
                            new_data[4] += n5 - amp + 2
                            new_data[5] += n6 - amp + 2
                            new_data[6] += n7 - amp + 2
                            # input(new_data)
                            if new_data[0]+new_data[1]>new_data[6] and np.sum(new_data)<lowest[0]:
                                if get_arrs(7,[]):
                                    t+=1
                                    # print('butts')
                                    s = ''
                                    for num in new_data:
                                        s += str(num)
                                    a.append([np.sum(new_data),s])
                                    if np.sum(new_data) < lowest[0]:
                                        lowest = [np.sum(new_data),s]
                                else:
                                    f+=1
                            else:
                                f2+=1
print(lowest[1])
# print(t,f,f2)
# print(a)