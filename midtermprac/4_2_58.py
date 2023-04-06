a = [int(i) for i in input().split()]
det = a[0]*a[3] - a[1]*a[2]
b = [a[3],-a[1],-a[2],a[0]]
b = [round((i/det),1) for i in b if det!= 0]

def mat(b):
    if b == []:
        print(0.0)
        return None
    mat =[b[:2],b[2:]]
    for n,m in mat:
        print("[%s %s]"%(n,m))
mat(b)