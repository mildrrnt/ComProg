n = 0
sum_i = 0
i = input()
while i != "q":
  sum_i += float(i)
  n += 1
  i = input()
print(round((sum_i/n),2) if n > 0 else "No Data")