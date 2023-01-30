tel = input()
num = ["06","08","09"]

if len(tel) == 10 and (tel[:2] in num): #check if have 10 digits and begin with num
    print("Mobile number")
else:
    print("Not a mobile number")