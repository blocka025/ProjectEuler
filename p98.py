f = open("ProjectEuler/p98_words.txt", "r")
for line in f:
  words = line.split(',')
f.close()
cleaned = [0]*len(words)
for i,word in enumerate(words):
    cleaned[i] = word[1:-1]
words = cleaned
pairs = []
for i,w1 in enumerate(words):
    for j,w2 in enumerate(words):
        if i <= j:
            break
        else:
            is_pal = True
            for char in w1:
                if w1.count(char) != w2.count(char):
                    is_pal = False
                    break
            if is_pal:
                for char in w2:
                    if w1.count(char) != w2.count(char):
                        is_pal = False
                        break
                if is_pal:
                    pairs.append((w1,w2))
# print(pairs)
# input()
lengths = []
for pair in pairs:
    if not(len(pair[0]) in lengths):
        lengths.append(len(pair[0]))
# print(lengths)
squares = []
squarepairs = []
for length in range(max(lengths)+1):
    squares.append([])
    squarepairs.append([])
i = 1
while len(str(i**2)) <= max(lengths):
    if len(str(i**2)) in lengths:
        squares[len(str(i**2))].append(i**2)
    # else:
    #     i = i//(10**-.5)
    i+=1
# print(len(squares[9]))

for k, leng in enumerate(squares):
    print(k)
    for i,w1 in enumerate(leng):
        for j,w2 in enumerate(leng):
            if i <= j:
                break
            else:
                is_pal = True
                for char in str(w1):
                    if str(w1).count(char) != str(w2).count(char):
                        is_pal = False
                        break
                if is_pal:
                    for char in str(w2):
                        if str(w1).count(char) != str(w2).count(char):
                            is_pal = False
                            break
                    if is_pal:
                        squarepairs[k].append((w1,w2))
# print(squarepairs)
# for l in range(len(squarepairs)):
#     print(squarepairs[l])
#     input()

#now I need to make a profile each anagram number
wordprofs = []
for pair in pairs:
    prof = {}
    word1 = []
    i = 0
    for letter in pair[0]:
        if not(letter in prof):
            prof[letter] = i
            word1.append(i)
            i += 1
        else:
            word1.append(prof[letter])
    word2 = []
    for letter in pair[1]:
        word2.append(prof[letter])
    prof = {}
    word3 = []
    i = 0
    for letter in pair[1]:
        if not(letter in prof):
            prof[letter] = i
            word3.append(i)
            i += 1
        else:
            word3.append(prof[letter])
    word4 = []
    for letter in pair[0]:
        word4.append(prof[letter])
    wordprofs.append(((word1,word2),(word3,word4)))
# print(wordprofs)
sqprofs = []
for l in range(len(squarepairs)):
    sqprofs.append([])
    for pair in squarepairs[l]:
        prof = {}
        num1 = []
        i = 0
        for letter in str(pair[0]):
            if not(letter in prof):
                prof[letter] = i
                num1.append(i)
                i += 1
            else:
                num1.append(prof[letter])
        num2 = []
        for letter in str(pair[1]):
            num2.append(prof[letter])
        prof = {}
        num3 = []
        i = 0
        for letter in str(pair[1]):
            if not(letter in prof):
                prof[letter] = i
                num3.append(i)
                i += 1
            else:
                num3.append(prof[letter])
        num4 = []
        for letter in str(pair[0]):
            num4.append(prof[letter])
        sqprofs[l].append(((num1,num2),(num3,num4)))
# for l in range(len(squarepairs)):
#     print(squarepairs[l])
#     print(sqprofs[l])
#     input(l)

largest = 0
for i, pair in enumerate(wordprofs):
    for order1 in pair:
        l = len(order1[0])
        for j, nums in enumerate(sqprofs[l]):
            for order2 in nums:
                if order1 == order2:
                    # print(pairs[i],squarepairs[l][j])
                    # input()
                    if squarepairs[l][j][0] >largest:
                        largest = squarepairs[l][j][0]
                        # print(largest)
                    if squarepairs[l][j][1] >largest:
                        largest = squarepairs[l][j][1]
                        # print(largest)
print(largest)

