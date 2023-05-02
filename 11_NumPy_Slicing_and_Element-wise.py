import numpy as np

def sum_2_rows(M):
    return M[::2,:] + M[1::2,:]

def sum_left_right(M):
    col = M.shape[1]
    return M[:,:col//2] + M[:,col//2:]

def sum_upper_lower(M):
    row = M.shape[0]
    return M[:row//2,:]+M[row//2:,:]

def sum_4_quadrants(M):
    return sum_left_right(sum_upper_lower(M))

def sum_4_cells(M):
    return M[::2,::2]+M[1::2,::2]+M[::2,1::2]+M[1::2,1::2]

def count_leap_years(years):
    y = years-543
    return sum((y%400==0)|((y%4==0)&(y%100!=0)))

exec(input().strip())