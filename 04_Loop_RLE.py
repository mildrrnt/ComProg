l = input()
n = ""
'''
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

'''
c = 1
for i in range(1,len(l)):
    if l[i-1] == l[i]:
        c += 1
    else:
        print(l[i-1],c,end=" ")
        c = 1
print(l[-1],c)