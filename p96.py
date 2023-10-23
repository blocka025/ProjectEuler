f = open("ProjectEuler/p96_sud.txt", "r")
games = []
game = []
for line in f:
    row = []
    for char in line:
        if char == 'G':
            if len(game) > 0:
                games.append(game)
            game = []
            break
        elif char != '\n':
            row.append(int(char))
    if line[0] != 'G':
        game.append(row)
games.append(game)
f.close()


import copy

class board:
    def __init__(self,startingboard):
        self.grid = startingboard
        self.possibs = [[],[],[],[],[],[],[],[],[]]
        for r in range(9):
            for c in range(9):
                self.possibs[r].append([])
                entry = self.grid[r][c]
                if entry == 0:
                    self.possibs[r][c] = [1,2,3,4,5,6,7,8,9]
                else:
                    self.possibs[r][c] = entry
                    
    def getcol(self,c):
        col = []
        for i in range(9):
            if type(self.possibs[i][c]) is list:
                col.append(0)
            else:
                col.append(self.possibs[i][c])
        return col
    def getrow(self,r):
        row = []
        for i in range(9):
            if type(self.possibs[r][i]) is list:
                row.append(0)
            else:
                row.append(self.possibs[r][i])
        return row
    def getcell(self,c):
        #the cells will be numbered as follows
        # 0 1 2
        # 3 4 5
        # 6 7 8
        cell = []
        r0 = c//3
        c0 = c%3
        for i in range(3):
            for j in range(3):
                if type(self.possibs[3*r0 + i][3*c0 +j]) is list:
                    cell.append(0)
                else:
                    cell.append(self.possibs[3*r0 + i][3*c0 +j])
        return cell
    def getcolpossibs(self,c):
        #this returns a list with a tuple correspoding to each undecided square. The tuple contains the index and the possib list.
        col = []
        for i in range(9):
            if type(self.possibs[i][c]) is list:
                col.append((i,self.possibs[i][c]))
        return col
    def getrowpossibs(self,r):
        row = []
        for i in range(9):
            if type(self.possibs[r][i]) is list:
                row.append((i,self.possibs[r][i]))
        return row
    def getcellpossibs(self,c):
        cell = []
        r0 = c//3
        c0 = c%3
        for i in range(3):
            for j in range(3):
                if type(self.possibs[3*r0 + i][3*c0 +j]) is list:
                    cell.append((3*i+j,self.possibs[3*r0 + i][3*c0 +j]))
        return cell
    def getcolposdict(self,c):
        col = self.getcolpossibs(c)
        colnums = {}
        #collect the total number of each number in dicts
        for square in col:
            for num in square[1]:
                if num in colnums:
                    colnums[num] += 1
                else:
                    colnums[num] = 1
        return colnums
    def getrowposdict(self,r):
        row = self.getrowpossibs(r)
        rownums = {}
        for square in row:
            for num in square[1]:
                if num in rownums:
                    rownums[num] += 1
                else:
                    rownums[num] = 1  
        return rownums
    def getcellposdict(self,c):
        cell = self.getcellpossibs(c)
        cellnums = {}
        for square in cell:
            for num in square[1]:
                if num in cellnums:
                    cellnums[num] += 1
                else:
                    cellnums[num] = 1
        return cellnums
    def haserror(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] != 0 or not(type(self.grid[r][c]) is list):
                    if self.grid[r][c] != self.possibs[r][c]:
                        return True
        for i in range(9):
            col = self.getcol(i)
            row = self.getrow(i)
            cell = self.getcell(i)
            for num in range(1,10):
                if col.count(num) > 1:
                    return True
                if row.count(num) > 1:
                    return True
                if cell.count(num) > 1:
                    return True
        return False
    def printgrid(self):
        for r in range(9):
            if r == 3 or r == 6:
                print('-------------')
            print("|",end="")
            for c in range(9):
                if c == 3 or c == 6:
                    print("|",end="")
                print(self.grid[r][c],end="")
            print("|")
    def printpossibs(self):
        for r in range(9):
            if r == 3 or r == 6:
                print('------------'*3)
            #print("|",end="")
            for subrow in range(3):
                print("|",end="")
                for c in range(9):
                    if c == 3 or c == 6:
                        print("|",end="")
                    for subcol in range(3):
                        if type(self.possibs[r][c]) is int:
                            if subcol == 0 and subrow == 1:
                                s = '-' + str(self.possibs[r][c]) + '-'
                                print(s,end="")
                            elif subrow != 1:
                                print(' ',end="")
                        elif subcol + 1 + 3*(subrow%3) in self.possibs[r][c]:
                            print(subcol + 1 + 3*(subrow%3),end="")
                        else:
                            print(' ',end="")
                    if c != 2 and c != 5 and c != 8:
                        print(' ',end="")
                print("|")
        print()
    def haswon(self):
        haswon = True
        for row in range(9):
            if haswon:
                for col in range(9):
                    if haswon:
                        if type(self.possibs[row][col]) is list:
                            haswon = False
        return haswon

