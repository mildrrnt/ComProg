n = int(input())
tel = {}
for i in range(n):
    x = input().split()
    name = " ".join(x[:2])
    num = x[2]
    tel[name] = num
    tel[num] = name
m = int(input())
output = ""
for i in range(m):
    x = input()
    if x in tel:
        output += x+" --> "+tel[x]+"\n"
    else:
        output += x+" --> Not found\n"
print(output)