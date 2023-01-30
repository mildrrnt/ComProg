d = int(input())
m = int(input())
y = int(input())-543 #convert
x = 0
dm = [31,28,31,30,31,30,31,31,30,31,30,31]

if y%400 == 0 or ((y%100) != 0 and (y%4) == 0): 
    dm[1] += 1 #dm[1] = dm[1] + 1

for i in range(1,m):
    x += dm[i-1]
print(x+d)
