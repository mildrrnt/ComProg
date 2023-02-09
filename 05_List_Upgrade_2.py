first = input()
num = []
grade = []
grade_up = ["F","D",'D+',"C","C+","B","B+","A","A"]
while first != "q":
    li = first.split()
    num.append(li[0])
    grade.append(li[1])
    first = input()

check = input().split()
output = []
for i in check:
    grade_index = grade_up.index(grade[num.index(i)]) + 1
    #find index of the grade that will be upgraded and find index of that grade in upgrade list and +1 to shift to higher grade
    grade[num.index(i)] = grade_up[grade_index]
for i in range(len(num)):
    st = num[i] + " " + grade[i] #join string
    output.append(st) #append to output list

output.sort() #sort the list ascending order
print("\n".join(output)) #join output into string