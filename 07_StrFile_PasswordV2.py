t = input().strip()
a = "!@#$%^&*())_+-=qwertyuiopasdfghjklzxcvbnm"
alpha = "abcdefghijklmnopqrstuvwxyz"

output = []

def lessThan():
    if len(t) < 8:
        output.append("Less than 8 characters")

def Lower():
    for i in t:
        if i in alpha:
            return True
    output.append("No lowercase letters")

def Upper():
    for i in t:
        if i in alpha.upper():
            return True
    output.append("No uppercase letters")

def Number():
    for i in t:
        if i.isnumeric():
            return True
    output.append("No numbers")

def Sym():
    for i in t:
        if i in a[:15]:
            return True
    output.append("No symbols")

def rep():
    for i in range(len(t)-4):
        if t[i:i+4] == t[1]*4:
            output.append("Character repetition")
            break

def numSeq():
    for i in range(len(t)-4):
        if t[i:i+4] in "0123456789":
            output.append("Number sequence")
            break


def letSeq():
    for i in range(len(t)):
        x = alpha.find(t[i])
        y = alpha.upper().find(t[i])
        if t[i:i+4] in alpha[x:x+4] or t[i:i+4] in alpha[y:y+4]:
            output.append("Letter sequence")
            break
        

def sepStr():
    return [t[i:i+4].lower() for i in range(len(t)-4)]

def onKey():
    for i in range(len(t)-4):
        if t[i:i+4].lower() in a or t[i:i+4].lower() in a[::-1]:
            output.append("Keyboard pattern")
        return False
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