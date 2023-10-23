import copy
import numpy as np

summ = 0
new_data = [1,2,3,4,5,6,7,8,9,10,11,12]


def get_arrs(leng,dat):
    if len(dat)<leng:
        dat1 = copy.deepcopy(dat)
        dat2 = copy.deepcopy(dat)
        dat1.append(0)
        dat2.append(1)
        return get_arrs(leng,dat1) + get_arrs(leng,dat2)
    else:
        if np.sum(dat)==0:
            return 0
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
        #start p106 specific stuff        
        if np.sum(old_dat)==np.sum(dat) and np.sum(dat)>1:
            inds1 = []
            inds2 = []
            for i in range(len(dat)):
                if dat[i]:
                    inds2.append(i)
                elif old_dat[i]:
                    inds1.append(i)   
            if max(inds1) > min(inds2) and max(inds1)>max(inds2):
                if old_dat[0]:
                    return 1
                # k = max(inds1)
                # while k>= min(inds2):#reduces redundancy
                #     if not(dat[k]) and not(old_dat[k]) and k<min(inds1):
                #         # print('beans',old_dat,dat)
                #         return 0
                #     k-=1
                
                # middle_count = 0
                # for ind in inds2:
                #     if ind>min(inds1):
                #         middle_count+=1
                # if middle_count == sum(old_dat):
                #     print('beans',old_dat,dat,'winner')
                #     return 1
                # else:
                k = max(inds1)
                bigger_count = 0
                while k> min(inds1):
                    if k in inds1:
                        bigger_count +=1
                    elif k in inds2:
                        bigger_count -= 1
                        if bigger_count <0:
                            # print(k)
                            # print('fucking beans',old_dat,dat)
                            return 1
                    k-=1
                return 0
            else:
                return 0
        else:
            return 0
    else:
        # print(old_dat,dat)
        if not(old_dat[len(dat)]):
            dat1 = copy.deepcopy(dat)
            dat2 = copy.deepcopy(dat)
            dat1.append(0)
            dat2.append(1)
            return get_subarrs(leng,old_dat,dat1) + get_subarrs(leng,old_dat,dat2)
        else:
            dat1 = copy.deepcopy(dat)
            dat1.append(0)
            return get_subarrs(leng,old_dat,dat1)

print(get_arrs(12,[]))