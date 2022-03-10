import math
# point = [ (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1), 
#         (9,1), (10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), 
#         (10,8), (10,9), (10,10), (9,9), (8,8), (7,7), (6,6), (5,5), (4,4), (3,3), (2,2) ]

point = [(0,0), (20,0), (20,20), (0,20)]

def translation(seq, x, y):
    new_list = []
    for i in range(len(seq)):   
        new_x = 0
        new_y = 0
        new_x = format(seq[i][0] + x, '.3f')
        new_y = format(seq[i][1] + y, '.3f')
        temp = "({0}, {1})".format(new_x,new_y)
        new_list.append(temp)
        temp = 0  
    return new_list

def scaling(seq, x, y, x_ref, y_ref):
    new_list = []
    for i in range(len(seq)):   
        new_x = 0
        new_y = 0
        new_x = format(((seq[i][0] - x_ref) * x) + x_ref, '.3f')
        new_y = format(((seq[i][1] - y_ref) * y) + y_ref, '.3f')
        temp = "({0}, {1})".format(new_x,new_y)
        new_list.append(temp)
        temp = 0  
    return new_list

def rotaition(seq, deg, x_ref, y_ref):
    deg = math.radians(deg)
    new_list = []
    for i in range(len(seq)):   
        new_x = 0
        new_y = 0
        new_x = format((math.cos(deg)*(seq[i][0]-x_ref)) - (math.sin(deg)*(seq[i][1]-y_ref))+x_ref ,".3f")
        new_y = format((math.sin(deg)*(seq[i][0]-x_ref)) + (math.cos(deg)*(seq[i][1]-y_ref))+y_ref ,".3f")
        temp = "({0}, {1})".format(new_x,new_y)
        new_list.append(temp)
        temp = 0  
    return new_list

def mirror(seq, reflec, unit):
    new_list = []
    if reflec==1: # x-axis for mirror
        for i in range(len(seq)):
            new_x = 0
            new_y = 0
            new_x = format(seq[i][0], '.3f')
            new_y = format(seq[i][1]*(-1) + (2*unit), '.3f')
            temp = "({0}, {1})".format(new_x,new_y)
            new_list.append(temp)
            temp = 0    
        return new_list
    elif reflec==2: # y-axis for mirror
        for i in range(len(seq)):
            new_x = 0
            new_y = 0
            new_x = format(seq[i][0]*(-1) + (2*unit), '.3f')
            new_y = format(seq[i][1], '.3f')
            temp = "({0}, {1})".format(new_x,new_y)
            new_list.append(temp)
            temp = 0  
        return new_list
    elif reflec==3:
        deg=math.radians(unit)
        for i in range(len(seq)):
            new_x = 0
            new_y = 0
            new_x = format((seq[i][0]*(math.pow(math.cos(deg),2)-math.pow(math.sin(deg),2))) + (seq[i][1]*(2*math.cos(deg)*math.sin(deg))), '.3f')
            new_y = format((seq[i][0]*(2*math.cos(deg)*math.sin(deg))) + (seq[i][1]*(math.pow(math.sin(deg),2)-math.pow(math.cos(deg),2))), '.3f')
            temp = "({0}, {1})".format(new_x,new_y)
            new_list.append(temp)
        return new_list


choice = int(input(''))
if choice==1:
    # Translation
    x = float(input(''))
    y = float(input(''))
    matrix = translation(point, x, y)
    for i in matrix:
        print(i)
elif choice==2:
    x = float(input(''))
    y = float(input(''))
    x_ref = float(input(''))
    y_ref = float(input(''))
    matrix = scaling(point, x, y, x_ref, y_ref)
    for i in matrix:
        print(i)
elif choice==3:
    deg = int(input(''))
    x_ref = float(input(''))
    y_ref = float(input(''))
    matrix = rotaition(point, deg, x_ref, y_ref)
    for i in matrix:
        print(i)
elif choice==4:
    reflec = int(input(''))
    unit = int(input(''))
    matrix = mirror(point, reflec, unit)
    for i in matrix:
        print(i)