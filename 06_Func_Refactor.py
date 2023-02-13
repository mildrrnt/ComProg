mname = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
zname = ["Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn"]
mday = [31,28,31,30,31,30,31,31,30,31,30,31,0]

def read_date():
    date = [i for i in input().split()]
    date[1] = mname.index(date[1]) + 1
    date = [int(i) for i in date]
    return date

def zodiac(d,m):
    if d >= 22 and m >2 or d >= 21 and m <= 2: #condition of zodiac sign of that month (mainly)
        z = zname[m-1]
    else: #zodiac sign of the previous month(mainly)
        z = zname[m-2]
    return z

def days_in_feb(y):
    if y %400 ==0 or y%100 !=0 and y%4 ==0: #condition when feb has 29 days
        return 29
    return 28

def days_in_month(m,y):
    mday[1] = days_in_feb(y) #set if feb gonna be 28 or 29
    return mday[m-1] #check how many days that month has

def days_in_between(d1,m1,y1,d2,m2,y2):
    n1 = d1
    n2 = d2
    n = 0 #number of days passed in case more than a year pass
    while y1 < y2: #loop until they are the same year
        for i in range(12):
            n += days_in_month(i+1,y1)
        y1 += 1 #increasing
    for i in range(m1-1): 
            n1 += days_in_month(i+1,y1) #number of days since new year
    for i in range(m2-1):
            n2 += days_in_month(i+1,y2) #number of days since new year
    return n2-n1+n-1 #dif of number of days since new year + number of days passed (years) - today

    

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1), end=" ")
    print(zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

exec(input().strip())