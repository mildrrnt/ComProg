x = input()
out = ""
while x != "end":
    for i in x:
        y = ord(i)
        if 77 < y <= 90 or 109 < y <= 122: #ascii value, last 13 of uppercase & lowercase
            out += chr(y-13)
        elif 65 <= y <=77 or 97<= y <= 109: #ascii value, first 13 of uppercase & lowercase
            out += chr(y+13)
        else:
            out += i #add other (special letters/numbers etc.)
    out += "\n"
    x = input()

print(out)