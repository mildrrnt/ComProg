c= input().split()
o = input()
h = len(c)//2

for n in o:
    if n == "C":
        c = c[h:]+c[:h]
    elif n == "S":
        c[::2],c[1::2] = c[:h],c[h:]
print(" ".join(c))