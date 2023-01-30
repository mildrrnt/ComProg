s = input()
o = ""
for d in s:
    if d =="(":
        o += "[" 
    elif d =="[":
        o += "("
    elif d ==")":
        o += "]"
    elif d =="]":
        o += ")"
    else:
        o += d
print(o)