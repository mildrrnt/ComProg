import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n,4),int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight,data

def report_lower_than_mean(weight,data):
    ids = np.array(data[:,0],str)
    total = np.dot(weight,data[:,1:].T)
    mean = np.mean(total)
    lower = ids[total<mean]
    print("None" if len(lower)==0 else ", ".join(ids[total<mean]))

exec(input().strip())