def reverse(d):
    rd = {}
    for k in d:
        rd[d[k]] = k
    return rd

def keys(d,v):
    li = []
    for k in d:
        if d[k] == v:
            li.append(k)
    return li

exec(input().strip())