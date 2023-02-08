spe = ["'",'"',"(",")",",","."]
key = input()
sen = input()

for ch in spe:
    sen = sen.replace(ch," ") #replace each char with space
        
print(sen.count(key))