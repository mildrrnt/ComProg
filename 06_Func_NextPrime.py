def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(n):
    n+=1
    while not is_prime(n): #if not prime continue to increase n
        n+=1
    return n

def next_twin_prime(n):
    n1 = next_prime(n)
    n2 = next_prime(n1)
    while (n2-n1) != 2: #if its not the next consecutive prime
        n1 = next_prime(n1) #find the next prime number
        n2 = next_prime(n1)
    return n1,n2
exec(input().strip()) #execute input