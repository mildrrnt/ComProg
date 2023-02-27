x = [ch for ch in input().replace(" ","").lower()] #remove space, lowercase all
y = [ch for ch in input().replace(" ","").lower()]
x.sort() #sort in order
y.sort()
if x==y:
    print("YES")
else:
    print("NO")