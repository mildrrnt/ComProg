def total(pocket):
    t = 0
    for bank,amount in pocket.items():
        t += bank*amount
    return t

def take(pocket,money):
    p = pocket
    for bank,amount in money.items():
        if bank in p:
            p[bank] += amount
        else:
            p[bank] = amount
    return p

def pay(pocket,amt):
    out = {}
    for b in sorted(pocket)[::-1]:
        if amt >= b:
            c = min(pocket[b],amt//b)
            out[b] = c
            pocket[b] -= c
            amt -= b*c
    if amt > 0:
        take(pocket,out)
        out = {}
    return out

exec(input().strip())