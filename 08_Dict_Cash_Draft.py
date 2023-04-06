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
    p = dict(pocket)
    t = total(pocket)
    z = amt
    if t < amt:
        return {}
    else:
        for bank,amount in p.items():
            if bank > amt or bank > z:
                continue
            else:
                if bank*amount >= z:
                    b = amt//bank
                else:
                    b = amount
                used = b*bank
                z -= used
                if z > 0:
                    out[bank] = b
                else:
                    out[bank] = amt+z
        if total(out) < amt:
            print("this")
            print(total(out))
            return {}
        for bank,amount in pocket.items():
            if bank in out:
                pocket[bank] = amount-out[bank]
            else:
                pocket[bank] = amount
        return out

exec(input().strip())