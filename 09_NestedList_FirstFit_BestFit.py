def first_fit(L,e):
    for i in range(len(L)):
        if sum(L[i])+e<= 100:
            L[i].append(e)
            return L
    L.append([e])
    return L

def best_fit(L,e):
    c = 0
    p = -1
    for i in range(len(L)):
        if e + sum(L[i]) <= 100 and c < (e + sum(L[i])):
            p = i
            c = e + sum(L[i])
    if p == -1:
        L.append([e])
    else: L[p].append(e)
    return L

def partition_FF(D):
    L = []
    for i in D:
        if not L:
            L.append([i])
        else:
            first_fit(L,i)
    return L

def partition_BF(D):
    L = []
    for i in D:
        if not L:
            L.append([i])
        else:
            best_fit(L,i)
    return L

exec(input().strip())