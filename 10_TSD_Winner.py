n = int(input())
win,lose = set(),set()
for i in range(n):
    w,l = input().split()
    win.add(w)
    lose.add(l)
win = win - (win&lose)
print(sorted(list(win)))