li = []
sum = 0
while True :
  x = input()
  if x == 'q': #quit if input = q
    break
  li.append(float(x)) #append list with x
if li == []:
  print('No Data')
else:
  for i in li: #can be done using sum(li)
    sum += i
  avg = round((sum/len(li)),2)
  print(avg)