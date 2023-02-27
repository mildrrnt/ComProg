import math as m
n = int(input())
low = m.sqrt(2*m.pi)*n**(n+0.5)*m.exp(-n+(1/(12*n+1)))
high = m.sqrt(2*m.pi)*n**(n+0.5)*m.exp(-n+(1/(12*n)))
print(low,high)