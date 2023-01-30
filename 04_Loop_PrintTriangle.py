h = int(input())
b = int(2*h-1)

print((" "*int(b/2))+"*")
if h > 2:
    space = 1
    for i in range(2,h):
        print((" "*(h-i))+"*"+" "*(space)+"*")
        space += 2
print("*"*b)