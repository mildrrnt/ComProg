def make_int_list(x):
    x = [int(i) for i in x.split()] #split string into list of int
    return x

def is_odd(e): #check if number is odd
    if e%2 != 0:
        return True
    return False

def odd_list(alist):
    o = []
    for e in alist:
        if is_odd(e):
            o.append(e) #add odd number to the list
    return o

def sum_square(alist):
    for i in range(len(alist)):
        alist[i] = alist[i]**2 #square each member in list and assign to the same index
    return sum(alist) #sum of list

exec(input().strip())