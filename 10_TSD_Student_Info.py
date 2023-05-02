student = [input().split() for i in range(int(input()))]
group = set(input().split())
out = sorted([x for x in student if group.issubset(set(x[1:]))])

if out:
    out = [" ".join(x) for x in out]
    print("\n".join(out))
else:
    print("Not Found")