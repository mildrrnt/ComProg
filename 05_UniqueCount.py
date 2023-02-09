li = [int(i) for i in input().split()]
li.sort()
v = []
for i in range(len(li)):
    if li[i] != li[i-1]: #check with index to the left
        v.append(li[i])
v.sort()
print(len(v))
print(v if len(v)<= 10 else v[:10])