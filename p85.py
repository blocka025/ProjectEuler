def getrect(length,width,breakpoint):
    total = 0
    for l in range(1,length+1):
        for w in range(1,width+1):
            if total > breakpoint:
                return total
            else:
                horizontal = length+1-l
                vertical = width + 1 - w
                total += horizontal*vertical
    return total
def sumfromto(startint,endint):
    return ((endint-startint+1)*(startint+endint))//2
#I must first find the stop case where there is at least 2 million rectanges. For any given length, l, the width of 1 will have the fewest rects inside. There will be 1+2+3+4.....l total rects.
#This means stop n can be found with 2,000,000 < (n)(n+1)/2
#solving this yields n<2000
smallest = [0,0,0,2000000]#this list contains the legnth, width, value, and smallest distance from 2 mil

#test

for l in range(1,2000):
    #print(l,smallest)
    for w in range(1,l+1):
        rect = getrect(l,w,smallest[3]+2000000)
        diff = abs(rect-2000000)
        if diff < smallest[3]:
            smallest = [l,w,rect,diff]
            print('Best Guess:',l*w)
print(smallest)
print('Final Answer:',smallest[0]*smallest[1])