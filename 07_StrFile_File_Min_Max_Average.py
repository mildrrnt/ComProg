x = input().split()
n = x[0] #file name
y = x[1][-2:] #select year from last two digit
fn = open(n,"r") #open file
score = []

for ln in fn:
    ln = ln.split() #seperate into student id and score
    if ln[0].startswith(y): #check if the first two digit of studnet id == selected year
        score.append(float(ln[1]))

if score ==[]:
    print("No data")
else:
    print(min(score),max(score),(round(sum(score)/len(score),2)))