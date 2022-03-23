def BresenhamLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    m = (y2-y1)/(x2-x1)
    m = round(m,3)
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    rdx = dx
    rdy = dy

    dx = abs(dx)
    dy = abs(dy)
    string = []
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
        print('dx>dy')
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
        print('dx<dy and swap dx,dy')

    D = 2*dy - dx
    print('D=',D)
    y = 0
    print('xsign =',xsign,',ysign =',ysign,',m =',m,',dx =',dx,',dy =',dy)
    print('xx =',xx,',xy =',xy,',yx =',yx,',yy =',yy)
    print('-------------')
    print('x, y, D, choose')
    choose = 'point one'
    for x in range(dx + 1):
        string.append((x1 + x*xx + y*yx,y1 + x*xy + y*yy,D,choose))
        if D >= 0:
            y += 1
            D -= 2*dx
            choose = 'U'
        else:
            choose = 'D'
        D += 2*dy
    return string
    
x1, y1, x2, y2 = input('').split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
s = BresenhamLine(x1,y1,x2,y2)
for i in s:
    print(i)
