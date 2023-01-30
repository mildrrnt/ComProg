s = input()
n = int(s)

if len(s) > 10:
    print(str(round(n/1000000000))+"B")
elif len(s) == 10:
    print(str(round((n/1000000000),1))+"B")
elif len(s) > 7:
    print(str(round(n/1000000))+"M")
elif len(s) == 7:
    print(str(round((n/1000000),1))+"M")
elif len(s) > 4:
    print(str(round(n/1000))+"K")
elif len(s) == 4:
    print(str(round((n/1000),1))+"K")
else:
    print(s)
