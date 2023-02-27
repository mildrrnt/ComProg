t = input().strip()
a = [" !@#$%^&*())_+"," 90-="," qwertyuiop"," asdfghjkl"," zxcvbnm"] #forsymbols & QWERTY check

output = []

def lessThan():
    if len(t) < 8:
        output.append("Less than 8 characters")

def Lower():
    for i in t:
        if 'a' <= i <= 'z':
            return True
    output.append("No lowercase letters")

def Upper():
    for i in t:
        if 'A' <= i <= 'Z':
            return True
    output.append("No uppercase letters")

def Number():
    for i in t:
        if i.isnumeric():
                return True
    output.append("No numbers")

def Sym():
    for i in t:
        if i in a[0] or i in a[1]:
            return True
    output.append("No symbols")

def rep():
    res = [s for s in t] #list of each character from input
    i = 0 #for indexing
    for n in (res): #for each char in list
        if res[i:i+4] == [n,n,n,n]: #4 char starting from that char == that char
            output.append("Character repetition")
            break
        i+=1

def asc(n,min,max): # n: each value in list, min value, max value
    out = [] #output list
    x = 0 #for adding
    for i in range(4): #loop 4 time to create list that contain 4 consectutive character
        if n+x > max : #if that value + adding is more than max value
            n = min #reassign that value to min value
            x = 0 #reset adding value to 0
            out.append(n) #append value to output list
        else:
            out.append(n+x) #append value + adding to output list
        x+=1 #increase adding value
    return out #list of 4 consecutive char

def dsc(n,min,max): #same as above function but in decreasing order
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

def conseq(res,min,max): # res: list for checking, min value, max value
    i = 0 #for indexing
    for n in (res): #for each value in list
        if res[i:i+4] == asc(n,min,max) or res[i:i+4] == dsc(n,min,max):
            return True
        i+=1

def numSeq():
    res = [int(i) for i in t if i.isdigit()] #list of only number in input
    if conseq(res,0,9):
        output.append("Number sequence")

def letSeq():
    res = [ord(s.lower()) for s in t if s.isalpha()] #list of only alphabet, convert to ASCII
    if conseq(res,97,122): #check with ASCII
        output.append("Letter sequence")

def sepStr(): #seperate input to list of 4 char, converted to lower case
    return [t[i:i+4].lower() for i in range(len(t))]

def onKey():
    if len(t) < 4: #skip if input is less than 4 char
        return True
    for n in sepStr(): #for each string in list of seperated 4 char
        for i in a: #for each string in list of QWERTY lines
            f = i.find(n[0]) #index of first letter of string 
            if f != -1 and (n == i[f:f+4] or n == i[f:f-4:-1]):
                #if it is found and is equal to the QWERTY str of index of f to f+4, or f to f-4 in reversed
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