def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:
            return i
def flatten(t):
    ilist = [j for i in t for j in i]
    ilist.remove(0)
    return ilist
def inversions(x):
    lists = []
    count = 0
    for i in range(len(x)-1):
        for j in range(i,len(x)):
            if i != j:
                lists.append((x[i],x[j]))
    for a,b in lists:
        if a>b:
            count += 1
    return count
def solvable(t):
    x = flatten(t)
    if len(t)%2 != 0 and inversions(x)%2==0:
        return True
    elif len(t)%2 == 0 and \
        ((inversions(x)%2 != 0 and row_number(t,0)%2 == 0) or\
        (inversions(x)%2 == 0 and row_number(t,0)%2 != 0)):
        return True
    return False

exec(input().strip())