#frames = [float(x) for x in input().split()]

frames=[1.0, 4.0, 1.5, 2.0, 2.0, 5.0, 2.5, 2.0, 4.0, 5.5, 1.5, 3.5, 6.0, 4.5, 1.5, 2.0]

def getInfo(i): #=x,y,w,h of the selected frame
  x,y,w,h = frames[(i-1)*4],frames[(i-1)*4+1],frames[(i-1)*4+2],frames[(i-1)*4+3]
  return(x,y,w,h)

def getArea(i): #area of the selected frame
  w,h = frames[(i-1)*4+2],frames[(i-1)*4+3]
  return w*h


def centr(i): #the centroid of the selected frame
  x,y,w,h = getInfo(i) #call getInfo function for x,y,w,h values
  x,y = x+(w/2),y-(h/2) #find coordinates of the centroid
  return x,y

def dist(f1,f2): #the distance between the selected frames
  x1,y1 = centr(f1) #for centroid of f1
  x2,y2 = centr(f2)
  d = abs((x2-x1)**2+(y2-y1)**2)**(1/2) #from c^2 = a^2+b^2
  return d

def interst(f1,f2): #the area of intersection between selected frames
  x1,y1,w1,h1 = getInfo(f1)
  x2,y2,w2,h2 = getInfo(f2)
  x3 = max(x1,x2) #compare the coordinate of upper left corner, use the max value to create the left line of the rectangle area
  y3 = min(y1,y2) #use the min value to create the lower line of the rectangle area
  x4 = min(x1+w1,x2+w2) #compate the coordinate of the lower right corner, use the min value to create the right line of the rectangle area
  y4 = max(y1-h1,y2-h2) #use the max value to create the upper line of the rectangle area
  area = (x4-x3)*(y3-y4) # a = w*h 
  if area > 0:
    return area
  else: #area < 0 means that there is no intersection
    return 0.0

def union(f1,f2): #the area of the union of the selected frames
  a1 = getArea(f1)
  a2 = getArea(f2)
  area = a1+a2-interst(f1,f2) #sum of area of two frames - intersection area
  return area

def iou(f1,f2): #ratio between intersection and union
  ia = interst(f1,f2)
  ua = union(f1,f2)
  return ia/ua

i = input()
out = []
while i != "end": #loop until input = end
  li = i.split()
  if li[0] == "center":
    out.append(", ".join(map(str,(centr(int(li[1]))))))
    #the function returns type tuple, convert them to string using map, then using join to turn it into str and append to list
  elif li[0] == "distance":
    out.append(dist(int(li[1]),int(li[2])))
    #appends the value to list
  elif li[0] == "intersection":
    out.append(interst(int(li[1]),int(li[2])))
  elif li[0] == "union":
    out.append(union(int(li[1]),int(li[2])))
  else:
    out.append(iou(int(li[1]),int(li[2])))
  i = input()
print(*out,sep="\n") #print each member of the list, seperated by new line