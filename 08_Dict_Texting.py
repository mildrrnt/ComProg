ref = {'abc':'2','def':'3','ghi':'4','jkl':'5','mno':'6','pqrs':'7','tuv':'8','wxyz':'9',' ':'0'}


def text2keys(text):
    t = ""
    out = []
    for ch in text.lower():
        if ch.isalpha() or ch == ' ':
            t+=ch
    for i in t:
        x = [k for k,v in ref.items() if i in k][0]
        y = x.index(i) +1 
        out.append(ref[x]*y)
    return " ".join(out)

def keys2text(text):
    t = text.split()
    out = []
    for i in t:
        x = i[0]
        y = len(i)-1
        z = [k for k,v in ref.items() if v == x][0][y]
        out.append(z)
    return "".join(out)


exec(input().strip())