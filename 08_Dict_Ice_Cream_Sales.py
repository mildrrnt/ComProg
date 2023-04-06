n = int(input())
ice = {}
sold = {}
for i in range(n):
    name,price = input().split()
    price = int(price)
    ice[name] = price
m = int(input())
for i in range(m):
    name,amount = input().split()
    amount = int(amount)
    if name in ice:
        if name in sold:
            sold[name] += (amount*ice[name])
        else:
            sold[name] = amount*ice[name]


if sold =={}:
    print("No ice cream sales")
else:
    total = 0.0
    for i in sold:
        total += sold[i]
    mx = max(sold.values())
    top = [k for k,v in sold.items() if v == mx]
    top.sort()
    print("Total ice cream sales:",total)
    print("Top sales:",end = " ")
    print(*top,sep=", ")