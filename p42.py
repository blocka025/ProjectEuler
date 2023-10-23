alphabet = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
f = open("p42_words.txt", "r")
for line in f:
  words = line.split(',')
f.close()
longest = 0
for i, word in enumerate(words):
  words[i] = word[1:-1]
  if len(word)>longest:
    longest = len(word)
tris = []
n = 1
while longest*26 > .5*n*(n+1):
  tris.append(.5*n*(n+1))
  n+=1
count = 0
for word in words:
  total = 0
  for letter in word:
    total += alphabet[letter.lower()]
  if total in tris:
    count += 1
print(count)