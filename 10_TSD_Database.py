id = open(input(),"r")
prof = open(input(),"r")
pair = open(input(),"r")

id_dict = dict()
prof_dict = dict()
pair_li = list()

def adddict(f,dic):
    for l in f:
        num,data = l.strip().split(",")
        dic[num] = data

adddict(id,id_dict)
adddict(prof,prof_dict)

for l in pair:
    i,p = l.strip().split(",")
    print(id_dict[i]+","+prof_dict[p] if i in id_dict and p in prof_dict else "record error")