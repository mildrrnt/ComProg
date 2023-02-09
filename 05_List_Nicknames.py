fn = ["Robert","William","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
nn = ["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
n = int(input())
o = ""
for i in range(n):
    s = input()
    if s in fn:
        o += nn[fn.index(s)] +"\n" #add to output if found
    elif s in nn:
        o += fn[nn.index(s)] +"\n"
    else:
        o += "Not found\n"
print(o)