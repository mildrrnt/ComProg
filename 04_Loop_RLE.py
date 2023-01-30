l = input()
n = ""
li = []

for d in l:
    if not d in n and n != "": #new character
        li.append(n)
        n = d
    else: #same character
        n += d
li.append(n) #append last set of char into list
x = ""
for s in li:
    x += s[0]+" "+ str(len(s))+" "

print(x[:-1]) #exclude the last space