k = int(input())
n = input().split()

n[k-1] = n[k-1][::-1]
print(" ".join(n))