import numpy as np

def toCelsius(f):
    return (f-32)*5/9

def BMI(wh):
    return wh[:,0]/(wh[:,1]/100)**2

def distanceTo(p,P):
    x = p[0]-P[:,0]
    y = p[1]-P[:,1]
    return (x**2 + y**2)**0.5

exec(input().strip())