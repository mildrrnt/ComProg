n = int(input())
o = [str(n)] #put first n in the list as string
while n != 1:
    if n%2 == 0:
        n = round(n/2)
    else:
        n = 3*n+1
    o.append(str(n))
print("->".join(o) if len(o)<= 15 else "->".join(o[-15:]))
#join each element in list, seperated by ->