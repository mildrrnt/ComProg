def knows(R,x,y):
    if y in R[x]: return True
    return False

def is_celeb(R,x):
    names = [k for k,v in R.items()]
    names.remove(x)
    for n in names:
        if not knows(R,n,x):
            return False
    if R[x] == set(x): return True 
    elif R[x] != set(): return False
    return True

def find_celeb(R):
    names = [k for k,v in R.items()]
    celeb = []
    for x in names:
        if is_celeb(R,x): celeb.append(x)
    if len(celeb) == 1: return celeb[0]
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1: break
        if d[0] not in R: R[d[0]] = set()
        if d[1] not in R: R[d[1]] = set()
        R[d[0]].add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())
