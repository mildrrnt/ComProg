def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c,A):
    m = []
    for n in range(len(A)):
            m.append([round(float(A[n][i])*c,1) for i in range(len(A[n]))])
    return m

def mult(A,B):
    m = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            ele = 0
            for k in range(len(B)):
                ele += A[i][k]*B[k][j]
            row.append(ele)
        m.append(row)
    return m
exec(input().strip())