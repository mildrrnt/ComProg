a = float(input())
L = 0
U = 1
k = a//10

while k != 0:
    U +=1
    k = k//10
b = (L + U) / 2
while abs(a-10**b) > max(a,b) * 10**(-10):
  if 10**b > a:
    U = b
  elif 10**b < a:
    L = b
  b = (L + U) / 2
print(round(b,6))