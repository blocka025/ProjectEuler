def opdecoder(opind,left,right):
    if opind == 0:
        return left + right
    elif opind == 1:
        return left - right
    elif opind == 2:
        return left * right
    elif opind == 3:
        return left / right
    else:
        input("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")





#there needs to be many different combos
#first whter are the different combos of numbers 1-10 no repeats
#with this, there needs to be each of the combos for the four nums 1-10
#then there is the combo of each of the 3 operations with repeats
#similarly, there is the order of the 3 operations no repeats
fourcombos = []#for the orders of the four digits abcd
allthreecombos = []#for the different combos of the of four operations
for a in range(4):
    for b in range(4):
        if b != a:
            for c in range(4):
                if a != c and b != c:
                    for d in range(4):
                        if d != b and d != c and a != d:
                            fourcombos.append([a,b,c,d])

for a in range(4):
    for b in range(4):
            for c in range(4):
                allthreecombos.append([a,b,c])
                    
# print(fourcombos)
# input(allthreecombos)

longest = 0
for d in range(1,10):
    for c in range(1,10):
        if c>=d:
            break
        else:
            for b in range(1,10):
                if b>=c:
                    break
                else:
                    for a in range(1,10):
                        if a>=b:
                            break
                        else:
                            possibs = set()
                            nums = [a,b,c,d]
                            # signs = ['+','-','*','/']
                            for numorder in fourcombos:
                                for ops in allthreecombos:
                                    val = nums[numorder[0]]
                                    for i, op in enumerate(ops):
                                        val = opdecoder(op,val,nums[numorder[i+1]])
                                    # print(nums[numorder[0]],signs[ops[0]],nums[numorder[1]],signs[ops[1]],nums[numorder[2]],signs[ops[2]],nums[numorder[3]],'=',val)
                                    # input()
                                    if not(val in possibs) and val>=1:
                                        possibs.add(val)
                                        # print(nums,numorder,ops)
                                        # input(possibs)

                                    val = opdecoder(ops[1],opdecoder(ops[0],nums[numorder[0]],nums[numorder[1]]),opdecoder(ops[2],nums[numorder[2]],nums[numorder[3]]))
                                    if not(val in possibs) and val>=1:
                                        possibs.add(val)
                            ind = 0
                            while ind + 1 in possibs:
                                ind +=1
                            if ind >= longest:
                                longest = ind
                                winningstring =str(a)+str(b)+str(c)+str(d)
                                # print(a,b,c,d)
                                # print(ind)
                            # print(a,b,c,d,ind)
                            # input()
print(winningstring)
