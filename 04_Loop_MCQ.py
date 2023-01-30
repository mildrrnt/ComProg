chk = input()
ans = input()
score = 0

if len(ans) < len(chk):
    print("Incomplete answer")
else:
    for i in range(len(chk)):
        if chk[i-1] == ans[i-1]:
            score+=1
    print(score)