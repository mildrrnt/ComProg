n = input().lower()
al = "abcdefghijklmnopqrstuvwxyz"
d = {}
li = []

for i in al:
    c = n.count(i)
    if c != 0:
        d[i] = c
for i in d:
    li.append([-d[i],i])
li.sort()
for a,b in li:
    print(b,"->",-a)