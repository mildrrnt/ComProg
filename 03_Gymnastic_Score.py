s = [float(f) for f in (input()).split()]

max = 0
min = 10

for i in s:
    if i > max:
        max = i
    if i < min:
        min = i

print(round(((sum(s)-max-min)/2),2))