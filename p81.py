f = open("p81_matrix.txt", "r")
matrix = []
for line in f:
  matrix.append(line.strip().split(","))
f.close()
print(matrix)
for i, a in enumerate(matrix):
    for b in range(len(a)):
        matrix[i][b] = int(matrix[i][b])
sums = []
tot = 0
for a in matrix[0]:
    tot += a
    sums.append(tot)
for row in range(1,80):
    guess = []
    while len(guess)<80:
        guess.append([])
    for col in range(0,80):
        tot = sums[col]
        for guecol in range(col,80):
            tot += matrix[row][guecol]
            guess[guecol].append(tot)
    sums = []
    for col in range(0,80):
        sums.append(min(guess[col]))
print(sums[79])    