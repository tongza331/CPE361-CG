import math

xref1 = 250 
yref1 = 250
xref2 = 750
yref2 = 950

# get two line point
x1, y1, x2, y2 = input('').split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

# find four bits
fpoint1 = []
fpoint2 = []

fpoint1.insert(0,1) if y1-yref2 > 0 else fpoint1.insert(0,0) # top
fpoint2.insert(0,1) if y2-yref2 > 0 else fpoint2.insert(0,0) 

fpoint1.insert(1,1) if y1-yref1 < 0 else fpoint1.insert(1,0) # bottom
fpoint2.insert(1,1) if y2-yref1 < 0 else fpoint2.insert(1,0) 

fpoint1.insert(2,1) if x1-xref2 > 0 else fpoint1.insert(2,0) # right
fpoint2.insert(2,1) if x2-xref2 > 0 else fpoint2.insert(2,0) 

fpoint1.insert(3,1) if x1-xref1 < 0 else fpoint1.insert(3,0) # left
fpoint2.insert(3,1) if x2-xref1 < 0 else fpoint2.insert(3,0) 

# print four bit point
print(*fpoint1) 
print(*fpoint2)

def top_bound(m,x,y):
    return x+((yref2-y)/m) # x3
def bottom_bound(m,x,y):
    return x+((yref1-y)/m) # x3
def right_bound(m,x,y):
    return y+(m*(xref2-x)) # y3
def left_bound(m,x,y):
    return y+(m*(xref1-x)) #y3

def x_check(x):
    if x>xref2:
        return xref2
    else:
        return xref1
        
def y_check(y):
    if y>yref2:
        return yref2
    else:
        return yref1

def find_intersect(m,x,y,fpoint,xref1,yref1,xref2,yref2): # x_min, y_min, x_max, y_max
    x3=0
    y3=0
    if fpoint == [0,0,0,0]:
        return x3,y3
    elif fpoint == [0,0,1,0]:
        # bound right
        y3 = right_bound(m,x,y)
        x3 = x_check(x)
        return x3,y3
    elif fpoint == [1,0,0,1]:
        # bound top, left
        x3 = top_bound(m,x,y)
        y3 = left_bound(m,x,y)
        return x3,y3
    elif fpoint == [1,0,0,0]:
        # bound top
        x3 = top_bound(m,x,y)
        y3 = y_check(y)
        return x3,y3
    elif fpoint == [1,0,1,0]:
        # bound top right
        x3 = top_bound(m,x,y)
        y3 = right_bound(m,x,y)
        return x3,y3
    elif fpoint == [0,0,0,1]:
        # bound left
        y3 = left_bound(m,x,y)
        x3 = x_check(x)
        return x3,y3
    elif fpoint == [0,1,0,1]:
        # bound bottom, left
        x3 = bottom_bound(m,x,y)
        if y<yref1:
            y3=yref1
        else:
            y3 = right_bound(m,x,y)
        return x3,y3
    elif fpoint == [0,1,0,0]:
        # bound bottom
        x3 = bottom_bound(m,x,y)
        y3 = y_check(y)
        return x3,y3
    elif fpoint == [0,1,1,0]:
        # bound bottom, right
        x3 = bottom_bound(m,x,y)
        y3 = right_bound(m,x,y)
        return x3,y3


# check category 
# def category():
temp_list = []
if fpoint1 and fpoint2 == [0,0,0,0]: 
    print("Visible")
    print("({0:.3f}, {1:.3f})".format(x1,y1))
    print("({0:.3f}, {1:.3f})".format(x2,y2))
else:
    for i,j in zip(fpoint1, fpoint2):
        b = i&j
        temp_list.append(b)
    if temp_list != [0,0,0,0]:
        print("Invisible")
    else:
        m = (y2-y1)/(x2-x1)
        x31,y31 = find_intersect(m,x1,y1,fpoint1,xref1,yref1,xref2,yref2)
        x32,y32 = find_intersect(m,x2,y2,fpoint2,xref1,yref1,xref2,yref2)
        print(m)
        if ((x31<xref1 or y31>yref2) and (x32<xref1 or y32>yref2))==True:
            print("Invisible")
            print("({0:.3f}, {1:.3f})".format(x31,y31))
            print("({0:.3f}, {1:.3f})".format(x32,y32))
        else:
            print("Clipping Candidate")
            print("({0:.3f}, {1:.3f})".format(x31,y31))
            print("({0:.3f}, {1:.3f})".format(x32,y32))



        
        
