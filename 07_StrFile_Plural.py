ch = input()
if ch.endswith(('s','x','ch')):
 ch += "es"
elif ch[-1]=='y' and ch[-2] not in 'aeiou':
 ch = ch.replace(ch[-1],"ies")
else:
 ch += "s"
print(ch)