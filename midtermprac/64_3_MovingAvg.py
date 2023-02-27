n = [float(i) for i in input().split()]
size = int(n[0])
n = n[1:]
out = []

for i in range(len(n)):
    x = n[i:i+size]
    avg = round((sum(x)/len(x)),1)
    out.append(str(avg))

print(" ".join(out))