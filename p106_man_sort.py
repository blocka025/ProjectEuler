save_file = open('C:/Users/blake/Documents/VSCode/Python/ProjectEuler/p106_7_need_checked', "w")
import copy
import numpy as np

summ = 0
new_data = [1,2,3,4,5,6,7,8,9,10,11,12]
count1 = 0

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
        # if np.sum(dat)>0 and np.sum(old_dat)>0:
        #     return 1
        if np.sum(old_dat)==np.sum(dat) and np.sum(dat)>1:
            
            inds1 = []
            inds2 = []
            for i in range(len(dat)):
                if dat[i]:
                    inds2.append(i)
                elif old_dat[i]:
                    inds1.append(i)   
            if max(inds1) > min(inds2) and max(inds1)>max(inds2):
                print(old_dat,dat)
                s = ''
                while s != 'y' and s !='n':
                    s = input('Need to check? (y/n)')
                print()
                if s != 'n':
                    save_file.write(str(old_dat)+'\t'+str(dat)+'\n')
                    return 1
                else:
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

print(get_arrs(7,[]))
save_file.close()
