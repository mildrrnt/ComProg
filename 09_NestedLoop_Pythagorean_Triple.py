def gcd(a,b):
    while b!= 0:
        a,b = b,a%b
    return a

def is_coprime(a,b,c):
    if gcd(a,b) == gcd(a,c) == gcd(b,c)== 1 or gcd(a,b) != gcd(a,c):
        return True
    return False

def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(1,max_len+1):
        for b in range(1,c+1):
            if gcd(b,c) != 1: continue
            for a in range(1,b+1):
                if is_coprime(a,b,c):
                    if a**2 + b**2 == c**2:
                        triple.append([a,b,c])
    triple.sort(key=lambda x: (x[2],x[0]))
    return triple

exec(input().strip())