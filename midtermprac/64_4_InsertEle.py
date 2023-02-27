data =  [['A102', 20], ['A014', 40], ['B104', 40], ['B109', 30]]

n = input().split(',')
n[1] = int(n[1])

data.append(n)
data.sort()
data.sort(key = lambda x: x[1], reverse=True)
print(data)