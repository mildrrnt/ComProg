dept = {}
stu = []

for i in range(int(input())):
    d = input().split()
    d[1] = int(d[1])
    dept[d[0]] = d[1]

for i in range(int(input())):
    s = input().split()
    stu.append(s)

stu.sort(key=lambda x: float(x[1]),reverse=True)
out = []
for n in stu:
    id = n[0]
    major = n[2:]
    for m in major:
        if dept[m] != 0:
            dept[m] -= 1
            out.append([id,m])
            break
        else:
            continue
out.sort(key=lambda x: x[0])
for id,m in out:
    print(id,m)