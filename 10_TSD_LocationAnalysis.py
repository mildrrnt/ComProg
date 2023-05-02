d = {}

for i in range(int(input())):
    id, city = input().split(": ")
    d[id] = set(city.split(", "))

keyID = input()
citylist = d[keyID]

k = True
li = []
for key,value in d.items():
    for city in citylist:
      if city in value and key != keyID:
          k =False
          li.append(key)
          break

print("Not Found" if not li else "\n".join(li))