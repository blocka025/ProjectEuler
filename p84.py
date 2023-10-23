import random
keys = range(1,11)
vals = [0,10,11,24,39,5,'R','R','U','-3']
CH = dict(zip(keys,vals))

def diceroll(sides):
    return random.randint(1,sides)
def getCC():
    card = random.randint(1,16)
    if card == 1:
        return 10
    elif card == 2:
        return 0
    return "No Move"

def getCH():
    card = random.randint(1,16)
    if card < 11:
        return CH[card]
    return "No Move"

class player():
    def __init__(self):
        self.squarecount = 40*[0]
        self.space = 0
        self.dicesides = 4
        self.doublecount = 0
    def roll(self):
        die1 = diceroll(self.dicesides)
        die2 = diceroll(self.dicesides)
        if die1 == die2:
            self.doublecount += 1
        else:
            self.doublecount = 0
        return die1 + die2
        
    def move(self):
        self.space = (self.space + self.roll())%40
        if self.doublecount == 3:# if roll 3 dubs in a row go 2 jail
            self.space = 10
            self.doublecount = 0
            
        else:    
            if self.space == 2 or self.space == 17 or self.space == 33:
                #if space is Community Chest
                card = getCC()
                if card != 'No Move':
                    self.space = int(card)
                    
            elif self.space == 7 or self.space == 22 or self.space == 36:
                #if space is Chance
                card = getCH()
                if card != 'No Move':
                    if type(card) == type(0):
                        self.space = card
                    elif card == 'R':
                        self.space +=1
                        while 1:
                            self.space = self.space%40
                            if self.space == 5 or self.space == 15 or self.space == 25 or self.space == 35:
                                break
                            self.space += 1
                    elif card == '-3':
                        self.space -= 3
                    else:
                        if self.space > 11 and self.space < 28:
                            self.space = 28
                        else:
                            self.space = 12
                
            if self.space == 30:
                # the space is go 2 jail
                self.space = 10
        self.squarecount[self.space] += 1

player1 = player()

for n in range(1000000):
    player1.move()
"""total = 0
for ele in player1.squarecount:
    total += ele
for i in range(len(player1.squarecount)):
    player1.squarecount[i] = player1.squarecount[i]/total"""

for n in range(3):
    i =player1.squarecount.index(max(player1.squarecount))
    print(i,end="")
    player1.squarecount[i] = 0
    