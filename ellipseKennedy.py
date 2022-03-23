
def BresenhemEllipse(rx,ry,cx,cy):
    twoAsqr = 2*rx*rx
    twoBsqr = 2*ry*ry

    x = rx
    y = 0
    xchange = ry*ry*(1-(2*rx))
    ychange = rx*rx
    ellipse_error = 0
    stoppingX = twoBsqr*rx
    stoppingY = 0
    result = []
    temp = []
    
    while(stoppingX >= stoppingY):
        result.append((cx+x, cy+y)) # Q1
        result.append((cx-x, cy+y)) # Q2
        result.append((cx-x, cy-y)) # Q3
        result.append((cx+x, cy-y)) # Q4

        y = y + 1
        stoppingY = stoppingY + twoAsqr
        ellipse_error = ellipse_error + ychange
        ychange = ychange + twoAsqr

        if ((2*ellipse_error + xchange) > 0):
            x = x - 1
            stoppingX -= twoBsqr
            ellipse_error += xchange
            xchange += twoBsqr

    x = 0
    y = ry
    xchange = ry*ry
    ychange = rx*rx*(1-(2*ry))
    ellipse_error = 0
    stoppingX = 0
    stoppingY = twoAsqr*ry

    while(stoppingX <= stoppingY):
        result.append((cx+x, cy+y)) # Q1
        result.append((cx-x, cy+y)) # Q2
        result.append((cx-x, cy-y)) # Q3
        result.append((cx+x, cy-y)) # Q4

        x = x + 1
        stoppingX = stoppingX + twoBsqr
        ellipse_error += xchange
        xchange += twoBsqr

        if ((2*ellipse_error + ychange) > 0):
            y = y - 1
            stoppingY -= twoAsqr
            ellipse_error += ychange
            ychange += twoAsqr

    for i in result:
        if i not in temp:
            temp.append(i)
    return temp

rx,ry,x,y = input('').split()
rx,ry,x,y = int(rx), int(ry), int(x), int(y)

s=BresenhemEllipse(rx,ry,x,y)

for i in s:
    print(i)
