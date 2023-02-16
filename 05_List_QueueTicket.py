n = int(input())
k = [input() for i in range(n)] #operation
q = [] #queue number
t = [] #start time
dif = [] #time difference
i = 0 #for indexing

for key in k:
    c = key.split()
    if c[0] == 'reset':
        num = int(c[1]) #set start value
    elif c[0] == 'new':
        q.append(num) #add queue number to list
        t.append(int(c[1])) #add time to list
        print("ticket",num) #print queue number
        num +=1 #increase queue number
    elif c[0] == 'next':
        print("call",q[i]) #call index i from queue number list
        i += 1 #increase index for the next call
    elif c[0] == 'order':
        dt = int(c[1]) - t[i-1] #time differece from new to order of the last queue number called
        dif.append(dt)
        print("qtime",q[i-1],dt) #the last queue number called
    elif c[0] == 'avg_qtime':
        avg = sum(dif)/len(dif)
        print("avg_qtime",round(avg,4))
