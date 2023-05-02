n = input().split()
l = []
while len(n) > 1:
    a,b = n[0],n[1]
    l.append(set((a,b)))
    n = input().split()

station1 = [{a,b} for (a,b) in l if n[0] in (a,b)]
station2 = []
out = []
for (a,b) in station1:
    for s in l:
        if a in s or b in s:
            station2.append(s)

for (a,b) in station2:
    if a not in out: out.append(a)
    if b not in out: out.append(b)

out.sort()
print("\n".join(out) if out else n[0])