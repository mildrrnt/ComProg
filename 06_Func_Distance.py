def distance1(x1,y1,x2,y2):
    d1 = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return d1

def distance2(p1,p2):
    p = p1+p2
    d2 = distance1(p[0],p[1],p[2],p[3])
    return d2

def distance3(c1,c2):
    d3 = distance2(c1[:-1],c2[:-1]) #list of the first two indices
    if d3 <= (c1[-1]+c2[-1]): #overlap if the distance between two points are less than or equal to sum of the radius
        overlap = True
    else:
        overlap = False
    return d3, overlap

def perimeter(points):
    p = 0
    for i in range(len(points)): #repeat the step k time; k = number of side
        p+= distance2(points[i-1],points[i])
    return p

exec(input().strip())