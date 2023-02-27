t = input().strip()
a = [" !@#$%^&*())_+"," 90-="," qwertyuiop"," asdfghjkl"," zxcvbnm"]

output = []

def lessThan():
    if len(t) < 8:
        output.append("Less than 8 characters")

def Lower():
    for i in t:
        if 97 <= ord(i) <= 122:
            return True
    output.append("No lowercase letters")

def Upper():
    for i in t:
        if 65 <= ord(i) <= 90:
            return True
    output.append("No uppercase letters")

def Number():
    for i in t:
        if 48 <= ord(i) <= 58:
            return True
    output.append("No numbers")

def Sym():
    for i in t:
        if not (48 <= ord(i) <= 58 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
            return True
    output.append("No symbols")

def rep():
    res = [s for s in t]
    i = 0
    for n in (res):
        if res[i:i+4] == [n,n,n,n]:
            output.append("Character repetition")
            break
        i+=1

def asc(n,min,max):
    out = []
    x = 0
    for i in range(4):
        if n+x > max :
            n = min
            x = 0
            out.append(n)
        else:
            out.append(n+x)
        x+=1
    return out

def dsc(n,min,max):
    out = []
    x = 0
    for i in range(4):
        if n-x < min :
            n = max
            x = 0
            out.append(n)
        else:
            out.append(n-x)
        x+=1
    return out

def conseq(res,min,max):
    i = 0
    for n in (res):
        if res[i:i+4] == asc(n,min,max) or res[i:i+4] == dsc(n,min,max):
            return True
        i+=1

def numSeq():
    res = [int(i) for i in t if i.isdigit()]
    if len(res) < 4:
        return True
    if conseq(res,0,9):
        output.append("Number sequence")

def letSeq():
    res = [ord(s.lower()) for s in t if s.isalpha()]
    if conseq(res,97,122):
        output.append("Letter sequence")

def sepStr():
    return [t[i:i+4].lower() for i in range(len(t))]

def onKey():
    if len(t) < 4:
        return True
    for n in sepStr():
        if len(n) == 4:
            for i in a:
                f = i.find(n[0])
                if f != -1 and (n == i[f:f+4] or n == i[f:f-4:-1]):
                    output.append("Keyboard pattern")
                    break
    return True
            
lessThan()
Lower()
Upper()
Number()
Sym()
rep()
numSeq()
letSeq()
onKey()

if output == []:
    print("OK")
else:
    print(*output, sep = "\n")