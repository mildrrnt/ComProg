spe = ["'",'"',"(",")",",","."]
key = input()
sen = input()

for ch in spe:
    if ch in sen:
        sen = sen.replace(ch," ") #replace each char with space

sen = sen.split() #split into list / does not count space
count = 0

for s in sen:
    if s == key: #check if the word is keyword or not
        count += 1
        

print(count)
