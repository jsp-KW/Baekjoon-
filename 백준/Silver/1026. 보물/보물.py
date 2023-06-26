import sys

n= int(input())

a= list(map(int, sys.stdin.readline().split()))
b= list(map(int, sys.stdin.readline().split()))

a.sort()

res =0
for i in range(n):
    res += a[i] * max(b)
    b.remove(max(b))

print(res)