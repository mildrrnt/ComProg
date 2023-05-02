songs = {}

for i in range(int(input())):
    s = input().strip().split(", ")
    time = s[3].split(":")
    t = int(time[0])*60 + int(time[1])
    if s[2] in songs:
        songs[s[2]] += t
    else:
        songs[s[2]] = t

songs = (sorted(songs.items(), key=lambda x: x[1],reverse=True)[:3])

for genre,time in songs:
    min = time//60
    sec = time%60
    if sec<=10:
        sec = "0"+str(sec)
    print("%s --> %s:%s"%(genre,min,sec))