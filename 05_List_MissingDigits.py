n = input()
o = ""
for i in range(0,10):
    if not str(i) in n:
        o = o+str(i)+"," #if number is not in string, add that number to output
print("None" if o == "" else o[:-1]) #if output sting if empty (no missing number) print none, if not print output exclude the last comma