f = open("ProjectEuler/p102_tri.txt", "r")
coords = []
for line in f:
  coords.append(line.strip().split(","))
f.close()
# print(coords)

def is_above_line(x1,y1,x2,y2,xtest,ytest):
    if x1 == x2:
        if xtest>0:
            return True
        else:
            return False
    else:
        m = (y2-y1)/(x2-x1)
        if ytest > m *(xtest-x1)+y1:
            return True
        else:
            return False

#first test if origin is on any line
total = 0
for points in coords:
    x1 = int(points[0])
    y1 = int(points[1])
    x2 = int(points[2])
    y2 = int(points[3])
    x3 = int(points[4])
    y3 = int(points[5])
    if (x1 == x2 and x1==0) or (x2 == x3 and x2==0) or (x1 == x3 and x1==0):
        total += 1
    elif x1 != x2 and x2 != x3 and x1 != x3:
        m1 = (y2-y1)/(x2-x1)
        m2 = (y3-y1)/(x3-x1)
        m3 = (y3-y2)/(x3-x2)
        if m1*x1 == y1 or m2*x1 == y1 or m3*x2 == y2:
            total += 1
        else:
            if is_above_line(x1,y1,x2,y2,0,0) == is_above_line(x1,y1,x2,y2,x3,y3):
                if is_above_line(x1,y1,x3,y3,0,0) == is_above_line(x1,y1,x3,y3,x2,y2):
                    if is_above_line(x3,y3,x2,y2,0,0) == is_above_line(x3,y3,x2,y2,x1,y1):
                        total += 1
    else:
        if is_above_line(x1,y1,x2,y2,0,0) == is_above_line(x1,y1,x2,y2,x3,y3):
            if is_above_line(x1,y1,x3,y3,0,0) == is_above_line(x1,y1,x3,y3,x2,y2):
                if is_above_line(x3,y3,x2,y2,0,0) == is_above_line(x3,y3,x2,y2,x1,y1):
                    total += 1
print(total)