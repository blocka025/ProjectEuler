def checkall(matrix,sums,row,col,stopdist):
#I need a recursive function to see if there is a shorter route that goes backwards. It must keep going deeper in every direction before it stops
#row and col are the cell that is meant to be checked in 4 directions. It will update in every direction until it hits a cell that is smaller or reaches stop distance
    sum = sums[row][col]
    if row > 0 and sums[row-1][col] > sum + matrix[row-1][col]:
        #checks up
        sums[row-1][col] = sum + matrix[row-1][col]
        sums = checkall(matrix,sums,row-1,col,stopdist)
    if col > 0 and sums[row][col-1] > sum + matrix[row][col-1]:
        #checks left
        sums[row][col-1] = sum + matrix[row][col-1]
        sums = checkall(matrix,sums,row,col-1,stopdist)
    if row < stopdist and sums[row+1][col] > sum + matrix[row+1][col]:
        #checks down
        sums[row+1][col] = sum + matrix[row+1][col]
        sums = checkall(matrix,sums,row+1,col,stopdist)
    if col < stopdist and sums[row][col+1] > sum + matrix[row][col+1]:
        #checks right
        sums[row][col+1] = sum + matrix[row][col+1]
        sums = checkall(matrix,sums,row,col+1,stopdist)
    return sums
     

f = open("p81_matrix.txt", "r")
matrix = []
for line in f:
  matrix.append(line.strip().split(","))
f.close()
for i, row in enumerate(matrix):
    for col in range(len(row)):
        matrix[i][col] = int(matrix[i][col])
        #changing the strings to ints

stopdist = 1#this is the index of the last cell we will be checking each iteration
sums = []
for a in range(len(matrix)):
    sums.append([0]*len(matrix))
sums[0][0] = matrix[0][0]
while stopdist < len(matrix):
    #for each stop distance, I want three steps:
    #1 initize sums
    #1a initize sums for the lowest rows, by adding the previous sums with the current matrix val
    #1b repeat with rightest cols this will overwrite the bottom right, but that's fine.
    #2check all for each of the bottom row
    #3 check all for each of the rightest cols
    #this will be 4 loops
    for row in range(stopdist):#rightest
        sums[row][stopdist] = sums[row][stopdist-1] + matrix[row][stopdist]
    for col in range(stopdist):#bottomest
        sums[stopdist][col] = sums[stopdist-1][col] + matrix[stopdist][col]
    if sums[stopdist][stopdist-1] < sums[stopdist-1][stopdist]:
        sums[stopdist][stopdist] = sums[stopdist][stopdist-1] + matrix[stopdist][stopdist]
    else:
        sums[stopdist][stopdist] = sums[stopdist-1][stopdist] + matrix[stopdist][stopdist]
    #this should take care of the majority of work  
    for row in range(stopdist):#rightest
        sums = checkall(matrix,sums,row,stopdist,stopdist)
    for col in range(stopdist+1):#bottomest
        sums = checkall(matrix,sums,stopdist,col,stopdist)    
    sums = checkall(matrix,sums,stopdist,stopdist,stopdist)
    stopdist += 1
# I will need to add a final columna and row consolidation where I iterate towards the bottom right corner starting from the top right and then the bottom left to account for the cases where the shortest path is out there.
for col in range(len(matrix)):
    sum = sums[len(matrix)-1][col]
    for right in range(len(matrix)-1):
        if sums[len(matrix)-1][right] > sum + matrix[len(matrix)-1][right]:
            sums[len(matrix)-1][right] = sum + matrix[len(matrix)-1][right]
            sum += matrix[len(matrix)-1][right]
        else:
            break

for row in range(len(matrix)):
    sum = sums[row][len(matrix)-1]
    for below in range(len(matrix)-1):
        if sums[below][len(matrix)-1] > sum + matrix[below][len(matrix)-1]:
            sums[below][len(matrix)-1] = sum + matrix[len(matrix)-1][right]
            sum += matrix[below][len(matrix)-1]
        else:
            break
print(sums[len(matrix)-1][len(matrix)-1])