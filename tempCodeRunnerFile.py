n = int(input())
li1 = [] #start at L side
li2 = [] #start at R side
for i in range(n+1):
    s = input()
    if s == "Zig-Zag":
        print(min(li1),max(li2)) #min of L, max of R
        break
    elif s == "Zag-Zig":
        print(min(li2),max(li1)) #min of R, max of L
        break
    x = [int(i) for i in s.split()] #convert to int
    if i%2 !=0: #check if the count of line is even or odd
        li1.append(x[0])
        li2.append(x[1])
    else:
        li1.append(x[1])
        li2.append(x[0])