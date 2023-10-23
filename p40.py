s = ""
n = 0
for num in range(1,1000001):
  s += str(num)
  n += len(str(num))
print(int(s[0])*int(s[9])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])*int(s[999999]))