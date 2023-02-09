spe = ["'",'"',"(",")",",","."]
key = input()
sen = input()

for ch in spe:
    sen = sen.replace(ch," ") #replace each char with space

sen = sen.split() #split into list / does not count space
        
print(sen.count(key))
