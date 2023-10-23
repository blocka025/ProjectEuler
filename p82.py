f = open("p81_matrix.txt", "r")
matrix = []
for line in f:
  matrix.append(line.strip().split(","))
f.close()
for i, row in enumerate(matrix):
    for col in range(len(row)):
        matrix[i][col] = int(matrix[i][col])
        #changing the strings to ints
sums = []# this will hold smallest value for each cell in the col
for i in range(len(matrix)):
    sums.append(matrix[i][0])
#this intialize the sums list by adding the leftmost val for each row

#now I will go one to the left and make that the new sum
#however, I will 
for col in range(1,len(matrix)):#this iterates from col 1 to 79 (skipping 0)
    #print(row)
    for row in range(len(matrix)):
        sums[row] = matrix[row][col] + sums[row]
        #this assumes the shortest path is directly to right
    for row in range(len(matrix)):
        sum = sums[row]#this is the starting point
        for belows in range(row,len(matrix)-1):
            newsum = sum + matrix[belows+1][col]
            if sums[belows+1] > newsum:
                sums[belows+1] = newsum
                sum = newsum
                #each time, the sum gets higher, as it travels farther
            else:
                break
                
        sum = sums[row]#this is the starting point
        for aboves in  range(row,0,-1):
            newsum = sum + matrix[aboves - 1][col]
            if sums[aboves-1] > newsum:
                sums[aboves-1] = newsum
                sum = newsum
                #each time, the sum gets higher, as it travels farther
            else:
                break
print(min(sums))   