def checkcol(game,colind):
    col = game.getcol(colind)
    nums = []
    for num in col:
        if num != 0:
            nums.append(num)
    for row in range(9):
        if not(type(game.possibs[row][colind]) is int):
            for num in nums:
                if num in game.possibs[row][colind]:
                    game.possibs[row][colind].remove(num)
    return game.possibs

def checkrow(game,rowind):
    row = game.getrow(rowind)
    nums = []
    for num in row:
        if num != 0:
            nums.append(num)
    for col in range(9):
        if not(type(game.possibs[rowind][col]) is int):
            for num in nums:
                if num in game.possibs[rowind][col]:
                    game.possibs[rowind][col].remove(num)
    return game.possibs

def checkcell(game,cellind):
    cell = game.getcell(cellind)
    nums = []
    for num in cell:
        if num != 0:
            nums.append(num)
    for i in range(9):
        if not(type(game.possibs[i//3 + 3*(cellind//3)][i%3 + 3*(cellind%3)]) is int):
            for num in nums:
                if num in game.possibs[i//3 + 3*(cellind//3)][i%3 + 3*(cellind%3)]:
                    game.possibs[i//3 + 3*(cellind//3)][i%3 + 3*(cellind%3)].remove(num)
    return game.possibs

def simplecheck(game):
    #this removes possibs when there is a already its respective number in its row col or cell
    for col in range(9):
        game.possibs = checkcol(game,col)
    for row in range(9):
        game.possibs = checkrow(game,row)
    for cell in range(9):
        game.possibs = checkcell(game,cell)
    return game.possibs

def addints(game):
    #first, we check each square to see if there is only 1 possib
     
    for row in range(9):
        for col in range(9):
            if type(game.possibs[row][col]) is list and len(game.possibs[row][col]) == 1:
                game.possibs[row][col] = game.possibs[row][col][0]
                game.possibs = simplecheck(game)
    #now we check each row, col and cell to see if there are any numbers that can only be in 1 spot
    for i in range(9):
        col = game.getcolpossibs(i)
        colnums = game.getcolposdict(i)
        #collect the total number of each number in dicts
        #search dict for nums that only happen once, and update possibs
        for key in colnums:
            if colnums[key] == 1:
                for square in col:
                    for num in square[1]:
                        if num == key:
                            game.possibs[square[0]][i] = num
                            game.possibs = simplecheck(game)
        row = game.getrowpossibs(i)
        rownums = game.getrowposdict(i)
        for key in rownums:
            if rownums[key] == 1:
                for square in row:
                    for num in square[1]:
                        if num == key:
                            game.possibs[i][square[0]] = num
                            game.possibs = simplecheck(game)

                          
        cell = game.getcellpossibs(i)
        cellnums = game.getcellposdict(i)
        for key in cellnums:
            if cellnums[key] == 1:
                for square in cell:
                    for num in square[1]:
                        if num == key:
                            game.possibs[square[0]//3 + 3*(i//3)][square[0]%3 + 3*(i%3)] = num
                            game.possibs = simplecheck(game)
                            break           
    return game.possibs

def getnuminds(obj,num):
    #given possibs for a col row or cell, this returns the inds of any given num
    output = []
    for ind in range(len(obj)):
        if num in obj[ind][1]:
            output.append(obj[ind][0])
    return output

def hidpair(game):
    for c in range(9):
        col = game.getcolpossibs(c)
        colnums = game.getcolposdict(c)
        if len(colnums) > 3:
            for n in range(2,len(colnums)-1):
                hasn = []
                for num in colnums:
                    if colnums[num] <= n:
                        hasn.append(num)
                if len(hasn) >= n:
                    for i in range(len(hasn)):
                        if colnums[hasn[i]] == n:
                            inds = getnuminds(col,hasn[i])
                            enclosed = []
                            for j in range(len(hasn)):
                                if i != j:
                                    jinds = getnuminds(col,hasn[j])
                                    works = True
                                    for k in jinds:
                                        if not(k in inds):
                                            works = False
                                            break
                                    if works:
                                        enclosed.append(hasn[j])
                            if len(enclosed) == n - 1:
                                for r in inds:
                                    game.possibs[r][c] = [hasn[i]]
                                for numb in enclosed:
                                    for r in getnuminds(col,numb):
                                        game.possibs[r][c].append(numb)
    for r in range(9):
        row = game.getrowpossibs(r)
        rownums = game.getrowposdict(r)
        if len(rownums) > 3:
            for n in range(2,len(rownums)-1):
                hasn = []
                for num in rownums:
                    if rownums[num] <= n:
                        hasn.append(num)
                if len(hasn) >= n:
                    for i in range(len(hasn)):
                        if rownums[hasn[i]] == n:
                            inds = getnuminds(row,hasn[i])
                            enclosed = []
                            for j in range(len(hasn)):
                                if i != j:
                                    jinds = getnuminds(row,hasn[j])
                                    works = True
                                    for k in jinds:
                                        if not(k in inds):
                                            works = False
                                            break
                                    if works:
                                        enclosed.append(hasn[j])
                            if len(enclosed) == n - 1:
                                for c in inds:
                                    game.possibs[r][c] = [hasn[i]]
                                for numb in enclosed:
                                    for c in getnuminds(row,numb):
                                        game.possibs[r][c].append(numb)
    for c in range(9):
        cell = game.getcellpossibs(c)
        cellnums = game.getcellposdict(c)
        if len(cellnums) > 3:
            for n in range(2,len(cellnums)-1):
                hasn = []
                for num in cellnums:
                    if cellnums[num] <= n:
                        hasn.append(num)
                if len(hasn) >= n:
                    for i in range(len(hasn)):
                        if cellnums[hasn[i]] == n:
                            inds = getnuminds(cell,hasn[i])
                            enclosed = []
                            for j in range(len(hasn)):
                                if i != j:
                                    jinds = getnuminds(cell,hasn[j])
                                    works = True
                                    for k in jinds:
                                        if not(k in inds):
                                            works = False
                                            break
                                    if works:
                                        enclosed.append(hasn[j])
                            if len(enclosed) == n-1:
                                for d in inds:
                                    game.possibs[d//3 + 3*(c//3)][d%3 + 3*(c%3)] = [hasn[i]]
                                for numb in enclosed:
                                    for d in getnuminds(cell,numb):
                                        game.possibs[d//3 + 3*(c//3)][d%3 + 3*(c%3)].append(numb)
    for a in range(9):
        for b in range(9):
            if type(game.possibs[a][b]) is list:
                game.possibs[a][b].sort()
    return game.possibs
 
def trivcheck(game):
    old = []
    while old != game.possibs:
        old = copy.deepcopy(game.possibs)
        game.possibs = simplecheck(game)
        game.possibs = addints(game)
        for a in range(9):
            for b in range(9):
                if type(game.possibs[a][b]) is list:
                    #game.printpossibs()
                    return game.possibs
        break
    return game.possibs

def crosscheck(game):
    #this will check if any of the possibilties for a row happen in a single cell, then all other possibs of that nubmer
    #can be removed it also works in reverse if all possibs in cell are in a row
    for c in range(9):
        col = game.getcolpossibs(c)
        colnums = game.getcolposdict(c)
        for num in colnums:
            inds = getnuminds(col,num)
            if len(inds) < 4 and len(inds) > 1:
                insamecell = True
                for ind in inds:
                    if ind//3 != inds[0]//3:
                        insamecell = False
                        break
                if insamecell:
                    cellnum = c//3+3*(inds[0]//3)
                    cell = game.getcellpossibs(cellnum)
                    cellinds = getnuminds(cell,num)
                    if len(cellinds) > len(inds):
                        # game.printpossibs()
                        for cellind in cellinds:
                            game.possibs[cellind//3 + 3*(cellnum//3)][cellind%3 + 3*(cellnum%3)].remove(num)
                        for ind in inds:
                            game.possibs[ind][c].append(num)
                        # game.printpossibs()
                        # print(col,'col',cell)
                        # input(num)

    
    for r in range(9):
        row = game.getrowpossibs(r)
        rownums = game.getrowposdict(r)
        for num in rownums:
            inds = getnuminds(row,num)
            if len(inds) < 4 and len(inds) > 1:
                insamecell = True
                for ind in inds:
                    if ind//3 != inds[0]//3:
                        insamecell = False
                        break
                if insamecell:
                    cellnum = 3*(r//3)+inds[0]//3
                    cell = game.getcellpossibs(cellnum)
                    cellinds = getnuminds(cell,num)
                    if len(cellinds) > len(inds):
                        for cellind in cellinds:
                            game.possibs[cellind//3 + 3*(cellnum//3)][cellind%3 + 3*(cellnum%3)].remove(num)
                        for ind in inds:
                            game.possibs[r][ind].append(num)

    # now we must look at the cells to see if we can eliminate possibs in the col and rows
    for c in range(9):
        cell = game.getcellpossibs(c)
        cellnums = game.getcellposdict(c)
        for num in cellnums:
            inds = getnuminds(cell,num)
            if len(inds) < 4 and len(inds) > 1:
                insamecol = True
                for ind in inds:
                    if ind%3 != inds[0]%3:
                        insamecol = False
                        break
                if insamecol:
                    colnum = 3*(c%3)+inds[0]%3
                    col = game.getcolpossibs(colnum)
                    colinds = getnuminds(col,num)
                    if len(colinds) > len(inds):
                        for colind in colinds:
                            game.possibs[colind][colnum].remove(num)
                        for ind in inds:
                            game.possibs[ind//3 + 3*(c//3)][ind%3 + 3*(c%3)].append(num)
    for c in range(9):
        cell = game.getcellpossibs(c)
        cellnums = game.getcellposdict(c)
        for num in cellnums:
            inds = getnuminds(cell,num)
            if len(inds) < 4 and len(inds) > 1:
                insamerow = True
                for ind in inds:
                    if ind//3 != inds[0]//3:
                        insamerow = False
                        break
                if insamerow:
                    rownum = 3*(c//3)+inds[0]//3
                    row = game.getrowpossibs(rownum)
                    rowinds = getnuminds(row,num)
                    if len(rowinds) > len(inds):
                        # game.printpossibs()
                        for rowind in rowinds:
                            game.possibs[rownum][rowind].remove(num)
                        for ind in inds:
                            game.possibs[ind//3 + 3*(c//3)][ind%3 + 3*(c%3)].append(num)
                        # print(c)
                        # print('rownum',rownum)
                        # print(inds)
                        # print(rowinds)
                        # game.printpossibs()
                        # input(num)  
    for a in range(9):
        for b in range(9):
            if type(game.possibs[a][b]) is list:
                game.possibs[a][b].sort()
    return game.possibs

def guessinggame(old):
    gameog = realcopy(old)
    guesssq = findskinny(board(gameog))
    # input(guesssq)
    poss = gameog[guesssq[0]][guesssq[1]]
    for guess in poss:
        game = realcopy(gameog)
        # game.printpossibs()
        # input('between guess')
        game[guesssq[0]][guesssq[1]] = guess
        # game.printpossibs()
        # input('newguess')
        founderr = False
        old2 = []
        newgame = board(game)
        while not(founderr):
            newgame.possibs = trivcheck(newgame)
            newgame.possibs = hidpair(newgame)
            newgame.possibs = trivcheck(newgame)
            newgame.possibs = crosscheck(newgame)
            newgame.possibs = trivcheck(newgame)
            newgame.printpossibs()
            if newgame.possibs == old2:
                #time to guess:
                newgame.possibs = guessinggame(newgame.possibs)#this may be the trouble
            old2 = copy.deepcopy(newgame.possibs)
            for r in range(9):
                for c in range(9):
                    if type(game[r][c]) is list and 0 == len(game[r][c]):
                        founderr = True
                        break
            if not(founderr) and newgame.haswon():
                return newgame.possibs
    return old

def findskinny(game):
    #this fucntion is meant to find good targets for guessing
    #the idea is that if there is a row, col, or cell that only has two or three squares that have 2 possibs each,
    #they are guarrenteed to at least to switch up the triv check at least a little, hopefully a lot
    #This hopefully prevents a guess only adding the guessed square this tries to guarentee two changed squares.
    out = (0,0,100)# of the form (row,col,sum)
    for i in range(9):
        row = game.getrowpossibs(i)
        if len(row) >0:
            rowsum = 0
            firstnumind = row[0][0]
            for sq in row:
                if type(sq[1]) is list:
                    for n in sq[1]:
                        rowsum += 1
                    # print(i,sq)
                    # input()
            if rowsum == 4:
                return (i,firstnumind,rowsum)
            elif rowsum < out[2] and rowsum != 0:
                out = (i,firstnumind,rowsum)


        col = game.getcolpossibs(i)
        if len(col) >0:
            colsum = 0
            firstnumind = col[0][0]
            for sq in col:
                if type(sq[1]) is list:
                    for n in sq[1]:
                        colsum += 1
            if colsum == 4:
                return (firstnumind,i,colsum)
            elif colsum < out[2] and colsum != 0:
                out = (firstnumind,i,colsum)

        cel = game.getcellpossibs(i)
        if len(cel) >0:
            celsum = 0
            firstnumind = cel[0][0]
            for sq in cel:
                if type(sq[1]) is list:
                    for n in sq[1]:
                        celsum += 1
            if celsum == 4:
                return (firstnumind//3 + 3*(i//3),firstnumind%3 + 3*(i%3),celsum)
            elif celsum < out[2] and celsum != 0:
                out = (i,firstnumind,celsum)
    return out

def realcopy(possibs):
    output = []
    for i in range(9):
        output.append([])
        for j in range(9):
            output[i].append(copy.deepcopy(possibs[i][j]))
    return output

total = 0
for g1 in games:
    game = board(g1)
    old = []
    while not(game.haswon()):
        game.possibs = trivcheck(game)
        game.possibs = hidpair(game)
        game.possibs = trivcheck(game)
        # game.printpossibs()
        game.possibs = crosscheck(game)
        game.possibs = trivcheck(game)
        game.printpossibs()
        if game.possibs == old:
            #time to guess:
            game.possibs = guessinggame(game.possibs)
        old =copy.deepcopy(game.possibs)
        # input()
    if game.haserror():
        print('Error Found')
    else:
        print('No errors found')
    if game.haswon():
        print('HOLY SHIT')
        total += int(str(game.getrow(0)[0])+str(game.getrow(0)[1])+str(game.getrow(0)[2]))
        print(total)