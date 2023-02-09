li = [int(i) for i in input().split()]
peak = 0
for i in range(1,len(li)-1): #starting with index 1 and end with the second last index
    if li[i] > li[i-1] and li[i] > li[i+1]:
        peak += 1
print(peak)