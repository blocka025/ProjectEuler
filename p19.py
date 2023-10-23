day = 1 #tuesday
month = 1
year = 1901
sundays = 0

while year<=2000:
  if month == 1 or month ==3 or month == 5 or month == 7 or month == 8 or month ==  10:
    if day == 6:
      sundays+=1
    day += 31%7
    day = day%7
    month+=1
    #print(month,day,year)

  elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 6:
      sundays+=1
    day += 30%7
    day = day%7
    month+=1
    #print(month,day,year)

  elif month == 2:
    if day == 6:
      sundays+=1
    if year%4 == 0:
      if not(year%400==0):
        day += 1
        day = day%7
    month+=1
    #print(month,day,year)

  else:
    if day == 6:
      sundays+=1
    day += 31%7
    day = day%7
    month = 1 
    year += 1
    #print(month,day,year)
print(sundays)