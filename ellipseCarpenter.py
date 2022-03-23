def midpointEllipse(rx, ry, xc, yc):
    x = 0
    y = ry
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    result = []
    temp = []
    while (dx < dy):

        result.append((xc+x, yc+y)) # Q1
        result.append((xc-x, yc+y)) # Q2
        result.append((xc-x, yc-y)) # Q3
        result.append((xc+x, yc-y)) # Q4

        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
           (rx * rx * ry * ry))

    while (y >= 0):
        
        result.append((xc+x, yc+y)) # Q1
        result.append((xc-x, yc+y)) # Q2
        result.append((xc-x, yc-y)) # Q3
        result.append((xc+x, yc-y)) # Q4

        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)

    for i in result:
        if i not in temp:
            temp.append(i)
    return temp

rx, ry, xc, yc = input('').split()
rx, ry, xc, yc = int(rx), int(ry), int(xc), int(yc)
s=midpointEllipse(rx, ry, xc, yc)

for i in s:
    print(i)


 