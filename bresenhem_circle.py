def BresenhemCircle(x,y,r):
    xc = 0
    yc = r
    h = 1-r
    dU = 0
    dD = 0
    result = []
    temp = []
    p1,p5,p3,p2,p7,p8,p6,p4 = [],[],[],[],[],[],[],[]
    
    temp2 = []
    choose='point one'

    temp2.append((h,xc, yc,choose))

    while (xc<=yc):

        p1.append((xc+x, yc+y)) # (x,y) P1
        p2.append((yc+x, xc+y)) # (y,x) P2
        p7.append((yc+x, -xc+y)) # (y,-x) P7
        p8.append((xc+x, -yc+y)) # (x,-y) P8 
        p5.append((-xc+x, -yc+y)) # (-x,-y) P5
        p6.append((-yc+x, -xc+y)) # (-y,-x) P6
        p3.append((-yc+x, xc+y)) # (-y,x) P3
        p4.append((-xc+x, yc+y)) # (-x,y) P4 

        if h < 0:
            # xc += 1
            dU = (2*xc)+3
            h = h + dU
            choose = 'U'
        else:
            # xc += 1
            # yc -= 1
            dD = (2*(xc-yc)) + 5
            h = h + dD
            yc -= 1
            choose = 'D'
        xc += 1
        
        temp2.append((xc, yc, choose))

    p2.reverse()
    p4.reverse()
    p6.reverse()
    p8.reverse()

    result.extend(p1)
    result.extend(p2)
    result.extend(p7)
    result.extend(p8)
    result.extend(p5)
    result.extend(p6)
    result.extend(p3)
    result.extend(p4)

    for i in result:
        if i not in temp:
            temp.append(i)
        
    return temp,temp2,p1,p2,p3,p4,p5,p6,p7,p8

x, y, r= input('').split()
x, y, r = int(x), int(y), int(r)

s,v,p1,p2,p3,p4,p5,p6,p7,p8 = BresenhemCircle(x, y, r)
for i in s:
    print(i)

print(len(s))

print('-------------')

print('xc, yc, choose')
for j in v:
    print(j)
print('-------------')

for a in p1:
    print('o1', a)
for b in p2:
    print('o2', b)
for c in p3:
    print('o3', c)
for d in p4:
    print('o4', d)
for e in p5:
    print('o5', e)
for f in p6:
    print('o6', f)
for g in p7:
    print('o7', g)
for h in p8:
    print('o8', h)

