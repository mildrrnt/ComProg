L = [[90,5],[50],[70,10]]
D = [50,90,10,80,50,20]

def first_fit(L,e):
    nL = L
    for i in range(len(nL)):
        if sum(nL[i])+e<= 100:
            nL[i].append(e)
            break
    return nL

def best_fit(L,e):
    nL = L
    x = [sum(i)+e for i in nL]
    for i in range(len(x)):
        if x[i] > 100:
            x[i]=-999
    ii = x.index(max(x))
    nL[ii].append(e)
    return nL
'''

'''
def partition_FF(D):
    x = [[D[0]]]
    for i in range(1,len(D)+1):
        x.append(first_fit(x,D[i]))
    return x


print(partition_FF(D))