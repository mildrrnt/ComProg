n = int(input())
l = []
for i in range(n):
    coor = [float(i) for i in input().split()]
    d = (coor[0]**2 + coor[1]**2)**(1/2)
    l += [(d,i+1,coor[0],coor[1])] #add lists to list
l = sorted(l) #sort list by index 0 of lists inside
print("#%s: (%s, %s)"%(l[2][1],l[2][2],l[2][3])) #id,coor x, coor y of the third closest