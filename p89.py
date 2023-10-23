f = open("ProjectEuler/p89_roman.txt", "r")
romans = []
all = ''
for i, line in enumerate(f):
    if i + 1 != 1000:
        romans.append(line[0:-1])
        all += line
    else:
        romans.append(line)
        all += line
f.close()
# print(all)
newstr = all

newstr = newstr.replace('LXXXX','XC')
newstr = newstr.replace('DCCCC','CM')
newstr = newstr.replace('VIIII','IX')
newstr = newstr.replace('IIII','IV')
newstr = newstr.replace('CCCC','CD')
newstr = newstr.replace('XXXX','XL')
# print(newstr)
print(len(all) - len(newstr))

out = ''
correct = []
for char in newstr:
    if char == '\n':
        correct.append(out)
        out = ''
    else:
        out += char
correct.append(out)


def streakcheck(dig,letters,five):
    consec = 0
    saved = 0
    # [v,1,1,1,1]
    # print(letters,dig,five)
    # input()
    # print(letters)
    for i,letter in enumerate(letters):
        if letter == dig:
            consec += 1
        else:
            consec = 0
        # print(i,letters,consec)
        # input('sdfasd')
        if consec == 4:
            if i>3 and letters[i-4]==five:
                # print(letters,'+3')
                # input()
                saved += 3
            else:
                # print(letters,'+2')
                # input()
                saved += 2
    # if saved == 0:
    #     print('all good papa g')
    # else:
    #     print('imma just take ',saved,' off the top')
    # input(letters)
    return saved

def getnum(letters):
    letters = list(roman)
    nums = []
    for letter in letters:
        nums.append(roman2nums[letter])
    for i in range(len(nums)):
        if i > 0:
            if nums[i] > nums[i-1]:
                nums[i] = nums[i] - nums[i-1]
                nums[i-1] = 0
    sum = 0
    for num in nums:
        sum += num
    return sum

def getroman(num):
    digits = list(str(num))
    roman = ''
    for i, digit in enumerate(digits):
        dig = int(digit)
        while dig > 0:
            if dig == 4 and not(i==0 and len(digits)==4):
                roman += num2romans[10**(len(digits)-i-1)] + num2romans[5*10**(len(digits)-i-1)]
                dig = 0
            elif dig == 9 and not(i==0 and len(digits)==4):
                roman += num2romans[10**(len(digits)-i-1)] + num2romans[10*10**(len(digits)-i-1)]
                dig = 0
            elif dig >= 5:
                roman += num2romans[5*10**(len(digits)-i-1)]
                dig -= 5
            else:
                roman += num2romans[10**(len(digits)-i-1)]
                dig -= 1
    return roman

num2romans = {1 : 'I', 5 : 'V', 10 :'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
roman2nums = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

totalorigchars = 0
totalnewchars = 0
test = []
for roman in romans:
    totalorigchars += len(roman)
    totalnewchars += len(getroman(getnum(roman)))
    test.append(getroman(getnum(roman)))
    # print(totalnewchars,totalorigchars)
    # print(getroman(getnum(roman)),roman)
    # input()

for n in range(1000):
    if test[n] != correct[n]:
        print(test[n],correct[n])
        print(n)
print(totalorigchars-totalnewchars)

saved = 0
for roman in romans:
    oldsaved = saved
    counts = {'I' : 0, 'V' : 0, 'X' : 0, 'L' : 0, 'C' : 0, 'D' : 0, 'M' : 0}
    letters = list(roman)
    num = getnum(letters)
    strlen = 0
    digits = list(str(num))
    # print(num)
    for i, digit in enumerate(digits):
        dig = int(digit)
        if dig < 4:#0,1,2,3
            strlen += dig
        elif dig == 4 or dig == 9:#4,9
            # print(i,len(digits))
            if i == 0 and len(digits) == 4:
                strlen += 4
            else:
                strlen += 2
        else:#5,6,7,8
            strlen += dig-4
    # print(letters,getnum(letters))
    # print(len(letters)-strlen)
    # saved += len(letters)-strlen
    for letter in letters:
        counts[letter] += 1
    if counts['C'] >= 4:
        saved += streakcheck('C',letters,'D')
    if counts['X'] >= 4:
        saved += streakcheck('X',letters,'L')
    if counts['I'] >= 4:
        saved += streakcheck('I',letters,'V')
    # print(saved,strlen,num)
    if saved -oldsaved != len(letters)-strlen:
        print(num)
        print(len(letters)-strlen)
        print(letters)
        print(counts)
        input()
print(saved)
