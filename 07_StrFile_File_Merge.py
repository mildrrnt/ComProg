x = input().split()

f1 = open(x[0],"r")
f2 = open(x[1],"r")

out = []

def appendf(f):
    for ln in f:
        ln = ln.split()
        out.append([ln[0],ln[1]]) #append each line to list

appendf(f1)
appendf(f2)

out.sort(key = lambda x: (x[0][-2:],x[0])) #sort by last 2 digit and student id
x = [" ".join(i) for i in out]
print(*x, sep="\n")