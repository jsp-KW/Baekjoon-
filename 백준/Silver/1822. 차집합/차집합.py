import sys

A = set()
B = set()

n,m = map(int,sys.stdin.readline().split())

temp = list(map(int,sys.stdin.readline().split()))

for t in temp :
    A.add(t)

temp2 = list(map(int,sys.stdin.readline().split()))


for t in temp2 :
    B.add(t)

result = len(A-B)
if result == 0 :
    print (0)
else:
    print (len(A-B))
    print (*sorted(A-B))
