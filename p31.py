count = 1
for a in range(3):
  for b in range(5):
    for c in range(11):
      for d in range(21):
        for e in range(41):
          for f in range(101):
            for g in range(201):
              if 100*a+50*b+20*c+10*d+5*e+2*f+g == 200:
                count += 1
              elif 100*a+50*b+20*c+10*d+5*e+2*f+g > 200:
                break
print(count)