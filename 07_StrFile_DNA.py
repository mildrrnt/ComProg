f = input().upper()
s = input()
p1 = ["A","T","G","C"]
p2 = ["T","A","C","G"] #reverse DNA pair

def isInvalid():
    x = f
    for i in p1:
        x = x.replace(i,"") #remove ATGC from the str
    if x != "": #if its not empty -> there are letters that are not in DNA
        return True

def rev():
    out = ""
    for i in f:
        out += p2[p1.index(i)] #add the DNA pair to output str
    print(out[::-1]) #reverse

def freq():
    a,t,g,c = f.count("A"),f.count("T"),f.count("G"),f.count("C") #assign multiple variables, count of each DNA pair
    print("A=%i, T=%i, G=%i, C=%i"%(a,t,g,c))

def disp():
    n = input()
    count = 0
    for i in range(len(f)):
        if f[i:i+2] == n: #that character and the character after it
            count +=1
    print(count)

if isInvalid():
    print("Invalid DNA")
else:
    if s=="R":
        rev()
    elif s=="F":
        freq()
    else:
        disp()