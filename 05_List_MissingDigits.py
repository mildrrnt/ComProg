n = input()
o = []
for i in range(0,10):
    if not str(i) in n:
        o.append(str(i)) #if number is not in string, add that number to list
print(",".join(o) if len(o)!=0 else "None") #if output list is not empty, turn list to string w/ join "," else print None