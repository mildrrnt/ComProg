n = input()

def low():
    for i in n:
        if 'a' <= i <= 'z':
            return True
        
def up():
    for i in n:
        if 'A' <= i <= 'Z':
            return True
        
def num():
    for i in n:
        if i.isdigit():
            return True

if len(n) == 5 and low() and up() and num():
    print("Valid Password")
else:
    print("Invvalid Password")