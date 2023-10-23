f = open("p79_passcode.txt", "r")
codes = []
for line in f:
  codes.append(int(line.strip().split(" ")[0]))
f.close()
digits = {}
for code in codes:
    for digit in str(code):
        if digit in digits:
            digits[digit] += 1
        else:
            digits[digit] = 1
print(digits)
one = {}
two = {}
thr = {}
for code in codes:
    if str(code)[0] in one:
        one[str(code)[0]] += 1
    else:
        one[str(code)[0]] = 1
    if str(code)[1] in two:
        two[str(code)[1]] += 1
    else:
        two[str(code)[1]] = 1
    if str(code)[2] in thr:
        thr[str(code)[2]] += 1
    else:
        thr[str(code)[2]] = 1
print(one)
print(two)
print(thr)
#I want to do this without brute force, more of a brain teaser.
# 7 is first cuz it only appears in one
# 7xxxxxxx
# 0 is last cuz it only appears in thr
# 7xxxxxx0
# 9 is almost certaintly 2nd to last
# 7xxxxx90
# 3 is almost certaintly 2nd
# 73xxxx90
#looking at frequency, lets just guess
#3rd adn 4th are probably 6 and 1
#because 1 only happens once in thr, it likely goes 7316 
# 7316xx90
#this leaves 8 and 2
#similarily,  8 is first once, so that means it is likely 5th
#73162890
def check(guess):
    count = -1
    for code in codes:
        count += 1
        i = 0
        works = False
        for digit in str(guess):
            if digit == str(code)[i]:
                if i == 2:
                    works = True
                    break
                i += 1
        if not(works):
            return False, count
    return True

print()
print(check(73162890))
print()

def has_repeated(codes):
    for code1 in codes:
        sames = 0
        for code2 in codes:
            if code1 == code2:
                sames += 1
                if sames > 1:
                    return True, code1
    return False
print(has_repeated(codes))