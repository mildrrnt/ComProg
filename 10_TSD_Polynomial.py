def find_tuple(num,p1): #to find if a tuple with that exponential exist
    result = [tup for tup in p1 if tup[1]==num]
    if result:
        return result[0]
    return None 

def add_poly(p1,p2):
    result = p1.copy() #make a copy so it doesn't modify the list
    for tuple in p2:
        num,expo = tuple[0],tuple[1]
        index = result.index(find_tuple(expo,result)) if find_tuple(expo,result) in result else -1
        #find the index of existing tuple
        if index == -1:
            result.append((num,expo))
        else:
            result[index] = (result[index][0]+num,expo) #add already exist num with expo with another num
    result = [(num,expo) for (num,expo) in result if num != 0] #remove the 0
    result.sort(key=lambda x: x[1], reverse = True)
    return result

def mult_poly(p1,p2):
    result = []
    for num1,expo1 in p1:
        for num2,expo2 in p2:
            if find_tuple(expo1+expo2,result) == None: #if tuple with the exponential of expo1+expo2 doesn't exist
                result.append((num1*num2,expo1+expo2))
            else: 
                index = result.index(find_tuple(expo1+expo2,result))
                result[index] = (result[index][0]+(num1*num2),result[index][1])
    result.sort(key=lambda x: x[1], reverse = True)
    return result

for i in range(3):
    exec(input().strip())