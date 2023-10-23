count = 0
bound = 50 + 1
for py in range(1,bound):
    for px in range(0,bound):
        for qy in range(0,bound):
            if py>=qy:
                for qx in range(0,bound):
                    if px<=qx:
                        a = (px**2 + py**2)**.5
                        b = (qx**2 + qy**2)**.5
                        c = ((px-qx)**2 + (py-qy)**2)**.5
                        sidelengths = [a,b,c]
                        sidelengths.sort()
                        if abs(sidelengths[0]**2 + sidelengths[1]**2 - sidelengths[2]**2) <1e-9 and sidelengths[0] != 0:
                            count+= 1
print(count)