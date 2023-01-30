num = input()
a = int(num[3::7])
b = int(num[7::5])
c = str(a+b+10000)
d = str(int(c[-4:-1]))
sum = 0
for i in [int(x) for x in d]: sum+=i
sum = str(sum)
e = int((sum)[len(sum)-1])+1
f = chr(e+64)
print(d+f)