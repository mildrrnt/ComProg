data =  [['A102', 50], ['A103', 40], ['B014', 40], ['B109', 30]]

n = input().split(',')
n[1] = int(n[1])

data.append(n)
data.sort(key = lambda x: x[1])
data.reverse()
print(data)