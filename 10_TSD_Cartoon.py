n = input().split(", ")
d = {}
animal = []

while n[0] != "q":
    name,type = n
    if type in d:
        d[type].append(name)
    else:
        d[type] = [name]
        animal.append(type)
    n = input().split(", ")

for a in animal:
    print(a,end=": ")
    print(", ".join(d[a]))