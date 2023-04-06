n = int(input())
d = {}
for i in range(n):
    nick,name = input().split()
    d[nick] = name
    d[name] = nick
m = int(input())
out = []
for i in range(m):
    name = input()
    if name in d:
        out.append(d[name])
    else:
        out.append("Not found")
print(*out,sep="\n")