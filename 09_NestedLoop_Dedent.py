n = int(input())
out = []
for i in range(n):
    x = input()
    c = 0
    for ch in x:
        if ch == ".":
            c+=1
        elif ch != ".":
            break
    y = int((c/2))
    out.append(x[y:])
print(*out,sep="\n")