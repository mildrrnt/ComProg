class roman:
    def __init__(self, r):
        self.r = r
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):            
        return self.r
    
    def __int__(self):
        val = {'I':1,'V':5,'X':10,'L':50,
               'C':100,'D':500,'M':1000,
               'IV':4,'IX':9,'XL':40,
               'XC':90,'CD':400,'CM':900}
        a = i = 0
        while i < len(self.r):
            if self.r[i:i+2] in val:
                a += val[self.r[i:i+2]]
                i += 2
            else:
                a += val[self.r[i]]
                i += 1
        return a
    def __add__(self, rhs):
        intval = int(self)+int(rhs)
        rval = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),\
                (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        out = ""
        for v,k in rval:
            while intval >= v:
                out += k
                intval -= v
        return roman(out)

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))