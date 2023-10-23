def add2theninvserse(numer, denom):
  new_numer = numer + (2 * denom)
  return (denom,new_numer)
top = 1
bot = 2
total = 0
for num in range(999):
  new_fract = add2theninvserse(top,bot)
  bot = new_fract[1]
  top = new_fract[0]
  final_top = top+bot
  if len(str(final_top))>len(str(bot)):
    total += 1
print(total)