i = input().split()
def findSum():
    n1,n2 = int(i[0],2),int(i[1],2) #convert to base 10
    s = n1+n2 #find sum
    return bin(s)[2:] #convert to binary and ignore 0b at the begining of the string
print(findSum())