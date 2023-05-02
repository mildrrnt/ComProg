def factor(N):
    i = 2
    c = 0
    out = []
    while N > 1:
        while N % i == 0:
            c += 1
            N /= i
        if c!= 0:
            out.append([i,c])
        i += 1
        c = 0
    return out
exec(input().strip())