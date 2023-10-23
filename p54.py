class Hand():
  def __init__(self,cards):
    self.cards = cards
    self.score = self.get_score()

  def is_royal(self):
    if not(self.is_flush()):
      return False
    vals = []
    for card in self.cards:
      vals.append(card[0])
    vals.sort()
    if vals == ["A","J","K","T","Q"]:
      return True
    else:
      return False

  def is_str_flush(self):
    if self.is_flush() and self.is_str():
      return True
    else:
      return False

  def is_flush(self):
    for card in self.cards:
      if self.cards[0][1] != card[1]:
        return False
    return True

  def is_str(self):
    vals = []
    for card in self.cards:
      vals.append(card[0])
    vals.sort()
    if vals == ["A","J","K","T","Q"] or vals == ["9","J","K","T","Q"] or vals == ["8","9","J","T","Q"] or vals == ["7","8","9","J","T"] or vals == ["6","7","8","9","T"] or vals == ["5","6","7","8","9"] or vals == ["4","5","6","7","8"] or vals == ["3","4","5","6","7"] or vals == ["2","3","4","5","6"] or vals == ["2","3","4","5","A"]:
      return True
    else:
      return False

  def is_four(self):
    vals = []
    for card in self.cards:
      vals.append(card[0])
    for val in vals:
      if vals.count(val) == 4:
        self.pair_val = val
        return True
    return False

  def is_full(self):
    vals = []
    for card in self.cards:
      vals.append(card[0])
    vals.sort()
    if (vals.count(vals[0]) == 2 and vals.count(vals[0]) == 3) or (vals.count(vals[0]) == 3 and vals.count(vals[0]) == 2):
      return True
    else:
      return False
  
  def is_three(self):
    vals = []
    for card in self.cards:
      vals.append(card[0])
    for val in vals:
      if vals.count(val) == 3:
        self.pair_val = val
        return True
    return False

  def is_two_pair(self):
    if self.is_pair():
      vals = []
      for card in self.cards:
        if card[0] != self.pair_val:
          vals.append(card[0])
      for val in vals:
        if vals.count(val) == 2:
          if val > self.pair_val:
            self.pair_val = val
          return True
    return False

  def is_pair(self):
    vals = []
    for card in self.cards:
      vals.append(card[0])
    for val in vals:
      if vals.count(val) == 2:
        self.pair_val = val
        #print(val)
        return True
    return False
  
  def get_high(self):
    output = []
    vals = []
    for card in self.cards:
      vals.append(card[0])
    for val in vals:
      if val == "A":
        output.append(val)
    for val in vals:
      if val == "K":
        output.append(val)
    for val in vals:
      if val == "Q":
        output.append(val)
    for val in vals:
      if val == "J":
        output.append(val)
    for val in vals:
      if val == "T":
        output.append(val)
    for val in vals:
      if val == "9":
        output.append(val)
    for val in vals:
      if val == "8":
        output.append(val)
    for val in vals:
      if val == "7":
        output.append(val)
    for val in vals:
      if val == "6":
        output.append(val)
    for val in vals:
      if val == "5":
        output.append(val)
    for val in vals:
      if val == "4":
        output.append(val)
    for val in vals:
      if val == "3":
        output.append(val)
    for val in vals:
      if val == "2":
        output.append(val)
    #print(output)
    return output

  def get_score(self):
    self.highs = self.get_high()
    if self.is_royal():
      return 0
    elif self.is_str_flush():
      return 1
    elif self.is_four():
      return 2
    elif self.is_full():
      return 3
    elif self.is_flush():
      return 4
    elif self.is_str():
      return 5
    elif self.is_three():
      return 6
    elif self.is_two_pair():
      return 7
    elif self.is_pair():
      return 8
    else:
      return 9


order = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
hands = []
f = open("p54_hands.txt", "r")
for line in f:
  line1 = line.strip()
  hands.append(line1.split(" "))
f.close()
#print(hands)
p1_wins = 0
p = 0
for hand in hands:
  win = False
  p1_hand = Hand(hand[:5])
  p2_hand = Hand(hand[5:])
  if p1_hand.score < p2_hand.score:
    p1_wins += 1
    win = True
  elif p1_hand.score == p2_hand.score and p1_hand.score <= 8:
    #print(p1_hand.cards,p2_hand.cards,p1_hand.score,p2_hand.score)
    if order.index(p1_hand.pair_val) < order.index(p2_hand.pair_val):
      p1_wins += 1 
      win = True

    #checked
    elif order.index(p1_hand.pair_val) == order.index(p2_hand.pair_val):
      for i in range(5):
        if order.index(p1_hand.highs[i])<order.index(p2_hand.highs[i]):
          p1_wins += 1
          win = True
          if i>0:
            print(p1_hand.cards,p2_hand.cards,p1_hand.score,p2_hand.score,)
          break
        elif order.index(p1_hand.highs[i])>order.index(p2_hand.highs[i]):
          break


  elif p1_hand.score == p2_hand.score and p1_hand.score == 9:
    for i in range(5):
      if order.index(p1_hand.highs[i])<order.index(p2_hand.highs[i]):
        #print(order.index(p1_hand.highs[i]),order.index(p2_hand.highs[i]))
        p1_wins += 1
        win = True
        if i>0:
          print(p1_hand.cards,p2_hand.cards,p1_hand.score,p2_hand.score)
        break
      elif order.index(p1_hand.highs[i])>order.index(p2_hand.highs[i]):
        break
  if p1_hand.score <= 5 or p1_hand.score <= 5:
    print(p1_hand.cards,p2_hand.cards,p1_hand.score,p2_hand.score)
print(p1_wins)  