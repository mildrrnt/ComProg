x = input()
i = [32]+[i for i in range(48,58)] + [i for i in range(65,91)] + [i for i in range(97,123)]
#list of ascii value, select only space, num, letters
letter = [chr(i) for i in i] #convert each num to character
o = ""
for ch in x:
    o += ch if ch in letter else " " #add only letter to the str, if not in list of letters, add space
o = o.split() #split into list of each word, seperated by space
o = o[0].lower() + "".join(ch.capitalize() for ch in o[1:]) #lowercase the first word, capitalize other
print(o)