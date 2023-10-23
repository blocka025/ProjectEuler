"""
one 3
two 3
three 5
four 4
five 4
six 3
seven 5
eight 5
nine 4
ten 3
eleven 6
twelve 6
thirteen 8
fourteen 8
fifteen 7
sixteen 7
seventeen 9
eighteen 8
nineteen 8
twenty 6
thirty 6
forty 5
fifty 5
sixty 5
seventy 7
eighty 6
ninety 6
hundred 7
one thousand 11
"""
first19 = 3+3+5+4+4+3+5+5+4+3+6+6+8+8+7+7+9+8+8
print(first19)
n1_9 = 3+3+5+4+4+3+5+5+4
print(n1_9)
first99 = first19 + 10*(6+6+5+5+5+7+6+6) + 8*n1_9
print(first99)
print(11+n1_9*100+10*99*9+7*9+first99*10)
