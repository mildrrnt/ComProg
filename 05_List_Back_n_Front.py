n = int(input())
o = []
for i in range(n): #input n times
    o.append(int(input()))
o += [int(i) for i in input().split()] #input one line of number seperated by space and add to list
x = int(input())
while x != -1:
    o.append(x)
    x = int(input())
print(o[::-2]+o[::2] if len(o)%2 == 0 else o[-2::-2]+o[::2]) #if length of list is even, print list starting from the last number