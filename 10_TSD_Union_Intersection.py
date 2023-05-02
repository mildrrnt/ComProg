n = int(input())
li = []
for i in range(n):
    li.append(set([int(i) for i in input().split()]))
un,ints = (set(),set()) if len(li)<=0  else (li[0],li[0]) 
for l in li: un,ints  = un|l,ints&l
print(len(un))
print(len(ints))