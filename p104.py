import time

def check_pan_dig(num): #not counting 0 #num is str #assuming 9 digits of string
    nums = set()
    for char in list(num):
        if char =='0':
            return False
        elif not(char in nums):
            nums.add(char)
        else:
            return False
    if len(nums) == 9:
        return True
    return False

def check_pan_dig2(num): #not counting 0 #num is str #assuming 9 digits of string
    a = num[:9]
    b = num[-9:]
    nums = set()
    for char in a:
        if char =='0' or char in nums:
            return False
        nums.add(char)
    nums = set()
    for char in b:
        if char =='0' or char in nums:
            return False
        nums.add(char)
    if len(a) ==9:
        return True
    else:
        return False

def get_fib(k,n1,n2):
    if k ==3:
        return n2,n1+n2
    else:
        return get_fib(k-1,n2,n1+n2)
def get_fib2(final):#final must be 3 or bigger
    count = 2
    n1,n2 = 1,1
    while final > count+1:
        n3 = n1 + n2#count+1
        n1 = n3 + n2#count+2
        n2 = n3 + n1#count+3
        count += 3
    if final%3==1:
        return n1
    elif final%3==2:
        return n2
    return n1 + n2
def get_fib3(n):
    a = 5**.5
    return round(((1+a)/2)**(n+1)/a,0)
 


# save_file = open('C:/Users/blake/Documents/VSCode/Python/ProjectEuler/FibNums.txt', "w")


n1,n2,n3 = 1,1,2
# save_file.write(str(n1)+'\n'+str(n2)+'\n')
k = 0
t1 = time.time()
# while not(check_pan_dig(str(n1)[:9]) and check_pan_dig(str(n1)[-9:])) and not(check_pan_dig(str(n2)[:9]) and check_pan_dig(str(n2)[-9:])) and not(check_pan_dig(str(n3)[:9]) and check_pan_dig(str(n3)[-9:])):
# while not(check_pan_dig2(a:=str(n1))) and not(check_pan_dig2(b:=str(n2))) and not(check_pan_dig2(c:=str(n3))):
while not(check_pan_dig2(str(n1))) and not(check_pan_dig2(str(n2))) and not(check_pan_dig2(str(n3))):
    n3 = n1 + n2#count+1
    n1 = n3 + n2#count+2
    n2 = n3 + n1#count+3
    k+=3
    # save_file.write(c+'\n'+a+'\n'+b+'\n')
print(time.time()-t1)

if check_pan_dig2(str(n1))and check_pan_dig2(str(n1)):
    print(k+1)
    print(n1)
elif check_pan_dig2(str(n2)) and check_pan_dig2(str(n2)):
    print(k+2)
    print(n2)
else:
    print(k)
    print(n3)
# print(check_pan_dig2(str(round(get_fib3(329466),0))))
# save_file.close()